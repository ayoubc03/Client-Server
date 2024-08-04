import socket 
import threading 


load_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
load_socket.bind("localhost", 8892)

while True:
    load_socket.listen(5)
    client_socket, _ = load_socket.accept()

    nachricht = client_socket.recv(1024).decode("utf-8")
    new_nach = nachricht.encode("utf-8")

    if "TCP" in nachricht:
        load_socket.connect(8880)
        load_socket.sendall(new_nach)

    if "UDP" in nachricht: 
        load_socket.connect(8891)
        load_socket.sendall(new_nach)
