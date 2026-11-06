import socket

server = socket.socket()
server.bind(('localhost', 8080))
server.listen(1)
print("Server listening on port 8080...")
conn, addr = server.accept()
data = conn.recv(1024).decode()
print("Received:", data)
conn.sendall(b"Message received")
conn.close()
server.close()
