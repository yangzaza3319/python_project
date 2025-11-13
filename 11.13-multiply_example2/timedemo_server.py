import socket
import time
import struct

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_socket.bind(('',8080))

print("时间服务器已启动，等待客户端请求...")

try:
    while True:
        data,client_addr = server_socket.recvfrom(1024)
        print(f"收到来自{client_addr}的请求")

        current_time = int(time.time())
        packet_time = struct.pack("!I",current_time)

        server_socket.sendto(packet_time,client_addr)
except KeyboardInterrupt:
    print("\n服务端主动终止")
finally:
    server_socket.close()


"""
运行服务端脚本
    成功后会输出——>收到来自('127.0.0.1',59008)的请求
"""