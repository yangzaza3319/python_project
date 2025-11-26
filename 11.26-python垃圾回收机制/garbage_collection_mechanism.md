"""
python的垃圾回收机制
"""
## python的垃圾回收机制
> 垃圾回收机制(简称GC garbage collection)是python解释器自带的一种机制，专门用来回收不可用的变量值所占用的内存空间
> 程序运行过程中会申请大量的内存空间，而对于一些无用的内存空间如果不及时清理的话会导致内存使用殆尽(即内存溢出)，导致程序崩溃，因此管理内存是一件重要且繁杂的事情，而python
解释器自带的垃圾回收机制会把程序员从繁杂的内存管理中解放出来
### 内存管理和垃圾回收
PythonGC主要使用引用计数(reference counting)来跟踪和回收垃圾。在引用计数的基础上，通过“标记·清除（mark and sweep）”解决容器对象可能产生的循环引用问题，通过“分代回收”以空间换时间的方法提高垃圾回收效率
python采用的是引用计数机制为主，标记-清除和分代手机两种机制为辅的策略

## 引用计数（reference count）
pyObject是每个对象必有的内容，其中ob_refcnt就是作为引用计数。当一个对象有新的引用时，它的ob_refcnt就会增加，当引用它的对象被删除，它的ob_refcnt就会减少，当引用计数为0时，该对象生命就结束了
### 工作原理
1. 引用计数增加
   - 对象被创建
   - 对象被引用
   - 对象被作为参数，传到函数中
   - 对象作为一个元素，存储在元素中
```python
a = 14   # 对象被创建
b = a    # 对象被引用
fun(a)   # 对象被作为参数，传到函数中
List = [a,"a","b",2]   # 对象作为一个元素，存储在容器中
```
2. 引用计数减少
    - 对象被显式销毁
    - 变量重新赋予新的对象
    - 对象离开他的作用域
    - 对象所在的容器被销毁，或从容器中删除对象
```python
# 此段代码继承上一段代码
del a # 删除a的引用，引用次数减为1
del b # 删除b的引用，此时引用次数减为0，内存被释放
```
#### 工作原理案例
```python
import sys
import gc

class MyObject:
    def __init__(self, name):
        self.name = name
        print(f"[+] 对象 {self.name} 被创建")

    def __del__(self):
        print(f"[-] 对象 {self.name} 被销毁")


def main():
    print("\n=== 场景：基础引用计数 ===")
    a = MyObject("A")

    # sys.getrefcount(a) 会临时增加一个引用（传参），所以结果 = 实际引用数 + 1
    print("创建 a 后引用计数:", sys.getrefcount(a))  # 应为 2：a + getrefcount 内部引用

    List = [1, a]
    print("加入列表后引用计数:", sys.getrefcount(a))  # 应为 3：a + List[1] + getrefcount

    b = a
    print("赋值给 b 后引用计数:", sys.getrefcount(a))  # 应为 4：a + b + List[1] + getrefcount

    del b
    print("删除 b 后引用计数:", sys.getrefcount(a))   # 回到 3

    del a
    print("删除 a 后，对象 A 是否立即销毁？")
    # 此时只有 List 中还持有引用，所以不会销毁

    print("当前列表 List 仍包含对象 A")
    print("手动清空列表或删除 List 后才会销毁")

    del List  # 现在没有引用了，触发 __del__

    # 强制垃圾回收（虽然通常不需要）
    gc.collect()

if __name__ == "__main__":
    main()

'''
=== 场景：基础引用计数 ===
[+] 对象 A 被创建
创建 a 后引用计数: 2
加入列表后引用计数: 3
赋值给 b 后引用计数: 4
删除 b 后引用计数: 3
删除 a 后，对象 A 是否立即销毁？
当前列表 List 仍包含对象 A
手动清空列表或删除 List 后才会销毁
[-] 对象 A 被销毁

'''
```