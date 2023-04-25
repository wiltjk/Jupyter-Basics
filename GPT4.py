import random
import threading
import time

# BaseThread: A class for creating threads with a thread count tracking
class BaseThread(threading.Thread):
    __threadCount = 0
    __threadCountLock = threading.Lock()  # Protects access to the shared __threadCount

    def __init__(self, name="UnnamedThread"):
        super().__init__()
        self.name = name
        with BaseThread.__threadCountLock:
            BaseThread.__threadCount += 1
        print(f"Starting {self.name}")

    def __del__(self):
        with BaseThread.__threadCountLock:
            BaseThread.__threadCount -= 1
        print(f"Ending {self.name}")

    @classmethod
    def getThreadCount(cls):
        return cls.__threadCount


# TestThread: A thread that simulates workload by sleeping for a random duration
class TestThread(BaseThread):
    def run(self):
        sleep_secs = random.randint(1, 5)
        print(f"{self.name} -- Sleeping {sleep_secs}s -- {self.getThreadCount()} thread(s)")
        time.sleep(sleep_secs)
        print(f"{self.name} -- {time.ctime()} -- {self.getThreadCount()} thread(s)")


# test_threads: Function to create, start, and join TestThreads
def test_threads():
    threads = []

    # Create and start TestThreads
    for i in range(10):
        thread = TestThread(f"Thread-{i}")
        thread.start()
        threads.append(thread)

    # Wait for all TestThreads to complete
    for t in threads:
        t.join()


if __name__ == "__main__":
    print("\n\n—BOJ—\n\n")
    test_threads()
    print("\n\n—EOJ—\n\n")