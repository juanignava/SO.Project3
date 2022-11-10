from fileinput import close
from http import server
import socket 
import sys
import time

"""
This method creates a TCP socket server
input: ip and port needed to create the server
output: the server or a string in case there is a mistake"""
def CreateServer(ip,port):
    if isinstance(port,int) and isinstance(ip,str):
        try:
            serverSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            serverSocket.bind((ip,port)) 
            return serverSocket
        except:
            return "Error creatign the server"
    else:
        return "ip or port incorrect"

"""
This method executes the server that is constantly waiting for clients
input: server created with TCP and the size of the messages that will be sent"""
def ExecuteServer(serverSocket,messageSize):
    message=""

    # server will continue receiving messages until it receives the message end
    while message!="end":    
        print("Waiting clients")
        serverSocket.listen(1)

        try:
            connection , clientAddress=serverSocket.accept()
            message=connection.recv(messageSize).decode()
            print("Connection from: ", clientAddress)
            if message:
                init_time = time.time()
                print("Message received: ",message)
                for i in range(10000):
                    # main load of the server 
                    # add the file encryption in here
                    calc = i*i
                    result = calc // i

                final_time = time.time()
                # response the time taken
                response_time = final_time - init_time
                answer= "Process time in the server: "
                answer += str(response_time)
                connection.send(answer.encode())
        except:
            print("Error accepting the connection from client")
            connection.close()
            exit()
        connection.close()
    
    # shutdown the server once finished
    serverSocket.shutdown(socket.SHUT_RDWR)
    serverSocket.close()
    print ("closed")

"""
Function that runs a server based on the inputs
input: ip and port of the server and also the size of the
    messages in the server"""
def RunServer(ip,port,size):
    server=CreateServer(ip,port)
    if isinstance(server, str):
        return  print(server)
    ExecuteServer(server,size)

if __name__ == "__main__":
    RunServer(sys.argv[1],17017,2048)

