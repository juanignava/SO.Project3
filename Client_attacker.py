import _thread
import sys
import os
import time
import socket

FORMAT = "utf-8"
SIZE = 1024

def check_ping(thread_name, ip, port):
    try:
        clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except:
        return "Error creating socket"

    clientSocket.connect((ip,port))

    #open file
    file = open("test.txt")
    data = file.read()
    init_time = time.time()
    #Send filename
    clientSocket.send("test2.txt".encode(FORMAT))
    msg = clientSocket.recv(SIZE).decode(FORMAT)
    print("Message received " + msg)

    #Send file data
    print("Contents of the file are: ")
    clientSocket.send(data.encode(FORMAT))
    msg = clientSocket.recv(SIZE).decode(FORMAT)
    print("message received " + msg)

    #close file
    file.close()

    #close connection 
    clientSocket.close()
    final_time = time.time()
    
    # display time taken
    response_time = final_time - init_time
    print("Time taken: ", response_time)
    clientSocket.close()
    
def create_threads(ip, port):
    counter = 0
    thread_name = "Thread-"
    thread_list = []
    while (counter < 100):
        thread_actual_name = thread_name + str(counter)
        t = _thread.start_new_thread( check_ping, (thread_actual_name, ip, port) )
        thread_list.append(t)
        counter += 1
    for x in thread_list:
        x.join()

    return

def call_threads(ip, port):
    # Create threads as follows
    try:
        create_threads(ip, port)

    except:
        print ("Error: unable to start threads")
        exit()

    while 1:
        pass

if __name__ == "__main__":
    call_threads(sys.argv[1], 17017)
