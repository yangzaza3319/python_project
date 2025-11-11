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