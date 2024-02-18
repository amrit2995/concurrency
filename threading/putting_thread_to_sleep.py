import threading
import time


def sleep_three_seconds():
    time.sleep(3)
    

def main():
    start_time = time.time()
    t1 = threading.Thread(target=sleep_three_seconds)
    t1.start()
    t1.join()
    end_time = time.time()
    runtime = end_time - start_time
    print(f"Runtime: {runtime}")

main()