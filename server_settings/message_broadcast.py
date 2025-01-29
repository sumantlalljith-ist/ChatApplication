

# Broadcast message to all connected clients except the sender
def broadcast(message, clients, sender_socket):
    """
    Sends a message to all connected clients except to the sender.

    Parameters:
    :param message (bytes): The message to be sent
    :param clients (List): List of connected client sockets
    :param sender_socket (socket): The socket that sent the original message
    :return:
    """

    for client in clients:
        # Check to avoid sending the message back to sender
        if client != sender_socket:
            try:
                # Send the message to the current client
                client.send(message)
            except:
                # If sending fails, remove the client from the list
                clients.remove(client)
