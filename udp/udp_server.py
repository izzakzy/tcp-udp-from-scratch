import socket

IP = "0.0.0.0"
PORT = 9998


def main():
    # SOCK_DGRAM = UDP
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((IP, PORT))   # no listen() or accept() in UDP
    print(f"[*] Listening on {IP}:{PORT} (UDP)")

    while True:
        # recvfrom() gives us the data AND who sent it
        data, address = server.recvfrom(4096)
        print(f"[*] Received from {address[0]}:{address[1]}: "
              f"{data.decode('utf-8', errors='replace')}")

        # No connection exists, so we reply to the address we just received from
        server.sendto(b"ACK", address)


if __name__ == "__main__":
    main()