# 生成器函数
def numbers(n):
    """生成1到n的自然数"""
    for i in range(1,n+1):
        yield i

for i in numbers(10):
    print(i)

# 案例1 现包现卖包子
def produce():
    for i in range(1,100):
        yield f'第{i}笼包子出炉'

gen = produce()
print(gen.__next__()) # 小客户要了第1笼包子
print(gen.__next__()) # 小客户要了第2笼包子
print(gen.__next__()) # 小客户要了第3笼包子
print(gen.__next__()) # 小客户要了第4笼包子

for i in range(5):
    print(gen.__next__())
"""
输出
>>> gen = produce()
>>> print(gen.__next__()) # 小客户要了第1笼包子
第1笼包子出炉
>>> print(gen.__next__()) # 小客户要 了第2笼包子
第2笼包子出炉
>>> print(gen.__next__()) # 小客户要 了第3笼包子
第3笼包子出炉
>>> print(gen.__next__()) # 小客户要 了第4笼包子
第4笼包子出炉
>>> for i in range(5):
...     print(gen.__next__())
... 
第5笼包子出炉
第6笼包子出炉
第7笼包子出炉
第8笼包子出炉
第9笼包子出炉
"""

# send案例

def generator():
    print(123)
    content = yield 1
    print('我爱',content)
    print(456)
    yield 2

g = generator()
ret = g.__next__()
print('***',ret)
ret = g.send('Python')
print('***',ret)