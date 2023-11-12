import socket
import time

def main():
    server_ip = "adres_serwera"
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    while True:
        data = "Hello, server!"
        client_socket.send(data.encode())
        
        response = client_socket.recv(1024)
        print(f"Otrzymano odpowiedź od serwera: {response.decode()}")

        time.sleep(2)  # Odczekanie przed wysłaniem kolejnej wiadomości


if __name__ == "__main__":
    main()

