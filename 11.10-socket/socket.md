## 套接字的相关方法
### 服务端套接字函数
函数|含义
---|---
`s.bind()`|绑定(主机，端口号)到套接字
`s.listen()`|开始TCP监听
`s.accept()`|被动接收TCP客户端的连接，阻塞式等待连接的到来

### 客户端套接字函数
函数|含义
---|---
`s.connect()`|主动初始化TCP服务器连接
`s.connect_ex()`|connect()函数的拓展版本，出错时返回出错码，而不是抛出异常

### 公共用途套接字函数
函数|含义
---|---
`s.recv()`|接收TCP数据
`s.send()`|发送TCP数据（send在待发送数据量大于缓存区剩余空间时，数据只会发送部分（其余丢失），不会发完）
`s.sendall()`|发送完整的TCP数据(本质就是循环调用send，sendall在待发送数据量大于缓存区剩余空间时，数据不丢失，循环调用send直至发完)
`s.recvfrom()`|接收UDP数据
`s.sendto()`|发送UDP数据
`s.getpeername()`|连接到当前套接字的远端的地址
`s.getsockname()`|当前套接字的地址
`s.getsockopt()`|返回指定套接字的参数
`s.setsockopt()`|设置指定套接字的参数
`s.close()`|关闭套接字

### 面向锁的套接字方法
函数|含义
---|---
`s.setblocking()`|设置套接字的阻塞和非阻塞模式
`s.settimeout()`|设置套接字操作的超时时间
`s.gettimeout()`|获取阻塞套接字操作的超时时间


### 面向文件的套接字函数
函数|含义
---|---
`s.fileno()`|套接字的文件描述符
`s.makefile()`|创建一个与套接字相关的文件


## 粘包问题
> 粘包问题产生的原因
>   1. TCP协议的特性：
>       - 流式传输：TCP将数据视为连续字节流，不会自动分割数据包，导致接收端无法区分消息边界
>       - 缓冲区机制：发送端和接收端均存在缓冲区，发送端可能将多个小数据包合并发送，接收端可能将多次接收的数据合并
>       - Nagle算法优化:TCP为了提高传输效率，会合并多个小数据包（例如间隔短且数据量小）后发送
>   2. 代码逻辑缺陷
>       - 连续发送：在未明确分隔消息的情况下连续调用`send()`。导致数据在缓冲区中合并
>       - 接收不完整：接收端`recv()`方法未动态调整缓冲区大小，导致部分数据残留

### 案例1——通过 连续发送小数据包 和 接收缓冲区合并 的场景（即接收方一次性读取到“粘在一起”的数据）模拟粘包现象
```python
# demo1_server.py
import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('0.0.0.0',8888))
server.listen(5)
print("服务端已启动，等待客户端连接...")

conn,addr = server.accept()
print(f"客户端{addr}已经连接")

try:
    # 连续发送两次数据(没有处理粘包)
    conn.send(b'hello') # 第一次发送
    conn.send(b'world') # 第二次发送（可能合并到缓冲区）
except KeyboardInterrupt:
    print("服务端主动终止")
finally:
    conn.close()
    server.close()
```

```python
# demo1_client.py
import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',8888))

try:
    data = client.recv(1024)
    print(f"接收到的数据：{data.decode()}")
except ConnectionAbortedError:
    print("服务端断开连接")
finally:
    client.close()
```

```bash
python3 demo1_server.py
    # 服务器控制台输出——服务端已启动，等待客户端连接...
python3 demo1_client.py
    # 服务端控制台输出——客户端('127.0.0.1', 59587)已经连接
    # 客户端控制台输出——接收到的数据：helloworld
```
"""
输出 
服务端调用了两次 send()（分别发送 'hello' 和 'world'），但客户端只调用了一次 recv(1024)，结果却收到了合并后的 'helloworld'
"""