import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',8888))

try:
    partial_data = client.recv(4096)                 # 设置接收缓冲区为4kb，且仅接收一次
    print(f"实际接收长度:{len(partial_data)}字节")      
except ConnectionResetError:
    print("服务端已关闭连接")
finally:
    client.close()
