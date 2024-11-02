import socket

def udp_server():
    host = "127.0.0.1"
    port = 8080
    buffer_size = 1024
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print("Server started...")

    while True:
        data, client_address = server_socket.recvfrom(buffer_size)
        message = data.decode()
        print(f"Client: {message}")
        
        if message.lower() == "exit":
            print("Server exiting...")
            break

        response = input("To client: ")
        server_socket.sendto(response.encode(), client_address)
    
    server_socket.close()

if __name__ == "__main__":
    udp_server()