import socket, threading

def server():
    s = socket.socket()
    try:
        s.bind(('localhost', 8080))
        s.listen(1)
        conn, _ = s.accept()
        try:
            conn.recv(1024)
        finally:
            conn.close()
            print("Server: connection closed properly")
    finally:
        s.close()
        print("Server: socket closed properly")

def client():
    c = socket.socket()
    try:
        c.connect(('localhost', 8080))
        c.sendall(b"Hello")
    finally:
        c.close()
        print("Client: socket closed properly")

threading.Thread(target=server).start()
client()
