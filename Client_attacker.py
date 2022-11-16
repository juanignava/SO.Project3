import threading
import sys
import os

AMOUNT_THREADS = 100

def send_file(thread_name, ip, port):
    dest_file = thread_name+".txt"
    os.system("make client src_filename=test.txt dest_filename="+dest_file)
    
def create_threads(ip, port):
    counter = 0
    thread_name = "Thread-"
    thread_list = []

    # crete threads
    while (counter < AMOUNT_THREADS):
        thread_actual_name = thread_name + str(counter)
        t = threading.Thread( target=send_file, args=(thread_actual_name, ip, port,) )
        t.start()
        thread_list.append(t)
        counter += 1

    # wait for threads to end
    for x in thread_list:
        x.join()

    return

if __name__ == "__main__":
    ip = sys.argv[1]
    create_threads(ip, 17017)
