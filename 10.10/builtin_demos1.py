# 作用域相关函数（locals和grobals）案例

a = 1
b = 2
print(locals())
print(globals())

def func(argv):
    c = 2
    print(locals())
    print(globals())
func(10)

"""
输出
print(locals())
    {'__name__':、、、一些乱七八糟的系统内置函数、、、 ''a': 1, 'b': 2, 'func': <function func at 0x102ff0ea0>}
print(locals())
    {'__name__':、、、一些乱七八糟的系统内置函数、、、 ''a': 1, 'b': 2, 'func': <function func at 0x102ff0ea0>}
func(10)
   {'__name__':、、、一些乱七八糟的系统内置函数、、、 'a': 1, 'b': 2, 'func': <function func at 0x102ff1080>}
"""

# eval()
result = eval('2 + 3')
print(result) # 输出5

n = -2
result = eval('n + 3')
print(result) # 输出1

eval('print("hello world")')
# 输出 hello world

# exec()

str = '''
for i in range(5):
    print(i)
'''
exec(str)
"""
输出
0
1
2
3
4
"""

# compile()
 ## 流程语句使用exec
code1 = 'for i in range(5):print(i)'
compile1 = compile(code1,'','exec')
exec(compile1)  
"""
输出
0
1
2
3
4
"""
## 简单求值表达式用eval
code2 = '1+2+3'
compile2 = compile(code2,'','eval')
eval(compile2) # 输出6

## 交互语句用single

code3 = 'name = input("please input your name: ")'
compiles3 = compile(code3,'','single')

exec(compiles3)
print(name)
"""
输出
please input your name: Alice
Alice
"""