import concurrent.futures, time

# print("Number of processors: ", mp.cpu_count())

def boo(sec):
    print("In boo.. - sleeping for",sec)
    time.sleep(sec)

# ---SERIAL---
def serial_runner(secs):
    start = time.time()
    for sec in secs:
        boo(sec)    
    end = time.time()
    print(f"Serial: {round(end-start,2)} second(s)")
    
# ---PARALLEL RUNNER FUTURES---
def parallel_runner(secs):
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(boo,secs)
    end = time.perf_counter()

    print(f"Parallel runner {end-start} second(s)")


if __name__ == '__main__':
    #RUN HERE!
    secs = [1,2,3,4,5,6]
    # serial_runner(secs)
    parallel_runner(secs)