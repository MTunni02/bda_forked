#  Exercise 1 - generate and sort numbers - generates `n` number of floating-point numbers (e.g. 10,000), each randomly ranging from 0 to 100. 
#  The function uses the bubble sort method to sort numbers in ascending order,

import random, multiprocessing as mp, time
repeats = 1000

def bubble_sort(array):
    n = len(array)
    for j in range(n):
        for k in range(0,j-1):
            if array[k]>array[k+1]:
                array[k],array[k+1] = array[k+1],array[k]


def generate_and_sort_numbers(n):
    result_list = []
    for i in range(n):
        result_list.append(random.uniform(0,100))
    bubble_sort(result_list)
    return result_list

# ---SERIAL PROCESSING---
def serial_runner(n):
    start = time.perf_counter()
    for i in range(n):
        generate_and_sort_numbers(repeats)
    end = time.perf_counter()
    print(f"Serial processing: {end-start} second(s)")

# ---PARALLEL PROCESSING---
def parallel_runner(n):
    start = time.perf_counter()
    processes = []
    for _ in range(n):
        p = mp.Process(target = generate_and_sort_numbers, args=[repeats])
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    end = time.perf_counter()
    print(f"Parallel processing: {end-start} second(s)")
    print(processes)
    print(type(processes[0]))

if __name__ == '__main__':
    n = 3
    serial_runner(n)
    parallel_runner(n)