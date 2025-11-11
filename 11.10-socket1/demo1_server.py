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