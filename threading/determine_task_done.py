import threading
import time

def task1():
    print("task started")
    time.sleep(5)
    print("task ended")

def main():
    t1 = threading.Thread(target=task1)
    t1.daemon = True
    t1.start()
    time.sleep(2)
    print(f"Task{' not ' if t1.is_alive() else ' '}done") #know if the thread is still alive.
    t1.join()
    print(f"Task{' not ' if t1.is_alive() else ' '}done")
    

main()