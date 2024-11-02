import socket

def server_program():
    host = "127.0.0.1"
    port = 8080
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server started...")

    conn, addr = server_socket.accept()
    print(f"Connection from: {addr}")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"From client: {data}")

        if data.lower() == "exit":
            print("Server Exit...")
            break

        response = input("To client: ")
        conn.send(response.encode())

    conn.close()

if __name__ == '__main__':
    server_program()