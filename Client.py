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
def ExecuteClient(clientSocket, ip, port, src_filename, dest_filename):
    
    # connect socket
    clientSocket.connect((ip,port))

    # read and send the file
    file = open(src_filename)
    init_time = time.time()
    line = file.readline()
    counter = 1
    while (line != ""):
        # read until de file is empty
        print("sending line: ", counter)
        if (line == '\n'):
            line = file.readline()
            counter += 1
            continue
        # construct a message that contains the destiny file
        message = dest_filename + ":" + line
        clientSocket.send(message.encode(FORMAT))
        response_msg = clientSocket.recv(SIZE).decode(FORMAT)
        line = file.readline()
        counter += 1

    # to indicate the end of the file send the finished flag
    clientSocket.send("finished".encode(FORMAT))
    response_msg = clientSocket.recv(SIZE).decode(FORMAT)
    server_time = float(response_msg)
    print("Server time -> ", server_time)

    #close file
    file.close()

    #close connection 
    clientSocket.close()
    final_time = time.time()
    
    # display time taken
    total_time = final_time - init_time
    print("Total time taken -> ", total_time)
    print("Connection time -> ", total_time - server_time)
    clientSocket.close()


if __name__ == "__main__":
    ip = sys.argv[1]
    src_filename = sys.argv[2]
    dest_filename = sys.argv[3]
    ExecuteClient(CreateClientSocket(), ip, 17017, src_filename, dest_filename)
