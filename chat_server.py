import socket # Module for network communication
import threading # Module to handle multiple client connections concurrently

from server_settings.client_connections import handle_client


# Main server function to start listening for client connections
def start_server():
    """Starts the chat server and listens for incoming connections"""
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the server to all available interfaces on port 5555
    server_socket.bind(('0.0.0.0',5555))
    # Set the server to listen for incoming connections (maximum 5 in queue)
    server_socket.listen(5)
    print("Server listening on port 5555...")

    # List to store active client sockets
    clients = []

    while True:
        # Accept a new client connection
        client_socket, client_address = server_socket.accept()

        # Add the client socket to the list of connected clients
        clients.append(client_socket)

        # Create a new thread to handle communication with this client
        thread = threading.Thread(target=handle_client, args=(client_socket, clients))
        thread.start()

if __name__ == "__main__":
    # Run the server when the script is executed directly
    start_server()



