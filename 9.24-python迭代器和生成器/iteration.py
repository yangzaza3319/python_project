"""
迭代相关代码
"""

# 1.迭代的引入
li = [1,2,3,'a','b','c']
for i in li:
    print(i)

str = "hello,world"
for j in str:
    print(j)

dic = {'name':'yc','age':18,'job':'teacher'}
for k,v in dic.items():
    print(k,v)

"""
输出
>>> li = [1,2,3,'a','b','c']
>>> for i in li:
...     print(i)
... 
1
2
3
a
b
c
>>> str = "hello,world"
for j in str:
...     print(j)
... 
h
e
l
l
o
,
w
o
r
l
d
dic = {'name':'yc','age':18,'job':'teacher'}
for k,v in dic.items():
...     print(k,v)
... 
name yc
age 18
job teacher
"""

# 2.判断是否为可迭代对象
from collections.abc import Iterable

list = [1,2,3,4]
temple = (1,2,3,4)
dict = {1:2,3:4,5:6}
set = {1,2,3,4}
a = 100

print(isinstance(list,Iterable))
print(isinstance(temple,Iterable))
print(isinstance(dict,Iterable))
print(isinstance(set,Iterable))
print(isinstance(a,Iterable))

"""
输出
from collections.abc import Iterable
list = [1,2,3,4]
tumple = (1,2,3,4)
dict = {1:2,3:4,5:6}
set = {1,2,3,4}
a = 100
print(isinstance(list,Iterable))      # 列表可迭代
True 
print(isinstance(tumple,Iterable))    # 元组可迭代
True
print(isinstance(dict,Iterable))      # 字典可迭代
True
print(isinstance(set,Iterable))       # 集合可迭代
True
print(isinstance(a,Iterable))         # 整数不可迭代
False
"""


list = [1,2,3,4]
tuple = (1,2,3,4)
dict = {1:2,3:4}
set = {1,2,3,4}

print(dir(list))
print(dir(tuple))
print(dir(dict))
print(dir(set))

"""
输出结果
这四种数据类型都有`__iter__`方法
print(dir(list))
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
print(dir(tuple))
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
print(dir(dict))
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
print(dir(set))
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
"""

# 3.1 初始化迭代器
list1 = [1,2,3,'a','b','c']
list_iter = list1.__iter__()
item = list_iter.__next__()
print(item)                # 输出 1
item = list_iter.__next__()
print(item)                # 输出 2
item = list_iter.__next__()
print(item)                # 输出 3
item = list_iter.__next__()
print(item)                # 输出 a
item = list_iter.__next__()
print(item)                # 输出 b
item = list_iter.__next__()
print(item)                # 输出 c
item = list_iter.__next__()
print(item)               # 报错，抛出`StopIteration异常`

# 3.2 初始化迭代器（写法2）
list2 = [1,2,3,'a','b','c']

list_iter = list2.__iter__()
while True:
    try:
        print(next(list_iter))
    except StopIteration:
        print("迭代结束")
        break


# 4. 判断一个对象是否为迭代器
from collections.abc import Iterator
list3 = [1,2,3,'a','b','c']

list_iter = list3.__iter__()

print(isinstance(list1,Iterator))  # 输出 False，list1非迭代器
print(isinstance(list_iter,Iterator))  # 输出True，list_iter为迭代器
print(isinstance(iter(list3),Iterator))# 输出True，iter()函数返回迭代器