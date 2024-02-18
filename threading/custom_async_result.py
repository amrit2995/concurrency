import threading

class PowerError(Exception):
    def __init__(self, message="Power calculation error"):
        self.message = message
        super().__init__(self.message)

class PowerThread(threading.Thread):
    def __init__(self, val):
        super().__init__()
        self.val = val
        self.result = None

    def run(self):
        squared = self.val ** 2
        if squared > 2147483647:  # Maximum value of integer type
            raise PowerError("Power calculation error: Result exceeds maximum integer value")
        self.result = squared

def power(val):
    thread = PowerThread(val)
    thread.start()
    thread.join()
    if isinstance(thread.result, PowerError):
        raise thread.result
    return thread.result

# Example usage:
try:
    result = power(46341)  # 46341 ** 2 = 2147398281 (exceeds maximum integer value)
    print("Result:", result)
except PowerError as e:
    print("Error:", e.message)
