import socket



def tcp_client(server, http_methode, nachricht):
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client_socket.connect((server_ip, server_port))

    try:
        payload = f"{http_methode} / HTTP/1.1\r\nHost: {server}\r\n\r\n{nachricht}"
        tcp_client_socket.sendall(payload)  

        
        antwort = tcp_client_socket.recv(4096).decode('utf-8')  
        print(f"Nachricht vom Server: {antwort}")
    finally:
        tcp_client_socket.close()

if not server_ip:
    print("Fehler: Server-IP-Adresse ist erforderlich.")
if not server_port_input:
    print("Fehler: Server-Portnummer ist erforderlich.")
if not http_method:
    print("Fehler: HTTP-Methode ist erforderlich.")
if not message:
    print("Fehler: Nachricht ist erforderlich.")

def udp_client ():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = f"{http_methode} / HTTP/1.1\r\nHost: {server}\r\n\r\n{nachricht}"

try:
    udp_socket.sendto(payload.encode("utf-8"), ("localhost", 8892))

    antwort = udp_socket.recvfrom(4096).decode("utf-8")
    print (f"Antwort vom Server: {antwort}")
except ConnectionRefusedError as e:
    print("Verbindung fehlgeschlagen! ", e)

finally: 
    udp_socket.close()

if __name__ == "__main__":
    server = input("Bitte gebe den Server ein: ")
    http_methode = input("Bitte gebe die HTTP-Methode ein: ")
    nachricht = input("Bitte gebe die Nachricht ein: ")
    if server == "TCP":
        client()
    elif server == "UDP":
        udp_client()
    else:
        print("Falscher Servertyp! ")
