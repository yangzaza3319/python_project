import socket

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(('localhost',8888))
print("UDP服务器监听`localhost:8888`")
while True:
    data,addr = server.recvfrom(1024)
    print(f"received from {addr}:{data.decode()}")
    server.sendto(b"UDP ACK",addr)
    