import random
import threading
import time

# Base class for all Threads
class BaseThread (threading.Thread):
    __threadCount = 0
    
    # Constructor 
    def __init__ (self, name = "thread name not set"):
        threading.Thread.__init__(self)
        self.name = name
        BaseThread.__threadCount += 1
        print (f"Starting {self.name} created")
                
    # Destructor 
    def __del__ (self):
        BaseThread.__threadCount -= 1
        print (f"Ending {self.name} deleted")
        
    # Return thread count 
    def getThreadCount (self):
        return BaseThread.__threadCount
        
        
# Child Class TestThread
class TestThread (BaseThread):
    #  Run thread
    def run (self):
        sleepSecs = random.randint(1, 4) + 1
        
        print (f"{self.name} -- Sleeping {sleepSecs} second(s) -- {self.getThreadCount ()} thread(s)")
        time.sleep (sleepSecs)
        
        print (f"{self.name} -- {time.ctime (time.time())} -- {self.getThreadCount ()} thread(s)")
        return
        
        
# Test Threads
def testThreads ():
    newThreads = []
        
    for ii in range (0, 10):
        try:
            newThread = TestThread (f"Thread-{ii}")
            newThread.start ()
            newThreads.append (newThread)
            
        except:
            print (f"*** Thread creation error iteration {ii}.") 
    
    # Wait for all threads to complete
    for tt in newThreads:
       tt.join ()
   
    return


# Main
print ("\n\n—BOJ—\n\n")
testThreads ()
print ("\n\n—EOJ—\n\n")
