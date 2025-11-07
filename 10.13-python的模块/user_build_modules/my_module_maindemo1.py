import my_module

print(my_module.PI)
print(my_module.greet("小问号"))
print(my_module.add(3,6))

"""
输出
this is my own module...
3.14159
hello,小问号!
9
"""


import my_module as mm  # 自定义模块起别名
print(mm.greet("小问号"))  # 输出 hello,小问号!