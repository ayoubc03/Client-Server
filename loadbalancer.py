import socket 
import threading 


load_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
load_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
load_socket.bind(("localhost", 8892))
load_socket.listen(5)

def client_verwaltung(client_socket, addr):
    
    
    nachricht = client_socket.recv(1024).decode("utf-8")
    new_nach = nachricht.encode("utf-8")
    try:
        if "TCP" in nachricht:
           server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           server_socket.connect(("localhost" , 8880))
           server_socket.sendall(new_nach)

           antwort = server_socket.recv(4096).decode("utf-8")
           client_socket.sendall(antwort.encode("utf-8"))

        elif "UDP" in nachricht: 
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            server_socket.sendto(new_nach, ("localhost", 8888))  # Zu UDP Server senden

            antwort, addr = server_socket.recvfrom(4096) # Antwort vom Server
            client_socket.sendall(antwort) # Zum Client senden
            server_socket.close()
            
    finally:
        client_socket.close()

def main ():
    while True:
        client_socket, addr = load_socket.accept()
        client_handler = threading.Thread(target=client_verwaltung, args= (client_socket, addr))
        client_handler.start()
    

if __name__ == "__main__":
    main()
  
