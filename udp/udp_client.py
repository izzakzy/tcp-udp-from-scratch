import socket

TARGET_HOST = "127.0.0.1"
TARGET_PORT = 9998


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.settimeout(3)   # UDP packets can get lost, so don't wait forever
    print(f"[*] Sending to {TARGET_HOST}:{TARGET_PORT} (UDP). Type 'quit' to exit.")

    try:
        while True:
            message = input("> ")
            if message.lower() == "quit":
                break

            # No connect() needed: put the destination in every send
            client.sendto(message.encode("utf-8"), (TARGET_HOST, TARGET_PORT))

            try:
                data, addr = client.recvfrom(4096)
                print(f"[*] Reply from {addr[0]}:{addr[1]}: "
                      f"{data.decode('utf-8', errors='replace')}")
            except socket.timeout:
                print("[!] No reply (packet lost, or no server listening)")
    finally:
        client.close()


if __name__ == "__main__":
    main()