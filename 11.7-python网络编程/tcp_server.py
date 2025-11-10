import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

server.bind(('localhost',9999))
server.listen(5)
print("TCP服务器监听`localhost:9999`")

try:
    while True:
        client,addr = server.accept()
        print(f"连接到{addr}")

        data = client.recv(1024)
        if data:
            print("Received:",data.decode('utf-8'))
            client.send(b"message received by server")

            client.close()
except KeyboardInterrupt:
    print("\n 服务器关闭中")
finally:
    server.close()