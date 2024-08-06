import socket
import http

def tcp_server():
    try:
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server_socket.bind(("localhost", 8880))
        tcp_server_socket.listen()

        while True:
            try:
                client_socket, add = tcp_server_socket.accept()

                daten = client_socket.recv(1024).decode("utf-8")

                antwort = "Hier ist der TCP-Server"

                client_socket.sendall(antwort.encode("utf-8"))    
            finally:
                client_socket.close()
    finally:
        tcp_server_socket.close()

if __name__ == "__main__":
    tcp_server()
