import socket 
from concurrent.futures import ThreadPoolExecutor

def handle_client(conn, addr):
    print(f"Пoдключился {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
        print("Отключился:", addr)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("127.0.0.1", 9000))
server.listen(5)
print("Жду подключения на порту 9000 .....")

with ThreadPoolExecutor(max_workers=10) as pool:
    while True:
        conn, addr = server.accept()
        pool.submit(handle_client, conn, addr)