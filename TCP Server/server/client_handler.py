from threading import Lock

from server.groups import (
    join_group,
    get_client_group,
    groups
)

clients = {}
client_lock = Lock()

COLORS = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[96m"   # Cyan
]

RESET = "\033[0m"

user_colors = {}


def broadcast(message, sender_socket=None):

    with client_lock:
        for client in clients:

            if client != sender_socket:
                try:
                    client.send(message.encode())
                except:
                    pass


def broadcast_group(message, sender_socket, group_name):

    members = groups.get(group_name, [])

    for member in members:

        if member != sender_socket:
            try:
                member.send(message.encode())
            except:
                pass


def handle_client(client_socket, address):

    try:
        username = client_socket.recv(1024).decode()

        user_colors[client_socket] = COLORS[
            len(user_colors) % len(COLORS)
        ]

    except:
        client_socket.close()
        return

    with client_lock:
        clients[client_socket] = username

    join_group(client_socket, "general")

    color = user_colors[client_socket]

    print(f"[CONNECTED] {username} ({address})")

    broadcast(
        f"*** {color}{username}{RESET} joined the chat ***"
    )

    while True:

        try:
            message = client_socket.recv(1024)

            if not message:
                break

            decoded = message.decode().strip()

            # Join a new group
            if decoded.startswith("/join"):

                parts = decoded.split()

                if len(parts) == 2:

                    old_group = get_client_group(client_socket)

                    new_group = parts[1]

                    join_group(client_socket, new_group)

                    print(
                        f"{username} moved from "
                        f"{old_group} to {new_group}"
                    )

                    client_socket.send(
                        f"Joined group: {new_group}".encode()
                    )

                else:

                    client_socket.send(
                        "Usage: /join <group>".encode()
                    )

                continue

            # List available groups
            if decoded == "/groups":

                available_groups = ", ".join(groups.keys())

                client_socket.send(
                    f"Groups: {available_groups}".encode()
                )

                continue

            print(f"{username}: {decoded}")

            group_name = get_client_group(client_socket)

            broadcast_group(
                f"[{group_name}] "
                f"{color}{username}{RESET}: {decoded}",
                client_socket,
                group_name
            )

        except:
            break

    print(f"[DISCONNECTED] {username}")

    with client_lock:

        if client_socket in clients:
            del clients[client_socket]

    broadcast(
        f"*** {color}{username}{RESET} left the chat ***"
    )

    if client_socket in user_colors:
        del user_colors[client_socket]

    client_socket.close()