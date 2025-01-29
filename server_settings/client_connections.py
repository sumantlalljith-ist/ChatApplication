from server_settings.message_broadcast import broadcast
# Handle communication with an individual client
def handle_client(client_socket, clients):
    """
    Handles the communication with a single connected client

    Parameters:
    :param client_socket: The client socket to handle
    :param clients: List of connected client sockets
    :return:
    """
    while True:
        try:
            # Receive a message from the client (buffer size: 1024 bytes)
            message = client_socket.recv(1024)

            # If no message is received, the client has disconnected
            if not message:
                break

            print(f"Message received: {message.decode()}")
            # Broadcast the message to other connected clients
            broadcast(message, clients, client_socket)
        except:
            # Exit the loop if any exception occurs (e.g., connection closed)
            break

    # Close the clients socket and remove it from the clients list
    client_socket.close()
    clients.remove(client_socket)
    print("Client disconnected")