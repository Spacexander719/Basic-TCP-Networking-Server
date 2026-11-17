import socket
import threading

from server.client_handler import handle_client

from shared.config import (
    SERVER_HOST,
    SERVER_PORT
)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((SERVER_HOST, SERVER_PORT))

server.listen()

print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}")

while True:

    client_socket, address = server.accept()

    thread = threading.Thread(
        target=handle_client,
        args=(client_socket, address)
    )

    thread.start()

    print(f"Active connections: {threading.active_count()-1}")