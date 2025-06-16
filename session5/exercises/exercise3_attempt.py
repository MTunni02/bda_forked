### Exercise 3: Sum of squares

# Create a script to calculate the sum of squares of integer numbers.

import time
import concurrent.futures
import multiprocessing

def sum_square(n):
    return sum(i * i for i in range(n))

def serial_runner(arange):
    start = time.perf_counter()
    for i in range(arange):
        sum_square(i)
    end = time.perf_counter()
    print(f'Serial processing time: {end-start} second(s)')

# ** Task 2 **
# With the parallel runner (ProcessPoolExecutor)

def parallel_runner(arange,n):
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=n+1) as executor:
        results = list(executor.map(sum_square, range(arange)))
    end = time.perf_counter()
    print(f'Parallel (process poolmap - {n+1} workers): {end-start:.4f} second(s).')


# **Task 3**

# Using the `multiprocessing.Pool`, measure the time taken to run and compare it against the `parallel_runner`. Do you notice any difference?


def parallel_map(arange):
    start = time.perf_counter()
    with multiprocessing.Pool() as p:
        results = list(p.map(sum_square,range(arange)))
    end = time.perf_counter()
    print(f"Multiprocessing pool processing time: {end-start} second(s)")
    return results

if __name__ == "__main__":
    arange = 20000
    serial_runner(arange)
    for n in range(8):
        parallel_runner(arange,n)
    parallel_map(arange)


# > [!NOTE]
# >
# > The `multiprocessing.Pool` is a class provided by Python's `multiprocessing` module.
# It offers a convenient means of parallelising the execution of a function across multiple input values, distributing the input data across processes (data parallelism). This is particularly useful for performing CPU-intensive operations concurrently on multiple processors, which can significantly speed up the execution of a function that is applied to many items.

# **Task 4**

# What is the difference between `multiprocessing.Pool()` and `concurrent.futures.ProcessPoolExecutor` in Python?

# - `multiprocessing.Pool()`: Best suited for straightforward parallel processing tasks where you want to quickly distribute a task among processes, especially when dealing with simple, independent data processing.
# - `ProcessPoolExecutor`: Ideal for more complex applications requiring better error handling, future-based programming, or integration with other concurrent execution features.

