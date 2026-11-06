import socket

client = socket.socket()
client.connect(('localhost', 8080))
msg = input("Enter message: ")
client.sendall(msg.encode())
print("Server response:", client.recv(1024).decode())
client.close()
