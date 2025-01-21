## it allow you to create process which run parallel
## CPU-Bound Tasks
## Parallel execution Multiple cores of the CPU



import multiprocessing


import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square : {i*i}")


def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i*i*i}")



t1 = multiprocessing.Process(target = print_numbers)
t2  = multiprocessing.Process(target = print_letter)

# start the thread
t1.start()
t2.start()

# join the thread
t1.join()
t2.join