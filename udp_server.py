import socket


udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind("localhost", 8891)

while True:
    nachricht, client_adresse = server_socket.recvfrom(4096)
    antwort = "Hier ist der UDP-Server! "



    udp_socket.sendto(antwort.encode('utf-8'), client_adresse) 

udp_socket.close()