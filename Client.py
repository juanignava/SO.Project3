import socket
import sys
import time

def CreateClienteSocket():
    try:
        clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        return clientSocket
    except:
        return "Error creating socket"

def ExecuteClient(clientSocket,ip,port,size, message, file_name):
    init_time = time.time()
    clientSocket.connect((ip,port))
    
    
    clientSocket.send(message.encode())
    print("Message sent: ", message)
    answer=clientSocket.recv(size).decode()

    final_time = time.time()
    print("Response from server: ", answer)
    
    response_time = final_time - init_time
    print("Time taken: ", response_time)
    
    #except:
        #print("Error sending the message")
    clientSocket.close()

if __name__ == "__main__":
    ExecuteClient(CreateClienteSocket(),"192.168.0.25",17017,2048, sys.argv[1], sys.argv[2])