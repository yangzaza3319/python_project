import socket

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.sendto(b"hello UDP",('localhost',8888))
response,_ = client.recvfrom(1024)
print("server response:",response.decode())

client.close()