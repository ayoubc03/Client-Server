import socket



def client(server, http_methode, nachricht):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost" , 8892))

    try:
        payload = f"{http_methode} / HTTP/1.1\r\nHost: {server}\r\n\r\n{nachricht}"
        client_socket.sendall(payload.encode("utf-8"))  

        
        antwort = client_socket.recv(4096).decode('utf-8')  
        print(f"Nachricht vom Server: {antwort}")
    finally:
        client_socket.close()




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


    client(server, http_methode, nachricht)