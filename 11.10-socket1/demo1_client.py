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