# 函数的嵌套和作用域链
## 嵌套声明
def f1():
    print('in f1 ...')
    def f2():
        print('in f2 ...')
    f2()
f1()

## 嵌套调用
### 例子，找出四个数字中最大的数字
def max_num(x,y):
    if x > y :
        return x
    else :
        return y
def number(a,b,c,d):
    res1 = max_num(a,b)
    res2 = max_num(res1,c)
    res3 = max_num(res2,d)
    return res3

res = number(9,-1,12,2)
print(res)    # 输出12


## 作用域链
x = "这个x是全局变量"

def outer_function():
    x = "这个x是外层变量"
    
    def innner_function():
        x = "这个x是内层变量"
        print(x)      # 这个x是内层变量
    
    innner_function()
    print(x)          # 这个x是外层变量

outer_function()
print(x)              # 这个x是全局变量


## 函数名本质
### 函数名可以复制给变量
def greet():
    return "函数名赋值给变量"
greeting = greet       # 将greet函数名赋给greeting变量
print(greeting())      # 打印greeting()函数


### 函数名可以被当作容器类型的元素
def f1():
    print('f1元素')

def f2():
    print('f2元素')

def f3():
    print('f3元素')

l = [f1,f2,f3]
d = {'f1':f1,'f2':f2,'f3':f3}
l[0]()    # 输出 f1元素
d['f2']   # 输出 <function f2 at 0x0000026376B5F6A0>


# 函数名可以当作函数的参数和返回值
def f1():
    print("当前在f1函数中")
def func(argv):
    argv()
    return argv

f = func(f1)  # f1函数名当作参数
f()      