import socket

def udp_server():

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("localhost", 8888))

    while True:
            nachricht, client_adresse = udp_socket.recvfrom(4096)
            antwort = "Hier ist der UDP-Server!"
            udp_socket.sendto(antwort.encode('utf-8'), client_adresse) 

        
    udp_socket.close()

if __name__ == "__main__":
    udp_server()