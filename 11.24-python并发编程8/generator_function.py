"""
生成器函数
# generator_function.py
"""

def simple_coroutine():
    print("协程启动")
    x = yield
    print(f"接收值：{x}")

coro = simple_coroutine()
next(coro)
try:
    coro.send(10)
except StopIteration:
    print("协程正常结束")

"""
输出
    协程启动
    接收值：10
    协程正常结束
"""