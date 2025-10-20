# print()

print(11,22,33,sep='*') # 输出 11*22*33
print(11,22,33)         # 输出 11 22 33，默认分隔符为空格
print(11,22,33,end='*') # 输出 11 22 33*，以*结尾
print(11,22,33,end='')  # 将结尾的换行符`\n`替换为空格，结果是输出`11 22 33`结束后不会自动换行
with open('log','w',encoding='utf-8') as f:
    print('写入文件',file=f,flush=True) # 代码执行后上述两行代码执行之后，会生成一个名为log，内容为写入文件的文件

# hash()
print(hash(112233))  # 整数的哈希值为它本身
print(hash('123'))   # 字符串的哈希值与python版本以及环境相关
print(hash(True))    # 布尔值true在数值上等同于1，其哈希值为1
print(hash((1,2,3))) # 实际值与环境有关

# id()
print(id('abc'))    # 输出 4365371552
print(id('123'))    # 输出 4377932976


# help()
print(help(print))
"""
输出
Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.

    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.
"""

# callable()
print(callable(0))       # 输出 False
print(callable('hello'))  # 输出 False
def demo1(a,b):   # 自定义函数
    return a + b
print(callable(demo1))  # 输出 True

class demo2:     # 自定义类
    def test1(self):
        return 0
print(callable(demo2))  # 输出 True

a = demo2()
print(callable)        # 输出 <built-in function callable>

# dir()
import time
print(dir(time))
print(dir([]))
"""
输出
['CLOCK_MONOTONIC', 'CLOCK_MONOTONIC_RAW', 'CLOCK_MONOTONIC_RAW_APPROX', 'CLOCK_PROCESS_CPUTIME_ID', 'CLOCK_REALTIME', 'CLOCK_THREAD_CPUTIME_ID', 'CLOCK_UPTIME_RAW', 'CLOCK_UPTIME_RAW_APPROX', '_STRUCT_TM_ITEMS', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'altzone', 'asctime', 'clock_getres', 'clock_gettime', 'clock_gettime_ns', 'clock_settime', 'clock_settime_ns', 'ctime', 'daylight', 'get_clock_info', 'gmtime', 'localtime', 'mktime', 'monotonic', 'monotonic_ns', 'perf_counter', 'perf_counter_ns', 'process_time', 'process_time_ns', 'sleep', 'strftime', 'strptime', 'struct_time', 'thread_time', 'thread_time_ns', 'time', 'time_ns', 'timezone', 'tzname', 'tzset']

['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
"""

# iter()
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