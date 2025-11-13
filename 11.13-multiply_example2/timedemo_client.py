import socket
import struct
import time

client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_addr = ('127.0.0.1',8080)

try:
    client_socket.sendto(b'',server_addr)
    print("已发送时间请求，等待响应...")

    client_socket.settimeout(2)
    data,_ =client_socket.recvfrom(1024)

    if len(data) == 4:
        timestamp = struct.unpack("!I",data)[0]
        print(f"服务器时间:{time.ctime(timestamp)}")
    else:
        print("错误：收到无效时间数据")
except socket.timeout:
    print("请求超时，服务器端未响应")
except ConnectionRefusedError:
    print("连接被拒，请检查服务端是否运行")
except KeyboardInterrupt:
    print("\n客户端主动终止")
finally:
    client_socket.close()

"""
运行客户端侧脚本两种情况
    1. 请求超时，服务器端未响应——>可能是服务端脚本未启动
    2. 服务器时间：Thu Nov 13 09:40:13 2025
"""