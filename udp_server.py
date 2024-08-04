import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_socket.bind("localhost", 8891)

while True:
    nachricht, _ = server_socket.recvfrom(4096)

    
