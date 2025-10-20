# namedtuple()
from collections import namedtuple
point = namedtuple('point',['x','y']) # 创建namedtuple数据类型
p = point(1,2)  # 创建实例
print(p.x,p.y)  # 输出 1 2，通过字段名访问

# deque

from collections import deque

q = deque(['a','b','c'])
q.append('m')  # 在尾部增加`m`
print(q)
q.pop()        # 删除尾部的元素
q.appendleft('u') # 头部添加 `u`
print(q)
q.popleft()    # 头部删除
print(q)
"""
输出
deque(['a', 'b', 'c', 'm'])
'm'
deque(['u', 'a', 'b', 'c'])
'u'
deque(['a', 'b', 'c'])
"""

# orderdict

d1 = {'a':1,'b':2}
d2 = {'b':2,'a':1}
print(d1 == d2)   # 输出 True ，内容相同即相等

from collections import OrderedDict
ord1 = OrderedDict([('a',1),('b',2)])
ord2 = OrderedDict([('b',2),('a',1)])
print(ord1 == ord2)  # 输出 False，有序字典顺序需要进行比较

# defaultdict案例1:计数器的实现
## 经典写法
count = {}
for char in "hello":
    if char not in count :
        count[char]=0
    count[char]+= 1
print(count)   # 输出 {'h': 1, 'e': 1, 'l': 2, 'o': 1}

## defaultdict 方法
from collections import defaultdict

count = defaultdict(int)
for char in "hello":
    count[char] += 1
print(count)  # 输出 defaultdict(<class 'int'>, {'h': 1, 'e': 1, 'l': 2, 'o': 1})

# defaultdict案例2:统计单词首字母分组
from collections import defaultdict

words = ["apple","banana",'avocado','blueberry']
index = defaultdict(list)  # 初始化

for word in words:
    first_char = word[0]
    index[first_char].append(word) # 无序判断键是否存在
print(index['a'])  # 输出 ['apple', 'avocado']
print(index['b'])  # 输出 ['banana', 'blueberry']

# counter
from collections import Counter
c = Counter('qaasccwcqwcwqcfrg')
print(c)  # 输出 Counter({'c': 5, 'q': 3, 'w': 3, 'a': 2, 's': 1, 'f': 1, 'r': 1, 'g': 1})


# 三种时间格式的转换
import time

# 1. 时间戳
ts = time.time()
print("时间戳:", ts)

# 2. 转 struct_time
st = time.localtime(ts)
print("结构化时间:", st)

# 3. 转格式化字符串
fmt_str = time.strftime('%Y-%m-%d %H-%M-%S', st)
print("格式化时间:", fmt_str)

# 4. 格式化字符串转回 struct_time
st2 = time.strptime(fmt_str, '%Y-%m-%d %H-%M-%S')
print("解析回 struct_time:", st2)

# 5. struct_time 转回时间戳
ts2 = time.mktime(st2)
print("还原时间戳:", ts2)

# 计算时间差
import time

s_time = time.mktime(time.strptime('2017-09-11 08:30:00','%Y-%m-%d %H:%M:%S'))
e_time = time.mktime(time.strptime('2025-10-12 10:08:00','%Y-%m-%d %H:%M:%S'))
dif_time = e_time - s_time
struct_time = time.gmtime(dif_time)
print('已经过去了%d年%d月%d天%d小时%d分钟%d秒'%(struct_time.tm_year-1970,struct_time.tm_mon-1,struct_time.tm_mday-1,struct_time.tm_hour,struct_time.tm_min,struct_time.tm_sec))
"""
输出
    已经过去了8年1月0天1小时38分钟0秒
"""



# datetime常用操作示例
from datetime import datetime, timezone, timedelta

# 1. 当前 UTC 时间（带时区）
now_utc = datetime.now(timezone.utc)  
print(now_utc) # 输出 2025-10-16 03:04:43.415994+00:00

# 2. 转为字符串
s = now_utc.strftime('%Y-%m-%d %H:%M:%S %Z') # 
print(s) # 输出 2025-10-16 02:53:07 UTC
# 3. 加 7 天
future = now_utc + timedelta(days=7)
print(future) # 输出 2025-10-23 02:53:07.507475+00:00

# 4. 转时间戳
ts = future.timestamp()
print(ts) # 输出 1761187872.260256

# 5. 从时间戳还原（还原成人类看一看明白的信息）
back = datetime.fromtimestamp(ts, tz=timezone.utc)
print(back)   # 输出 2025-10-23 02:51:12.260256+00:00

print("原始:", now_utc)  # 输出 原始: 2025-10-16 02:51:12.260256+00:00
print("7天后:", future)  # 输出 7天后: 2025-10-23 02:51:12.260256+00:00
print("还原:", back)     # 输出 还原: 2025-10-23 02:51:12.260256+00:00