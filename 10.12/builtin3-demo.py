# int()

print(int())        # 输出 0
print(int('12'))    # 输出 12
print(int(3.6))     # 输出 3
print(int('0100',base=2))  # 输出4，将2进制的0100转化为十进制

# complex()
z1 = complex(2,3)
print(z1)           # 输出 2+3j

# bin()
b = bin(10)
print(b)            # 输出 0b1010
print(type(b))      # 输出 <class 'str'>
print(type(bin(10)))# 输出 <class 'str'>

# oct()
print(oct(10),type(oct(10))) # 输出 0o12 <class 'str'>

# hex()
print(hex(10),type(hex(10))) # 输出 0xa <class 'str'>

# abs()
print(abs(-5),abs(13)) # 输出 5 13

# divmod()
print(divmod(7,2)) # 输出 (3,1) ——>商为3，余数为1
print(divmod(4,2)) # 输出（2，0）——>商为2，余数为0

# round()
print(round(7/3))        # 输出 2
print(round(7/3,2))      # 输出 2.33
print(round(3.32567,3))  # 输出 3.326

# pow()
print(pow(2,3))    # 输出 8
print(pow(2,3,3))  # 输出 2

# sum()
print(sum(2,3))       # 报错，整数2不是可迭代对象
print(sum([2,3],10))  # 输出 15

# min()
print(min([1,2,-2]))            # 输出 -2
print(min([1,2,-5],key = abs))  # 输出 1 （指定key=abs，比较绝对值）

# max()
print(max([1,2,-5]))            # 输出 2
print(max([1,2,-5],key = abs))  # 输出 -5


# list()
print(list((1,2,3)),list({1,2,3}),list({'key':'value'}))  # 输出 [1, 2, 3] [1, 2, 3] ['key']

# tuple()
print(tuple([1,2,3]),tuple({'key':'value'}))   # 输出 (1, 2, 3) ('key',)

# format()
## 字符串提供的参数
print('|<——',format('test','<20'),'——>|') # 输出 |<—— test                 ——>|
print('|<——',format('test','>20'),'——>|') # 输出 |<——                 test ——>|
print('|<——',format('test','^20'),'——>|') # 输出 |<——         test         ——>|

## 整型数值提供的参数
print(format(192,'b'))         # 输出 11000000
print(format(128512,'c'))      # 输出 😀
print(format(10111000,'d'))    # 输出 10111000,因为在python中，不加特殊的标志的数字全部都是整数
print(format(0b10111000,'d'))  # 输出 184
print(format(0b10111000,'o'))  # 输出 八进制数字 270
print(format(0b10111000,'x'))  # 输出 十六进制数字 b8
print(format(0b10111000,'X'))  # 输出 十六进制数字 B8
print(format(0b10111000,'n'))  # 输出 十进制数字 184
print(format(0b10111000,''))  # 输出 十进制数字 184

## g 参数格式化
print(format(123.456789, '.3g'))   # 输出: 123
print(format(123.456789, '.5g'))   # 输出: 123.46
print(format(0.000123456, '.3g'))  # 输出: 0.000123
print(format(123456789, '.3g'))    # 输出: 1.23e+08
print(format(0.000000123, '.3g'))  # 输出: 1.23e-07

# repr()
s = "Hello\nWorld\t!"
print(s)       
"""
输出
Hello
World   !
"""
print(repr(s)) # 输出 'Hello\nWorld\t!'

# reversed()
ite = reversed(['a',2,4,'f',12,6]) 
for i in ite:
    print(i)
"""
输出
6
12
f
4
2
a
"""
ite = reversed(['a',2,4,'f',12,6]) 
for i in ite:
    print(i)
for k in ite:
    print(k)
"""
输出
6
12
f
4
2
a
 # ——>此处为空格，因为第二次循环取不到反转后的迭代器（迭代器为一次性消耗品）
"""


# slice()
l = ['1','2','3','4','5','6','7','8','9']
sli = slice(3)      # 取序列的前三个数
print(l[sli])       # 输出 ['1', '2', '3'] 等价于 print(l[slice(3)])  
print(l[slice(3)])  # 输出 ['1', '2', '3']
print(l[slice(0,10,2)]) # 输出 ['1', '3', '5', '7','9']

# sorted()
num =  [1,0,0,8,6]
print(sorted(num))              # 输出 [0,0,1,6,8]
print(sorted(num,reverse=True)) # 输出 [8, 6, 1, 0, 0]

word = ["中华人民共和国",'漂亮国','岛国小日本']
print(sorted(word,reverse=True,key=len)) # 输出 ['中华人民共和国', '岛国小日本', '漂亮国']

# enumerate()
print(enumerate(['a','b','c'])) # 输出 <enumerate object at 0x1034e70b0> ，因为enumerate()方法返回的是迭代器对象，python为了节省内存不能直接用print()
for i in enumerate(['a','b','c']):
    print(i)
for i in enumerate(['a','b','c'],100):
    print(i)


# all()
print(all([1,2,True,0]))   # 输出 False 全部为真才是真,只要有假就是假

# any()
print(any([1,'',0])) ,    # 输出 True 只要有真就是真


# zip()
names = ['zhangsan','lisi','wangwu']
ages = [25,18,30,40]

zipped = zip(names,ages)
print(list(zipped))

for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

"""
输出
[('zhangsan', 25), ('lisi', 18), ('wangwu', 30)]
zhangsan is 25 years old.
lisi is 18 years old.
wangwu is 30 years old.
** 可以看到最后多出来的一个age被丢弃了。这是因为 zip() 以“最短的可迭代对象”为准，自动截断，不会报错 **
"""


# filter()
def is_even(x):
    return x % 2 ==0
result = filter(is_even,[1,2,3,44,13,14])
print(result)  # 输出 <filter object at 0x1034d6980>
for i in result:
    print(i)   
"""
输出
2
44
14
""" 

numbers = [9,8,7,6,5,4,3,2,1]
print(list(filter(lambda x:x >5,numbers))) # 输出 [9, 8, 7, 6]


# map()
def square(x):
    return x**2

list1 = [1,2,3,4,5,6,7,8]
result = map(square,list1)
print(result)

for i in result:
    print(i)
"""
输出
1
4
9
16
25
36
49
64
"""

# 匿名函数
func2 = lambda n:n **n
print(func2(10)) # 输出 10000000000

## 匿名函数案例1 ：计算两数之和
add = lambda x,y:x+y
print(add(2,3))  # 输出 5

## 匿名函数案例2：计算1-7的平方
list = [1,2,3,4,5,6,7]

result = map(lambda x: x**2 ,list)
print(result)
for i in result:
    print(i)

"""
输出
1
4
9
16
25
36
49
"""


## 匿名函数案例3：筛选出偶数

result = filter(lambda x : x % 2 == 0,[1,2,3,4,5,6,7,8,9,10])
for i in result:
    print(i)

"""
输出
2
4
6
8
10
"""