import threading
from threading import Semaphore
import time

# Shared buffer
particle_buffer = []

# Semaphores and initial values
space = Semaphore(100)   # empty particle slots
s = Semaphore(0)         # particles in buffer
lock = Semaphore(1)      # mutual exclusion


def producer(pid):
    while True:
        # Produce particle pair
        p1 = f"P{pid}-1"
        p2 = f"P{pid}-2"

        # Need two free spaces
        space.acquire()
        space.acquire()
        lock.acquire()

        # Place particles consecutively
        particle_buffer.append(p1)
        particle_buffer.append(p2)
        print(f"Producer {pid} produced {p1}, {p2}")

        lock.release()
        s.release()
        s.release()

        time.sleep(1)


def consumer():
    while True:
        # Need two particles
        s.acquire()
        s.acquire()
        lock.acquire()

        # Fetch particle pair
        p1 = particle_buffer.pop(0)
        p2 = particle_buffer.pop(0)
        print(f"Consumer packaged {p1}, {p2}")

        lock.release()
        space.release()
        space.release()

        time.sleep(1.5)


# Create multiple producers
for i in range(3):
    threading.Thread(target=producer, args=(i + 1,), daemon=True).start()

# Create single consumer
threading.Thread(target=consumer, daemon=True).start()

# Keep main thread alive
while True:
    time.sleep(10)
