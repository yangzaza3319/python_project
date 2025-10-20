
a=10
b="10"
print(a+b)
print(a == b)


"""
 PS D:\GitHubRoot> & D:/GitHubRoot/.venv/Scripts/python.exe d:/GitHubRoot/liujieyangLocal/python/8.21/强弱类型.py
Traceback (most recent call last):
  File "d:\GitHubRoot\liujieyangLocal\python\8.21\强弱类型.py", line 4, in <module>
    print(a+b)
          ~^~
TypeError: unsupported operand type(s) for +: 'int' and 'str'  # 不同类型的变量（int型变量a和string型变量）不能拼接
"""