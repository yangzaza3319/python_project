## socket 通信
> socket通信是网络编程的基础，它允许不同计算机或进程之间通过网络进行数据交换。在Python中，`socket`模块提供了对底层BSD socket接口的封装，支持TCP(可靠、面向连接)和UDP(快速、无连接)通信
> socket 是所有网络应用的基石（HTTP、FTP、SSH等高层协议都构建在socket上）
## Socket通信基本原理
> Socket 是”IP地址+端口号“的抽象
1. 需要服务器和客户端两个部分
2. 服务器监听某个端口，等待连接；客户端主动连接服务器的IP和端口
一旦TCP连接建立,双方可以通过socket发送/接收字节流

## python Socket模块核心API

```python
# 代码范例
import socket

socket socket.socket(family=AF_INET,type=SOCK_STREAM)  # 1. 创建socket对象

"""
常见参数
    family:
     - AF_INET  ——> IPv4
     - AF_INET6 ——> IPv6
    type:
     - SOCK_STREAM ——> TCP
     - SOCK_DGRAM  ——> UDP
"""
```
方法|说明
---|---
bind((host,port))|绑定本地地址(监听服务器本地)
listen(n)|开始监听(TCP服务器)
accept()|接受返回，返回(client_socket,addr)
connect((host,port))|连接远程服务器(客户端用)
send(data) / recv(bufsize)|TCP 发送/接收数据
sendto(data,addr) / recvfrom(bufsize)| UDP 发送/接收数据
close()| 关闭连接

## TCP Socket通信案例（可靠、有序）
### TCP服务器(Server)
```python
import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   # 创建socket对象，并且用IPv4和TCP进行通信
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)  # 允许端口重用

server.bind(('localhost',9999))   # 监听本地9999端口
server.listen(5)
print("TCP服务器监听`localhost:9999`")

try:
    while True:
        client,addr = server.accept()
        print(f"连接到{addr}")

        data = client.recv(1024)
        if data:
            print("Received:",data.decode('utf-8'))
            client.send(b"message received by server")

            client.close()
except KeyboardInterrupt:
    print("\n 服务器关机中")
finally:
    server.close()
```

### TCP客户端(client)
```python
import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost',9999))

client.send(b"hello from TCP client")
response = client.recv(1024)

print("server response:",response.decode('utf-8'))

client.close()
```
### 验证TCP数据传输的流程
```bash
python3 tcp_server.py
    控制台输出 TCP服务器监听`localhost:9999`
python3 tcp_client.py
    控制台输出 
            连接到('127.0.0.1', 50552)
            Received: hello from TCP client
    控制台输出
            server response: message received by server
^c 
    控制台输出 服务器关闭中
```

## UDP Socket通信(无连接、不可靠)案例
> UDP不保证到达、不保证顺序，但开销小，适合视频流以及游戏等场景
### UDP服务器
```python
import socket

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(('localhost',8888))
print("UDP服务器监听`localhost:8888`")
while True:
    data,addr = server.recvfrom(1024)
    print(f"received from {addr}:{data.decode()}")
    server.sendto(b"UDP ACK",addr)
    
```

### UDP 客户端
```python
import socket

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.sendto(b"hello UDP",('localhost',8888))
response,_ = client.recvfrom(1024)
print("server response:",response.decode())

client.close()
```

### 验证UDP数据传输的流程
```bash
python3 udp_server.py
    控制台输出 UDP服务器监听`localhost:8888`
python3 udp_clinet.py
    客户端控制台输出 server response: UDP ACK
    服务器控制台输出 received from ('127.0.0.1', 65193):hello UDP
```

## 注意事项

### 异常处理
```python
try:
    sock.connect(...)
except ConnectionRefusedError:
    print("server not running")
except socket.timeout:
    print("Timeout")
```

### 资源释放
> 使用`with`或确保`close()`被调用到
```python
with socket.socket() as s:
    s.connect(...)
    # 自动关闭
```

### 编码问题
> 网络传输的是bytes，字符串需要`.encode()`/`.decode()`

### TCP的粘包问题
> TCP是流协议，多次send可能会被合并吸收
>   解决方案：固定长度消息/添加分隔符(如`\n`)/使用长度头(先发出去的4字节表示长度)

### 扩平台的兼容问题
> windows不支持`SO_REUSEADDR`的某些问题
> IPv6需要显式指定`AF_INET6`

## 套接字家族
> 套接字有两种（或被称为两个种族），分别是基于文件型和基于网络型
### 基于文件类型的套接字家族——`AF_UNIX`
unix一切皆文件，基于文件的套接字调用的就是底层的文件系统来取数据，两个套接字进程运行在同一机器，可以通过访问同一个文件系统间接完成通信
### 基于网络类型的套接字家族——`AF_INET`
