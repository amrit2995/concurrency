import threading
import time

def test_thread():
    print("thread starter")
    time.sleep(2)
    print("thread end")

# Join mode:
a = threading.Thread(target=test_thread)
a.start() #start the thread
a.join() #wait for the thread to execute
print("thread execution complete")


# Daemon mode (detach mode):
b = threading.Thread(target=test_thread)
b.daemon = True # Set the thread as a daemon thread
b.start() #Start the thread
print("thread execution complete")