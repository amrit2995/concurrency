import threading

def func(thread1, thread2):
    # Swap target functions of the threads
    import pdb;pdb.set_trace()
    thread1_func = thread1._target
    thread1._target = thread2._target
    thread2._target = thread1_func

def main():
    thread1 = threading.Thread(target=lambda: print("Thread 1 is executing"))
    thread2 = threading.Thread(target=lambda: print("Thread 2 is executing"))
    # Start the threads
    thread1.start()
    thread2.start()

    import pdb;pdb.set_trace()
    id1 = thread1.ident
    id2 = thread2.ident

    # Pass the threads to the func function
    func(thread1, thread2)
    print(thread1.ident == id2 and thread2.ident == id1)

    # Wait for the threads to finish
    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()
