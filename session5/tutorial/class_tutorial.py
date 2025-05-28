import multiprocessing as mp
import time

def foo(sec):
    time.sleep(sec)
    print("Sleeping")

# --SERIAL---

def serial_runner():
    start = time.time()
    foo(1)
    foo(3)
    foo(2)
    end = time.time()
    print(end-start)

# --PARALLEL--

def parallel_runner():
    p1 = mp.Process(target = foo, args=[1])
    p2 = mp.Process(target = foo, args=[3])
    p3 = mp.Process(target = foo, args = [2])
    start = time.perf_counter()
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    end = time.perf_counter()
    print(end-start)


if __name__ == '__main__':
    serial_runner()
    parallel_runner()
