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