import socket



def tcp_client(server, http_methode, nachricht):
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client_socket.connect(("localhost" , 8880))

    try:
        payload = f"{http_methode} / HTTP/1.1\r\nHost: {server}\r\n\r\n{nachricht}"
        tcp_client_socket.sendall(payload.encode("utf-8"))  

        
        antwort = tcp_client_socket.recv(4096).decode('utf-8')  
        print(f"Nachricht vom Server: {antwort}")
    finally:
        tcp_client_socket.close()



def udp_client(server, http_methode, nachricht):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = f"{http_methode} / HTTP/1.1\r\nHost: {server}\r\n\r\n{nachricht}"

    try:
        udp_socket.sendto(payload.encode("utf-8"), ("localhost", 8891))

        daten, add = udp_socket.recvfrom(4096)
        antwort = daten.decode("utf-8")
        print (f"Antwort vom Server: {antwort}")
    except ConnectionRefusedError as e:
        print("Verbindung fehlgeschlagen! ", e)

    finally: 
        udp_socket.close()

if __name__ == "__main__":
    server = input("Bitte gebe den Server ein: ")
    http_methode = input("Bitte gebe die HTTP-Methode ein: ")
    nachricht = input("Bitte gebe die Nachricht ein: ")
    
    if not server:
        print("Fehler: Servertyp st erforderlich.")
    if not http_methode:
        print("Fehler: HTTP-Methode ist erforderlich.")
    if not nachricht:
        print("Fehler: Nachricht ist erforderlich.")


    if server == "TCP":
        tcp_client(server, http_methode, nachricht)
    elif server == "UDP":
        udp_client(server, http_methode, nachricht)
    else:
        print("Falscher Servertyp! ")
