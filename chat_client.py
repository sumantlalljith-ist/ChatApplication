import socket
import threading

from client_settings.incoming_messages import receive_messages


# Main function to start the client

def start_client():
    # Create a TCP socket (IPv4, Stream-based connection)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server at the given IP address and port
    # Replace '127.0.0.1' with the actual server IP if connecting remotely
    client_socket.connect(('127.0.0.1',5555))
    print("Connected to the server!")

    # Start a new thread to handle incoming messages from the server
    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()

    # Main loop to send messages to the server
    while True:
        # Prompt the user for a message to send
        message = input("You: ")

        # If the user types 'exit', close the connection and break the loop
        if message.lower() == 'exit':
            break

        # Send the message to the server (encoded to bytes)
        client_socket.send(message.encode())

    # Close the socket connection after exiting the loop
    client_socket.close()
    print("Disconnected from the server")

# Entry point for the client application
if __name__ == "__main__":
    start_client()
