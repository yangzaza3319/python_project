import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost',9999))

client.send(b"hello from TCP client")
response = client.recv(1024)

print("server response:",response.decode('utf-8'))

client.close()