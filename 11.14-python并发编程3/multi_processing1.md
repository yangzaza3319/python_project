## python的多进程编程1
> 使用multiprocess包来实现多进程编程
> multiprocess包提供的子模块非常多，大致可以分为四个部分：创建进程部分、进程同步部分、线程池部分、进程之间数据共享

### 进程创建
process模块是一个创建进程的模块，借助这个模块，就可以完成进程的创建

#### 直接创建
> Process类+target函数

```python
from multiprocessing import Process
p = Process(target=func,args=(arg1,))
p.start()
```

#### 继承类创建
> 自定义Process子类，重写`run()`方法

```python
from multiprocessing import Process
class MyProcess(Process):
    def run(self):
        print("hello world!")
```

#### 示例代码

```python
"""
直接创建父进程和子进程
"""
from multiprocessing import Process

def func(name):
    print("hello %s" % name)
    print("子进程结束")
if __name__ == '__main__':
    p = Process(target=func,args=('niuniu',))   # 实例化对象：子进程p 传递函数名和函数的实参
    p.start()                                   # 启动子进程
    print("主进程结束")

"""
运行输出
    主进程结束
    hello niuniu
    子进程结束
"""
```

```python
"""
通过继承类创建子进程
"""
import os
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self,name):
        super().__init__()
        self.name = name
    
    def run(self):
        print(os.getpid())
        print('%s正在和女主播聊天'%self.name)

if __name__ == '__main__':
    p1 = MyProcess('张三')
    p1.start()               # 继承Process类内部的start()方法，他会在新进程运行时自动调用重写的`run()`方法
    print('主进程结束')
"""
运行输出 
    主进程结束
    44482
    张三正在和女主播聊天
"""
```
#### 方法介绍

方法|含义
---|---
`p.start()`|启动进程，并调用该子进程中的`p.run()`
`p.run()`|进程启动时运行的方法，作用是调用target指定的函数，我们自定类的类中一定要实现该方法
`p.terminate()`|强制终止进程p，不会进行任何处理操作，如果p创建了子进程，该子进程就成了僵尸进程，使用该方法需要特别小心这种情况，如果p还保存了一个锁那么也将不会被释放，进而导致死锁
`p.is_alive()`|如果进程p在运行，则返回True
`p.join([timeout])`|join()让主进程暂停，直到子进程p真正终止，timeout是可选的超时时间。join() 只对通过 start() 启动的、真正的子进程有效；如果你直接调用 run()，并没有创建新进程，因此 join() 要么无效，要么报错
`p.daemon()`|默认值为False，如果设置成True，代表p为后台运行的守护进程，当p的父进程终止时，p也随之停止，且设置为True后，p不能创建自己的新进程，必须在p.start()之前设置
`p.name()`|进程的名称
`p.pid()`|进程的pid
`p.exitcode()`|进程在运行时为None,如果为-N，表示被信号N结束
`p.authkey()`|进程的身份验证键，默认是由os.urandom()随机生成的32位字符的字符串。这个键的用途是为涉及网络连接的底层进程间通信提供安全性，这类连接只有在具有相同的神锋验证键时才能成功

> 在Windows操作系统中，由于没有fork( Linux操作系统中创建进程的机制)，在创建子进程的时候会自动import启动它的这个文件。而在import的时候又执行了整个文件。因此如果将`process()`直接写在文件中，则会产生无限递归，导致创建子进程报错。所以必须把子进程创建的部分用`if __name__ == '__main__'`判断保护起来，import的时候，就不会递归运行了

##### join 方法案例
> 正常情况下，是主进程先执行结束，然后等待子进程执行结束后，整个程序退出。如果在start了以后使用join，那么将会阻塞(也可以理解为同步)主进程，等子进程结束以后，主进程才能继续执行

```python
from multiprocessing import Process

def func(name):
    print("hello %s" %name)
    print("子进程运行完成，输出了name变量的内容")

if __name__ == '__main__':
    p =Process(target=func,args=('niuniu',))
    p.start()
    p.join()    # 阻塞等待完成
    print("主程序执行完毕，程序退出")

"""
输出 
    hello niuniu
    子进程运行完成，输出了name变量的内容
    主程序执行完毕，程序退出
"""
```

##### 查看进程号
> 通过os模块中提供的getpid的方法来获取当前进程的进程号

