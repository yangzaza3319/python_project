import socket
import multiprocessing

def handle_client(conn,addr):
    print(f"客户端已连接")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"接收来自{addr}的数据:{data.decode()}")
            conn.sendall(f"服务器响应:{data.decode().upper()}".encode())
    except ConnectionResetError:
        print(f"客户端{addr}异常断开")
    finally:
        conn.close()
if __name__=="__main__":
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind(("127.0.0.1",8888))
    server.listen(5)
    print("服务器已启动，等待连接...")

    try:
        while True:
            conn,addr= server.accept()
            process = multiprocessing.Process(
                target=handle_client,
                args=(conn,addr),
                daemon = True,
            )
            process.start()
            conn.close()
    except KeyboardInterrupt:
        print("\n服务器正在关闭...")
    finally:
        server.close()
        