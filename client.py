import socket


def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    server = input("Bitte gebe den Server ein: ")
    http_methode = input("Bitte gebe die HTTP-Methode ein : ")
    nachricht = input("Bitte gebe die Nachricht ein: ")

    try:
        payload = f"{http_methode} / HTTP/1.1\r\nHost: {server_ip}\r\n\r\n{message}"
        client_socket.sendall(payload)  

        
        antwort = client_socket.recv(4096).decode('utf-8')  
        print(f"Nachricht vom Server: {antwort}")
    finally:
        client_socket.close()



if not server_ip:
    print("Fehler: Server-IP-Adresse ist erforderlich.")
if not server_port_input:
    print("Fehler: Server-Portnummer ist erforderlich.")
if not http_method:
    print("Fehler: HTTP-Methode ist erforderlich.")
if not message:
    print("Fehler: Nachricht ist erforderlich.")

