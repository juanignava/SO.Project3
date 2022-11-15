import _thread
import time

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

def create_threads():
    counter = 0
    thread_name = "Thread-"
    while (counter < 5):
        thread_actual_name = thread_name + str(counter)
        _thread.start_new_thread( print_time, (thread_actual_name, (counter+1), ) )
        counter += 1

        
def call_threads():
    # Create two threads as follows
    try:
        create_threads()

    except:
        print ("Error: unable to start threads")

    while 1:
        pass

if __name__ == "__main__":
    call_threads()
