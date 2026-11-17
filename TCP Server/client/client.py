import socket
import threading

print("""
Available Commands:

/join networking
/join gaming
/join security
/groups
/help
""")

from shared.config import (
    SERVER_HOST,
    SERVER_PORT,
    BUFFER_SIZE
)

COLORS = [
    "\033[91m",   # red
    "\033[92m",   # green
    "\033[93m",   # yellow
    "\033[94m",   # blue
    "\033[95m",   # magenta
    "\033[96m"    # cyan
]

RESET = "\033[0m"


def receive_messages(client_socket):

    while True:

        try:
            message = client_socket.recv(BUFFER_SIZE)

            if not message:
                break

            print("\n" + message.decode())

        except:
            break


def send_messages(client_socket):

    while True:

        try:
            message = input()
            client_socket.send(message.encode())
        except:
            break


username = input("Enter username: ")

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect((SERVER_HOST, SERVER_PORT))

client.send(username.encode())

print(f"Connected as {username}")
print("Type messages below:")

receive_thread = threading.Thread(
    target=receive_messages,
    args=(client,)
)

send_thread = threading.Thread(
    target=send_messages,
    args=(client,)
)

receive_thread.start()
send_thread.start()