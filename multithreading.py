### where you have to wait for many operators
### when you want to improve the throughput of your application



import threading
import time


def print_numbers():
    for i in range(5):
        print(f"NUmber:{i}")

def print_letter():
    for letter in "abcde" 
    print(f"Letter : {letter}")


# create 2 threads
t1 = threading.Thread(target = print_numbers)
t2  = threading.Thread(target = print_letter)

# start the thread
t1.start()
t2.start()

# join the thread
t1.join()
t2.join

print_numbers()
print_letter