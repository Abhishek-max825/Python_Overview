'''
Multithreading in Python
These techniques allow your programs to perform multiple tasks concurrently, improving performance.

Multithreading (using threading module):

Multithreading is suitable for I/O-bound tasks (e.g., waiting for network requests).

'''

import threading
import time

def worker(num):
    print(f"Thread {num}: Starting")
    time.sleep(2)  # Simulate some work
    print(f"Thread {num}: Finishing")

threads = []
for i in range(3):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()  # Wait for all threads to finish

print("All threads completed.")

'''
Mutli Processing

-> Multiprocessing refers to the ability of a system to support more than one processor at the same time.
-> Applications in a multiprocessing system are broken to smaller routines that run independently. 
-> The operating system allocates these threads to the processors improving performance of the system.
'''

# importing the multiprocessing module
import multiprocessing
import os

def worker1():
    # printing process id
    print("ID of process running worker1: {}".format(os.getpid()))

def worker2():
    # printing process id
    print("ID of process running worker2: {}".format(os.getpid()))

if __name__ == "__main__":
    # printing main program process id
    print("ID of main process: {}".format(os.getpid()))

    # creating processes
    p1 = multiprocessing.Process(target=worker1)
    p2 = multiprocessing.Process(target=worker2)

    # starting processes
    p1.start()
    p2.start()

    # process IDs
    print("ID of process p1: {}".format(p1.pid))
    print("ID of process p2: {}".format(p2.pid))

    # wait until processes are finished
    p1.join()
    p2.join()

    # both processes finished
    print("Both processes finished execution!")

    # check if processes are alive
    print("Process p1 is alive: {}".format(p1.is_alive()))
    print("Process p2 is alive: {}".format(p2.is_alive()))

'''
Output :- 
ID of main process: 2900
ID of process p1: 15632
ID of process p2: 24368
ID of process running worker1: 15632
ID of process running worker2: 24368
Both processes finished execution!
Process p1 is alive: False
Process p2 is alive: False
'''