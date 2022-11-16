from fileinput import close
from http import server
import socket 
import sys
import time
from cryptography.fernet import Fernet


FORMAT = "utf-8"
SIZE = 1024

"""
This method creates, writes and saves the key.
"""
def GenerateKey():
    key = Fernet.generate_key()
    with open("clave.key", "wb") as file_key:
        file_key.write(key)

"""
This method gets the key
output: key from the key file
"""
def LoadKey():
    return open("clave.key", "rb").read()

"""
This method encrypts a file
input: name of the file to encrypt and the key to use
"""
def encript(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_info = file.read()
    encrypted_data = f.encrypt(file_info)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

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

def separateInfo(message):
    char_num = 0
    for char in message:
        if (char != ':'):
            char_num += 1
            continue
        filename = message[:char_num]
        data = message[char_num+1:]
        return filename, data
        

"""
This method executes the server that is constantly waiting for clients
input: server created with TCP and the size of the messages that will be sent"""
def ExecuteServer(serverSocket,messageSize):
    message=""

    # server will continue receiving messages until it receives the message end
    while True:    
        print("Waiting clients")
        serverSocket.listen(100)
        connection , clientAddress=serverSocket.accept()
        print("Connection from: ", clientAddress)

        init_time = time.time()
        #Receiving the file name
        message=connection.recv(SIZE).decode(FORMAT)
        filename = ""
        firstLine =True
        while (message != "finished"):
            filename, data = separateInfo(message)
            if (firstLine):
                file = open(filename, 'w')
                firstLine = False
            else:
                file = open(filename, 'a')
            file.write(data)

            connection.send("line received:".encode(FORMAT))
            message = connection.recv(SIZE).decode(FORMAT)
            
            
            
            #Close file
            file.close()

        GenerateKey()
        key = LoadKey()
        #encript(filename, key)
        

        final_time = time.time()
        # response the time taken
        response_time = final_time - init_time
        answer= "Process time in the server: " + str(response_time)

        connection.send(answer.encode(FORMAT))
        #Close connection
        connection.close()
        print("Disconnected")

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

