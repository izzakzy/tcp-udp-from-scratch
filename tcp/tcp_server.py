import socket
import threading

IP = "0.0.0.0"   # listen on all network interfaces of this computer
PORT = 9998      # the "door number" clients will connect to


def main():
    # Create a TCP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Lets you restart the server immediately without "Address already in use"
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Attach the socket to our IP and port
    server.bind((IP, PORT))

    # Start listening; up to 5 clients can wait in line
    server.listen(5)
    print(f"[*] Listening on {IP}:{PORT}")

    while True:
        # accept() waits here until a client connects.
        # It returns a NEW socket just for that client, plus the client's address.
        client_socket, address = server.accept()
        print(f"[*] Accepted connection from {address[0]}:{address[1]}")

        # Handle each client in its own thread so many can connect at once
        t = threading.Thread(
            target=handle_client, args=(client_socket, address), daemon=True
        )
        t.start()


def handle_client(client_socket, address):
    # "with" closes the socket automatically when we leave the block
    with client_socket as sock:
        while True:
            data = sock.recv(1024)   # wait for up to 1024 bytes
            if not data:             # empty bytes means the client disconnected
                print(f"[*] {address[0]}:{address[1]} disconnected")
                break

            message = data.decode("utf-8", errors="replace")  # bytes -> text
            print(f"[*] Received from {address[0]}:{address[1]}: {message}")

            sock.send(b"ACK: " + data)   # reply (must be bytes)


if __name__ == "__main__":
    main()