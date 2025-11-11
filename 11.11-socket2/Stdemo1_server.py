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
    conn.send(header+data)
    data = b'world'
    header = struct.pack("!I",len(data))
    conn.send(header+data)
except KeyboardInterrupt:
    print("服务端主动终止")
finally:
    conn.close()
    server.close()
    