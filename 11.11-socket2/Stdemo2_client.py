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
    