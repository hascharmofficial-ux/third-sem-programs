import socket

client = socket.socket()
client.connect(('localhost', 8080))
print("Connected to server at localhost:8080")
client.sendall(b"Hello Server!")
client.close()
