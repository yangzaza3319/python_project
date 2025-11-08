## socket 通信
> socket通信是网络编程的基础，它允许不同计算机或进程之间通过网络进行数据交换。在Python中，`socket`模块提供了对底层BSD socket接口的封装，支持TCP(可靠、面向连接)和UDP(快速、无连接)通信

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
