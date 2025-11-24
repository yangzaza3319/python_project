import threading

semaphore = threading.Semaphore(2)

def task():
    with semaphore:
        print(f"{threading.current_thread().name}正在工作")
        threading.Event().wait(3)

threads = [threading.Thread(target=task) for _ in range(10)]
for i in threads:
    i.start()
for i in threads:
    i.join()
"""
输出
    Thread-1 (task)正在工作
    Thread-2 (task)正在工作
    Thread-3 (task)正在工作
    Thread-4 (task)正在工作
    Thread-5 (task)正在工作
    Thread-6 (task)正在工作
    Thread-7 (task)正在工作
    Thread-8 (task)正在工作
    Thread-9 (task)正在工作
    Thread-10 (task)正在工作
"""