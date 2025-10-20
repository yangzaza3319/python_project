# 命名空间的例子

def my_function():
    x = 10 
    print(x)

print(f"局部x的值是{x}")   # 局部命名空间中声明的x只作用于当前函数
x = 10 
my_function()
print("全局x的值是:",x)    # 全局命名空间中声明的x作用域包含声明之后的所有代码


# 作用域例子

def outer_function():
    outer_var = "我是外部变量"      # 在outer_function()函数内部定义的变量，局部作用域，仅在outer_function()函数内部可以使用

    def inner_function():
        inner_var = "我是内部变量"  # 在inner_function()函数内部定义的变量，局部作用域，仅在inner_function()函数内部可以使用
        print(inner_var)           
        print(outer_var)

    inner_function()
    # print(inner_var)   # 运行这行代码会报错：未定义“inner_var”,因为这个变量函数在外部不可见

outer_function()
# print(outer_var)         # 运行这行代码会报错：未定义“outer_var”，因为这个变量函数在外部不可见


# globals() 和 locals()方法
x = "全局1" 
y = "全局2" 
print(globals())
print(locals())

"""
输出
 {'__name__': 
 '__main__', '__doc__': None, '__package__':
   None, '__loader__':
 <class '_frozen_importlib.BuiltinImporter'>,
   '__spec__': None, '__annotations__':
   {}, '__builtins__': 
   <module 'builtins' (built-in)>, 'x': 
   '全局1', 'y': '全局2', 'func': <function func at 0x0000026701748A40>}
输出
{'__name__': 
'__main__', '__doc__': None, '__package__':
 None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, 
 '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'x':
   '全局1', 'y': '全局2', 'func': <function func at 0x0000026701748A40>}
"""

def func():
    a = "当前1" 
    b = "当前2" 
    print(globals())
    print(locals())

func()
"""
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'x': '全局1', 'y': '全局2', 'func': <function func at 0x0000026701ACF1A0>}
{'a': '当前1', 'b': '当前2'}
"""

# global 和 nonlocal 关键字
def modify_global():
    global x  # 声明 x 为全局变量
    x = 20    # 修改全局变量

modify_global()
print(x)  # 输出: 20

# 如果不使用 global，在函数内部直接赋值会创建一个新的局部变量，而不会影响全局变量
def try_modify():
    x = 30  # 创建一个局部变量 x，未声明为 global
    print(x)  # 输出: 30

try_modify()
print(x)  # 输出: 20，仍然是全局变量的值


## 
li = [1,2,3]
dic = {'name':'aaron'}

def change():
    li.append(4)
    dic['age'] = 18
    print(dic)
    print(li)

change()
print(dic)
print(li)

## 
def outer_function():
    x = 10  # 外层函数的局部变量

    def inner_function():
        nonlocal x  # 声明 x 为外层函数的局部变量
        x = 20      # 修改外层函数的变量

    inner_function()
    print(x)  # 输出: 20

outer_function()   
###  nonlocal 仅在嵌套函数中有效，不能用于声明全局变量。