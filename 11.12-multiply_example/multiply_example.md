## 循环通信
> 服务器和客户端之间可以循环通信

### 服务端代码
```python
import socket
import struct

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",8080))
server.listen(5)
print("服务端已启动，等待连接")
conn = None

try:
    while True:
        conn,client_addr = server.accept()
        print(f"客户端{client_addr}已连接")
        while True:
            header = conn.recv(4)  # 接收头部
            data_size = struct.unpack("!I",header)[0]
            received_data = b""
            while len(received_data) < data_size:
                remaining = data_size - len(received_data)
                chunk = conn.recv(min(remaining,1024))
                if not chunk:
                    break
                received_data += chunk
            if (not received_data 
                or received_data.decode("utf-8").strip().upper()=="EXIT"
                ) : 
                print(f"客户端{client_addr}申请断开连接")
                break
            print(f"收到消息「{received_data.decode('utf-8')}」")
            response = received_data.decode("utf-8").upper()
            header = struct.pack("!I",len(received_data))
            conn.send(header+response.encode("utf-8"))
except ConnectionResetError:
    print("客户端异常断开")
except KeyboardInterrupt:
    print("服务端主动终止")
except Exception as e:
    print(f"未知异常：{e}")
finally:
    if conn:
        conn.close()
    server.close()


```

### 客户端代码
```python
import socket
import struct

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",8080))

try:
    while True:
        msg = input("请输入消息(输入exit退出)")
        if not msg.strip():
            print("消息不能为空，请重新输入消息")
            continue
        if msg.strip().upper()=="exit":
            break
        header = struct.pack("!I",len(msg.encode("utf-8"))) 
        client.send(header+msg.encode("utf-8")) 

        header = client.recv(4)
        data_size = struct.unpack("!I",header)[0]
        received_data = b""
        while len(received_data) < data_size:
            remaining = data_size -len(received_data) 
            chunk = client.recv(min(remaining,1024))
            if not chunk:
                break
            received_data += chunk
        print(f"服务端返回：{received_data.decode('utf-8')}")
except KeyboardInterrupt:
    print("客户端主动终止")
except BrokenPipeError:
    print("客户端已关闭连接，终止发送") 
except Exception as e:
    print(f"异常{e}")
finally:
    client.close()       
```

### 运行脚本验证

```bash
python3 circledemo_server.py
    服务端控制台输出 服务端已启动，等待连接
python3 circledemo_client.py
    服务端控制台输出 客户端('127.0.0.1',52028)已连接
    客户端控制台输出 请输入消息(输入exit退出)
客户端控制台输入 消息
    服务端控制台输出 收到消息「消息」
    客户端控制台输出 服务端返回：消息
客户端控制台输入 exit
    服务器端输出 客户端('127.0.0.1', 65432)申请断开连接
...但是服务器不会关闭会话，这里是代码逻辑问题...
```

## 执行远程命令
> 客户端发送指令给远程服务器，服务器接收到指令并将执行结果发给客户端
### 模拟简易SSH服务器

### 模拟SSH客户端