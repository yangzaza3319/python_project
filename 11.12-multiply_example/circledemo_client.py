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
            remaining = data_size - len(received_data) 
            chunk = client.recv(min(remaining,1024))
            if not chunk:break
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