import threading
from threading import Semaphore

# Semaphores
a = Semaphore(1)  # P1 can start
b = Semaphore(0)  # P2 waits
c = Semaphore(0)  # P3 waits

def process1():
    a.acquire()
    print("H")
    print("E")
    b.release()  # allow process2 to run

def process2():
    b.acquire()
    print("L")
    print("L")
    c.release()  # allow process3 to run

def process3():
    c.acquire()
    print("O")

# Create threads
t1 = threading.Thread(target=process1)
t2 = threading.Thread(target=process2)
t3 = threading.Thread(target=process3)

# Start threads
t1.start()
t2.start()
t3.start()

# Wait for all threads to finish
t1.join()
t2.join()
t3.join()
