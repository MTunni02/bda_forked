#  Exercise 1 - generate and sort numbers - generates `n` number of floating-point numbers (e.g. 10,000), each randomly ranging from 0 to 100. 
#  The function uses the bubble sort method to sort numbers in ascending order,

import random, multiprocessing as mp, time

def generate_numbers():
    return random.uniform(0,100)

# ---SERIAL PROCESSING---
def serial_runner(n):
    start = time.perf_counter()
    
    for i in range(n):
        generate_numbers()
