from threading import RLock as Lock


mutexA = Lock()
mutexA.acquire()
mutexA.acquire()
print(123)
mutexA.release()
mutexA.release()


"""
输出
    123
"""