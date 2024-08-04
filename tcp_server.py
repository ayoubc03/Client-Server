import socket
import http

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_socket.bind(("localhost", 8880))


while True:
    tcp_server_socket.listen()
    client_socket, add = tcp_server_socket.accept()

    daten = client_socket.recv(1024).decode("utf-8")

    
    

