import time, requests, threading
from get_dog import *

def serial_runner(index):
    start = time.time()
    for i in range(index):
        fetch_and_save_dog_image(i)
    end = time.time()
    print(f"Serial processing time: {end-start} second(s).")
    
    
    
if __name__ == '__main__':
    index = 10
    serial_runner(index)