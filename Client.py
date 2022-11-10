import socket
import sys
import time

"""
This function creates the client socket with TCP
output: the client socket instance"""
def CreateClientSocket():
    try:
        clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        return clientSocket
    except:
        return "Error creating socket"

"""
This function connects to the server, sends a message and then closes the connection
input: clients, ip, port and size to create a correct conenection. message
    to indicate the texto to share with the server"""
def ExecuteClient(clientSocket,ip,port,size, message):
    init_time = time.time()
    clientSocket.connect((ip,port))
    
    # Send message
    clientSocket.send(message.encode())
    print("Message sent: ", message)
    answer=clientSocket.recv(size).decode()
    final_time = time.time()
    print("Response from server: ", answer)
    
    # display time taken
    response_time = final_time - init_time
    print("Time taken: ", response_time)
    clientSocket.close()

if __name__ == "__main__":
    ExecuteClient(CreateClientSocket(),sys.argv[1],17017,2048, sys.argv[2])