```python
import os
from multiprocessing import Process

def func():
    print('子进程id:',os.getpid(),'父进程id:',os.getppid())
    print("子进程结束")

if __name__=="__main__":
    p = Process(target=func,args=())
    p.start()
    print("主进程id:",os.getpid())
    print("主进程结束，等待子进程结束中...")
"""
输出
    主进程id: 48464
    主进程结束，等待子进程结束中...
    子进程id: 48466 父进程id: 48464
    子进程结束
此时子进程中查看它的父进程id号，等于我们在主进程中查看到的id号，说明子进程确实是由我们的主进程创建的
"""
```

##### 多进程实例

1. 多个进程同时运行
```python
# 多个进程同时运行(子进程的执行顺序不是根据启动顺序决定的)
# multiprocessing_demo1.py
from multiprocessing import Process
import time

def func(name):
    print("hello %s" %name)
    time.sleep(1)
    print("子进程结束")
if __name__ == "__main__":
    for i in range(5):
        p = Process(target=func,args=('niuniu',))
        p.start()
    print("主进程结束，等待子进程...")
```

2. 使用join()方法
```python
# multiprocessing_demo2.py
"""
使用了join方法后，子进程变成了顺序执行，每个子进程结束以后，下一个子进程才能开始。同一时刻，只能由一个子进程执行，变成了一种阻塞的方式
"""
from multiprocessing import Process
import time

def func(name):
    print("hello %s" %name)
    time.sleep(1)
    print("子进程结束")

if __name__ == "__main__":
    for i in range(5):
        p = Process(target=func,args=('niuniu',))
        p.start()
        p.join()
    print("所有子进程已完成，主进程结束")
"""
输出 
    hello niuniu
    子进程结束
    hello niuniu
    子进程结束
    hello niuniu
    子进程结束
    hello niuniu
    子进程结束
    hello niuniu
    子进程结束
    所有子进程已完成，主进程结束
"""
```
3. 综合案例

```python
import multiprocessing
import time

def worker(num):
    print(f"进程{num}开始工作")
    time.sleep(2)
    print(f"进程{num}工作结束")
if __name__=='__main__':
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=worker,args=(i,))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()

    print("所有进程完成，主进程退出...")


"""
输出 
    进程0开始工作
    进程2开始工作
    进程1开始工作
    进程1工作结束
    进程2工作结束
    进程0工作结束
    所有进程完成，主进程退出...
"""
```

##### 守护进程
> 随着主进程的结束而结束，主进程创建守护进程，进程之间是互相独立的，主进程代码运行结束，守护进程随即终止
> 1. 守护进程会在主进程代码执行结束后就终止
> 2. 守护进程内无法再开启子进程，否则抛出异常

```python
# deamon.py

from multiprocessing import Process
import time

def worker():
    print("守护进程正在工作...")
    n = 0
    while True:
        print(f"  工作循环 {n}")
        n += 1
        time.sleep(0.5)

if __name__ == '__main__':
    p = Process(target=worker)
    p.daemon = True
    p.start()
    
    print("主进程睡眠 2 秒...")
    time.sleep(2)
    print("主进程结束！")  # 此时守护进程会被强制终止

"""
输出 
    主进程睡眠 2 秒...
    守护进程正在工作...
    工作循环 0
    工作循环 1
    工作循环 2
    工作循环 3
    主进程结束！
"""
```

##### socket聊天并发实例
1. 服务端
```python
# socketchat_server.py
import socket
import multiprocessing

def handle_client(conn,addr):
    print(f"客户端已连接")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"接收来自{addr}的数据:{data.decode()}")
            conn.sendall(f"服务器响应:{data.decode().upper()}".encode())
    except ConnectionResetError:
        print(f"客户端{addr}异常断开")
    finally:
        conn.close()
if __name__=="__main__":
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind(("127.0.0.1",8888))
    server.listen(5)
    print("服务器已启动，等待连接...")

    try:
        while True:
            conn,addr= server.accept()
            process = multiprocessing.Process(
                target=handle_client,
                args=(conn,addr),
                daemon = True,
            )
            process.start()
            conn.close()
    except KeyboardInterrupt:
        print("\n服务器正在关闭...")
    finally:
        server.close()
        
```

2. 客户端
```python
# socketchat_client.py
import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",8888))

while True:
    msg = input(">>:").strip()
    if not msg:
        continue

    client.send(msg.encode("utf-8"))
    msg = client.recv(1024)
    print(msg.decode("utf-8"))
```

3. 案例调试

```bash
客户端控制台输入
    1234
服务器控制台输出
    接收来自('127.0.0.1', 60259)的数据:1234
客户端控制台输出
    服务器响应：1234
```

