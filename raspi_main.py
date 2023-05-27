import socket

HOST = '0.0.0.0'  # Raspberry Pi IP address
PORT = 5000  # Choose an available port

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)
print(f"Server listening on {HOST}:{PORT}")

# Accept a client connection
client_socket, client_address = server_socket.accept()
print(f"Client connected from {client_address}")

# Receive and print data from the client
while True:
    data = client_socket.recv(1024)
    if not data:
        continue
    print(f"Received data: {data.decode()}")

# Close the client and server sockets
client_socket.close()
server_socket.close()
