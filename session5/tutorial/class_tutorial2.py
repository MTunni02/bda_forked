import multiprocessing as mp, time

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
    
# ---PARALLEL---
def parallel_runner(secs):
    start = time.time()
    p1 = mp.Process(target = boo, args = [1])
    p2 = mp.Process(target = boo, args = [2])
    p3 = mp.Process(target = boo, args = [3])
    p4 = mp.Process(target = boo, args = [4])
    p5 = mp.Process(target = boo, args = [5])

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()

    print(f"Parallel: {round(time.time()-start,2)} second(s)")

    
if __name__ == '__main__':
    #RUN HERE!
    secs = [1,2,3,4,5]
    serial_runner(secs)
    parallel_runner(secs)