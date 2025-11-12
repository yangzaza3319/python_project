import socket
import struct

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",8080))
server.listen(5)
print("服务端已启动，等待连接")
conn = None

try:
    while True:
        conn,client_addr = server.accept()
        print(f"客户端{client_addr}已连接")
        while True:
            header = conn.recv(4)  # 接收头部
            data_size = struct.unpack("!I",header)[0]
            received_data = b""
            while len(received_data) < data_size:
                remaining = data_size - len(received_data)
                chunk = conn.recv(min(remaining,1024))
                if not chunk:
                    break
                received_data += chunk
            if (not received_data 
                or received_data.decode("utf-8").strip().upper()=="EXIT"
                ) : 
                print(f"客户端{client_addr}申请断开连接")
                break
            print(f"收到消息「{received_data.decode('utf-8')}」")
            response = received_data.decode("utf-8").upper()
            header = struct.pack("!I",len(received_data))
            conn.send(header+response.encode("utf-8"))
except ConnectionResetError:
    print("客户端异常断开")
except KeyboardInterrupt:
    print("服务端主动终止")
except Exception as e:
    print(f"未知异常：{e}")
finally:
    if conn:
        conn.close()
    server.close()

