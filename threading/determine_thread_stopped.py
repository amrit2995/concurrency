import threading
import time

def count_keep_running(event):
    print("Waiting for the event")
    event.wait()
    while event.is_set():
        time.sleep(1)
        print("is set")
    
    

def main():
    event = threading.Event()
    thread = threading.Thread(target=count_keep_running, args=(event,))
    print("starting thread")
    # thread.daemon = True
    thread.start()
    time.sleep(4)
    event.set()
    time.sleep(6)
    print("Clearing the event")
    event.clear()
    thread.join()

main()
