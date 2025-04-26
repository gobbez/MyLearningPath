import socket

target_host = "127.0.0.1"
target_port = 80

# Create UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    # Send data
    client.sendto(b"AAABBBCCC", (target_host, target_port))

    # Receive response
    data, addr = client.recvfrom(4096)

    print(data)
