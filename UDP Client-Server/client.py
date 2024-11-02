import socket

def udp_client():
    host = "127.0.0.1"
    port = 8080
    buffer_size = 1024
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        message = input("Enter message to server: ")
        client_socket.sendto(message.encode(), (host, port))

        if message.lower() == "exit":
            print("Client exiting...")
            break

        data, _ = client_socket.recvfrom(buffer_size)
        print(f"Server: {data.decode()}")
    
    client_socket.close()

if __name__ == "__main__":
    udp_client()