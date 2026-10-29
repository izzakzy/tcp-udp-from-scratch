import socket

TARGET_HOST = "127.0.0.1"   # 127.0.0.1 = this same computer
TARGET_PORT = 9998          # must match the server's port


def main():
    # Create a TCP socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server (this performs the TCP handshake)
    client.connect((TARGET_HOST, TARGET_PORT))
    print(f"[*] Connected to {TARGET_HOST}:{TARGET_PORT}. Type 'quit' to exit.")

    try:
        while True:
            message = input("> ")
            if message.lower() == "quit":
                break

            client.send(message.encode("utf-8"))   # text -> bytes, then send

            response = client.recv(4096)           # wait for the server's reply
            print(f"[*] Server replied: {response.decode('utf-8', errors='replace')}")
    finally:
        client.close()   # always close the connection, even after an error


if __name__ == "__main__":
    main()