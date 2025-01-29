
# Function to listen for and display messages from the server
def receive_messages(client_socket):
    while True:
        try:
            # Receive a message from the server (maximum size 1024 bytes)
            message = client_socket.recv(1024)

            # If the server closes the connection, break the loop
            if not message:
                break;

            #Display the received message to the user
            print(f"\n{message.decode()}")

        except:
            # If an error occurs (e.g., server disconnected), display a message and break the loop
            print("Connection to server is lost")
            break

