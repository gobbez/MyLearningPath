import socket

target_host = "www.google.com"
target_port = 80

# Create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to client
client.connect((target_host, target_port))

# Send some data
client.sendall(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# Receive some data
response = client.recv(4096)

print(response)