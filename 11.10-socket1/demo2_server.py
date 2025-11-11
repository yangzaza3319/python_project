import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('0.0.0.0',8888))
server.listen(5)

print("服务端已启动，等待客户端连接")
conn,addr = server.accept()

try:
    # 发送10kb数据(超过常规数据接收区大小)
    big_data = b'a' * 1024 * 10 
    conn.sendall(big_data)
    print(f"已发送{len(big_data)}字节数据")
except KeyboardInterrupt:
    print("服务端主动终止")
finally:
    conn.close()
    server.close()
