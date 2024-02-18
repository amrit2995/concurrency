#using threading

import threading

# Global variable
a = 0

# Mutex
m = threading.Lock()

def func():
    global a
    for _ in range(5000000):
        with m:
            a += 1

def main():
    # Create threads
    t1 = threading.Thread(target=func)
    t2 = threading.Thread(target=func)

    # Start threads
    t1.start()
    t2.start()

    # Wait for threads to finish
    t1.join()
    t2.join()

    print("Final value of a:", a)

if __name__ == "__main__":
    main()


# We define a global variable a to store the value that will be modified by the threads.
# We create a mutex m using threading.Lock().
# In the func() function, we use the with statement to acquire the lock before modifying the global variable a. This ensures that only one thread can modify a at a time.
# In the main() function, we create two threads t1 and t2, each calling the func() function.
# We start both threads using the start() method and wait for them to finish using the join() method.
# Finally, we print the final value of a to see the result. Since the mutex ensures that only one thread modifies a at a time, the final value of a will be 1e7 as expected.
