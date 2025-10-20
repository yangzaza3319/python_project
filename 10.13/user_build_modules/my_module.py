print("this is my own module...")

def greet(name):
    return f"hello,{name}!"
def add(a,b):
    return a+b
PI = 3.14159


"""
该自定义模块实现了4个基本的功能
1. 打印提示语，可以用于测试模块是否正常执行
2. 封装打招呼的功能
3. 封装两数相加的功能
4. 定义了PI的值

可以在另一个python文件中导入模块
"""