import threading,time


def background_task():
    while True:
        print("守护线程运行中...")
        time.sleep(1)

daemon_thread = threading.Thread(target=background_task)
daemon_thread.daemon = True
daemon_thread.start()

time.sleep(5)
print("主线程结束，守护线程将被终止")
"""
输出
    守护线程运行中...
    守护线程运行中...
    守护线程运行中...
    守护线程运行中...
    守护线程运行中...
    主线程结束，守护线程将被终止
"""