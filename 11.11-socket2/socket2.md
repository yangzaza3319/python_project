## 粘包的解决方案
> 固定包头法：发送端在数据前附加一个固定长度的包头，标明数据长度，接收端根据包头解析完整数据

### struct 模块
> 把一个类型，如数字转成固定长度的bytes；将收到的bytes解包回原始数据
> 核心用途——>实现跨平台、二进制协议通信(如自定义网络协议、解析二进制文件)

#### struct模块常用格式码对照表格

格式|   C类型   |   Python类型  |   大小(字节)  |   说明       |    示例
---|    ---    |   ---        |   ---       |   ---        |    ---
`x`|  pad byte |    无值       |    1        |填充字节（占位）| `struct.pack('!xx',1)`——>b'\x00\x00'
`c`|    char    |长度为1的字符串 |     1      |单个字符（bytes）|`struct.pack('!c',b'A')`——>b'A'
`b`|signed char|整数|1|有符号的8位整数(-128~127)|`struct.pack('!b',-1)`——>b'\xff'
`B`|unsigend char|整数|1|无符号的8位整数（0～255）|`struct.pack('!B',255)`——>b'\xff'
`?`|_Bool|bool|1|布尔值|`struct.pack('!?',True)`——> b'\x01'
`h`|short|整数|2|有符号16位整数|`struct.pack('!h',123)`——> b'\x00\x7b' 
`H`|unsigned short|整数|2|无符号的16位整数|`struct.pack('!H',123)`——> b'\x00\x7b' 
`i`|int|整数|4|有符号32位整数|`struct.pack('!i',12345)`——> b'\x00\x00\x30\x39'
`I`|unsigned int|整数|4|无符号32位整数|`struct.pack('!I',12345)`——>b'\x00\x00\x30\x39'
`l`|long|整数|4|有符号的32位整数(同i)|同上
`L`|unsigned long|整数|4|无符号的32位整数(同I)|同上
`q`|long long|整数|8|有符号64位整数|`struct.pack('!q',123456789012345)`
`Q`|unsigned long long|整数|8|无符号64位整数|同上
`f`|float|float|4|单精度浮点数(IEEE 754)|`struct.pack('!f',3.14)`
`d`|double|float|8|双精度浮点数(IEEE 754)|`struct.pack('!d',3.1415926)`
`s`|char[]|string|可变|需指定固定长度的字符串|`struct.pack('!10s',b'hello')`——>b'hello\x00'
`p`|char[]|string|可变|null终止字符串(自动计算长度)|`struct.pack('!p',b'hello')`——>b'hello\x00'
`P`|void*|整数|平台相关|指针(通常不用)|不推荐使用

### struct模块常见用法
```python
import struct

# 将一个数字转换成等长度的bytes类型
ret = struct.pack('i',188334)
print(ret,len(ret))

ret1 = struct.unpack('i',ret)[0] # 通过unpack反解回来，返回一个元组
print(ret1)
```

###  利用struct模块解决粘包问题可运行的demo1

1. 服务端代码
```python
import socket
import struct

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('0.0.0.0',8888))
server.listen(5)

print("服务端已启动，等待客户端连接...")

conn,addr = server.accept()
print(f"客户端{addr}已连接")


try:
    data = b'hello'
    header = struct.pack("!I",len(data))
    conn.send(header+data) # 第一次发送数据
    data = b'world'
    header = struct.pack("!I",len(data))
    conn.send(header+data) # 第二次发送数据
except KeyboardInterrupt:
    print("服务端主动终止")
finally:
    conn.close()
    server.close()
    
```
2. 客户端代码
```python
import socket
import struct

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',8888))


try:
    header = client.recv(4)
    data_size = struct.unpack("!I",header)[0]
    received_data = client.recv(data_size)
    print(f"实际接收长度:{len(received_data)}字节")
    print(received_data)
except ConnectionResetError:
    print("服务端已关闭连接")
finally:
    client.close()
```

#### 验证
```bash
python3 Stdemo1_server.py
    服务端控制台输出 服务端已启动，等待客户端连接
python3 Stdemo1_client.py
    服务端控制台输出 客户端('127.0.0.1',65340)已连接
    客户端控制台输出 实际接收长度:5字节
                  b'hello'
```

###  利用struct模块解决粘包问题可运行的demo2
#### 服务端代码(发送10kb大数据包)
```python
import socket
import struct

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('0.0.0.0',8888))
server.listen(5)

print("服务端已启动，等待客户端连接")
conn,addr = server.accept()

try:
    big_data = b'A' * 1024 * 10 # 发送10kb数据
    header = struct.pack("!I",len(big_data)) # 发送固定长度包头
    conn.sendall(header + big_data)
    print(f"已发送{len(big_data)} 字节数据")
except KeyboardInterrupt:
    print("服务端主动终止")
finally:
    conn.close()
    server.close()
```

```python
import socket
import struct

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',8888))

try:
    header = client.recv(4)
    data_size = struct.unpack("!I",header)[0]
    received_data = b""
    while len(received_data) < data_size:
        remaining = data_size - len(received_data)
        chunk = client.recv(min(remaining,1024))
        if not chunk:
            break
        received_data += chunk
    print(f"实际接收长度：{len(received_data)}字节")

except ConnectionResetError:
    print("服务器端关闭连接")
finally:
    client.close()
```

### 运行结果
```bash
服务端控制台输出 
    服务端已启动，等待客户端连接
    已发送10240 字节数据
客户端控制台输出
    实际接收长度：10240字节
```