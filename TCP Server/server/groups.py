groups = {
    "general": [],
    "networking": [],
    "gaming": [],
    "security": []
}


def join_group(client_socket, group_name):

    for group in groups.values():

        if client_socket in group:
            group.remove(client_socket)

    if group_name not in groups:
        groups[group_name] = []

    groups[group_name].append(client_socket)


def get_client_group(client_socket):

    for group_name, members in groups.items():

        if client_socket in members:
            return group_name

    return None


def get_groups():

    return list(groups.keys())