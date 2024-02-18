import threading

def asyncTask(fn):
    # Define a function to run in a thread
    def thread_func():
        result = fn()
        # Store the result in the shared variable
        asyncTask.result = result
    
    # Create a thread with the thread function
    thread = threading.Thread(target=thread_func)
    thread.start()  # Start the thread
    
    # Wait for the thread to complete
    thread.join()
    
    # Return the result stored in the shared variable
    return asyncTask.result

# Example function to run asynchronously
def example_fn():
    import time
    time.sleep(1)  # Simulate some operation
    return "Async task completed"

# Main function to test asyncTask()
def main():
    result = asyncTask(example_fn)
    print("Result of async task:", result)

main()
