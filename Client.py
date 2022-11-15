import socket
import sys
import time

FORMAT = "utf-8"
SIZE = 1024
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
    
    clientSocket.connect((ip,port))

    #open file
    file = open("test.txt")
    data = file.read()
    init_time = time.time()
    #Send filename
    clientSocket.send("test.txt".encode(FORMAT))
    msg = clientSocket.recv(SIZE).decode(FORMAT)
    print("Message received {msg}")

    #Send file data
    clientSocket.send(data.encode(FORMAT))
    msg = clientSocket.recv(SIZE).decode(FORMAT)
    print("message received {msg}")

    #close file
    file.close()

    #close connection 
    clientSocket.close()
    final_time = time.time()
    print("Response from server: ", answer)
    
    # display time taken
    response_time = final_time - init_time
    print("Time taken: ", response_time)
    clientSocket.close()

if __name__ == "__main__":
    ExecuteClient(CreateClientSocket(),sys.argv[1],17017,2048, sys.argv[2])