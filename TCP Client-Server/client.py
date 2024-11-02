import socket

def client_program():
    host = "127.0.0.1"
    port = 8080
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Connected to the server...")

    while True:
        message = input("Enter the string: ")
        client_socket.send(message.encode())

        if message.lower() == "exit":
            print("Client Exit...")
            break

        response = client_socket.recv(1024).decode()
        print(f"From Server: {response}")

    client_socket.close()

if __name__ == '__main__':
    client_program()