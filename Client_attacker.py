import _thread
import sys
import os

def check_ping(thread_name, ip):
    response = os.system("ping -c 100 " + ip)
    # and then check the response...
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"

    print(thread_name + ": ", response)
    
def create_threads(ip):
    counter = 0
    thread_name = "Thread-"
    thread_list = []
    while (counter < 1000):
        thread_actual_name = thread_name + str(counter)
        t = _thread.start_new_thread( check_ping, (thread_actual_name, ip, ) )
        thread_list.append(t)
        counter += 1
    for x in thread_list:
        x.join()

    return

def call_threads(ip):
    # Create threads as follows
    try:
        create_threads(ip)

    except:
        print ("Error: unable to start threads")

    while 1:
        pass

if __name__ == "__main__":
    call_threads(sys.argv[1])
