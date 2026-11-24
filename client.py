import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1", 9000))
    while True:
        text = input("Ты: ")
        if not text:
            break
        s.sendall(text.encode())
        print("Сервер ответил:", s.recv(1024).decode())