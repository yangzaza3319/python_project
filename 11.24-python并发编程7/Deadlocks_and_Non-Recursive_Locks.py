"""
死锁和不可重入锁案例
Deadlocks_and_Non-Recursive_Locks.py
"""
from threading import Lock
import time

mutexA = Lock()
mutexA.acquire()
mutexA.acquire()
print(123)
mutexA.release()
mutexA.release()