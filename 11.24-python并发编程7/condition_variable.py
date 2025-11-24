import threading

queue = []
condition = threading.Condition()

def producer():
    with condition:
        queue.append("小问号菜馆A套餐")
        condition.notify()

def consumer():
    with condition:
        while not queue:
            condition.wait()
        data = queue.pop()
        print(f"消费数据: {data}")

threading.Thread(target=producer).start()
threading.Thread(target=consumer).start()

"""
输出
    消费数据: 小问号菜馆A套餐
"""