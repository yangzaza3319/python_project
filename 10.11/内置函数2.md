## 内置函数2
### 输入/输出相关
#### 1. `input()`
> 接受一个标准输入数据，返回为`string`类型
#### 2. `print()`
> 打印输出
#### 源码分析
```python
print(value,...,sep='',end='\n',file=sys.stout,flush=False)
file ——> 指定输出文件，默认输出到屏幕
sep ——> 打印多个值之间的分隔符，默认为空格
end ——> 每一次打印的结尾，默认为换行符
flush ——> 立即把内容输出到流文件，不做缓存 
```
#### 代码案例
```python
print(11,22,33,sep='*') # 输出 11*22*33
print(11,22,33)         # 输出 11 22 33，默认分隔符为空格
print(11,22,33,end='*') # 输出 11 22 33*，以*结尾
print(11,22,33,end='')  # 将结尾的换行符`\n`替换为空格，结果是输出`11 22 33`结束后不会自动换行
with open('log','w',encoding='utf-8') as f:
    print('写入文件',file=f,flush=True) # 代码执行后上述两行代码执行之后，会生成一个名为log，内容为写入文件的文件
```

### 内存相关
#### 1. `hash()`
> 获取一个可哈希对象的哈希值（int、str、bool、tuple）
```python
print(hash(112233))  # 整数的哈希值为它本身
print(hash('123'))   # 字符串的哈希值与python版本以及环境相关
print(hash(True))    # 布尔值true在数值上等同于1，其哈希值为1
print(hash((1,2,3))) # 实际值与环境有关
```

#### 2. `id()`
> 用于获取对象的内存地址
```python
print(id('abc'))    # 输出 4365371552
print(id('123'))    # 输出 4377932976
```
### 文件操作相关
#### 1. `open()`
> 用于打开一个文件，创建一个file对象

#### 2.`read()`
> 通过文件对象调用，读取文件的内容

#### 3. `write()`
> 通过调用文件对象，往文件尾部插入内容

### 帮助文档相关
#### `help()`
> 用于查看函数或模块用途的详细说明

```python
print(help(print))
```

### 调用相关的函数
#### `callable()`
> 用于检查一个对象是否可调用——>如果返回True，object仍然可能调用失败；返回True，调用对象objet永远不会成功
```python
print(callable(0))
print(callable('hello'))
def demo1(a,b):
    return a + b
print(callable(demo1))
```

### 查看内置属性
#### `dir()`
> 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表
> 如果参数包含方法`__dir__()`,该方法将被调用；如果参数不包含方法`__dir__()`,该方法将最大限度的收集参数信息
```python
import time
print(dir(time))
print(dir([]))
```

### 迭代器生成器相关

#### range()
> 函数可创建一个整数对象，一般用在for循环中

#### next()
> 内部实际使用了`__next()__`方法，返回迭代器等下一个项目

#### iter()
> 用于生成迭代器
```python
from collections import Iterator,Iterable

l = [1,2,3,4]  # 首先获得Iterator
l1 = iter(l)

print(isinstance(l1,Iterable)) # 输出 True
print(isinstance(l1,Iterator)) # 输出 True

# 循环 
while True:
    try:
        x = next(l1) # 获取下一个值
        print(x)
    except StopIteration:  # 遇到不可迭代时退出循环
        break
```