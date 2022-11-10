from fileinput import close
from http import server
import socket 
import sys
import time


def CreateServer(ip,port): # ip->id, port-> "channel"
    if isinstance(port,int) and isinstance(ip,str):
        try:
            serverSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket for TCP
            serverSocket.bind((ip,port)) 
            return serverSocket
        except:
            return "Error creatign the server"
    else:
        return "ip or port incorrect"
def ExecuteServer(serverSocket,messageSize):
    message=""
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
                    calc = i*i
                    print(calc)
                final_time = time.time()
                response_time = final_time - init_time
                answer="All right"
                #answer += str(response_time)
                connection.send(answer.encode())
        except:
            print("Error accepting the connection from client")
        connection.close()

def RunServer(ip,port,size):
    server=CreateServer(ip,port)
    ExecuteServer(server,size)
RunServer("192.168.0.25",17017,2048)

