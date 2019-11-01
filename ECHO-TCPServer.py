import socket
import threading

def handle_tcp_connection(client_socket) :
    #Reads data from socket buffer
    data = client_socket.recv(1024)
    #Prints read data
    print('Recived: {}'.format(data))
    #Returns same data to the client
    client_socket.send(data)
    #Close socket
    client_socket.close()

#Will use all available interface on port 1025
bind_ip = ''
bind_port = 1025

#Create socket to listen connection requests
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Bind it with an IP and PORT
server.bind((bind_ip, bind_port))
#Set max clients to 5
server.listen(5)

while True:
    #Wait for a requests and then accept it
    client_socket, client_address = server.accept()
    #Prints connection information
    print('Accepted connection request from: {}'.format(client_address))
    #Create a new thread to comunicate with this client
    client_handler = threading.Thread(target=handle_tcp_connection, args=(client_socket,))
    #Start its execution
    client_handler.start()