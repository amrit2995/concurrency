import threading

def example_async_task():
    import time
    time.sleep(1)
    return "async task comeplete"


def create_async_task():
    t1 = threading.Thread(target=example_async_task)
    t1.start()
    t1.join()
    return t1.result

print(create_async_task())