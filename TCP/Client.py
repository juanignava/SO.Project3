import socket
import sys
import time

def CreateClienteSocket():
    try:
        clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        return clientSocket
    except:
        return "Error creating socket"

def ExecuteClient(clientSocket,ip,port,size):
    clientSocket.connect((ip,port))
    message= "begin"
    count = 0
    try:
            while(message!="end"):
                message= input("Type your message to server: ")
                """
                if (count < 100):
                    message = "test " + str(count)
                    count += 1
                else:
                    message = "end"
                """

                #time.sleep(0.1)

                clientSocket.send(message.encode())
                print("Message sent: ", message)
                answer=clientSocket.recv(size).decode()
                print("Response from server: ", answer)
                
    except:
        print("Error sending the message")
    clientSocket.close()
ExecuteClient(CreateClienteSocket(),"127.0.0.1",17017,2048)