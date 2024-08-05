import socket 
import threading 


load_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
load_socket.bind(("localhost", 8892))

while True:
    load_socket.listen(5)
    client_socket, _ = load_socket.accept()

    nachricht = client_socket.recv(1024).decode("utf-8")
    new_nach = nachricht.encode("utf-8")
    try:
        if "TCP" in nachricht:
           server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           server_socket.connect(("localhost" , 8880))
           server_socket.sendall(new_nach)

        if "UDP" in nachricht: 
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            server_socket.sendto(new_nach, ("localhost" , 8891))
            
    finally:
        server_socket.close()



