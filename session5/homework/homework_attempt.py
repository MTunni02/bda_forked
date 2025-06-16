from PIL import Image, ImageFilter
import multiprocessing, time, concurrent.futures

img_names = ['photo-1516117172878-fd2c41f4a759.jpg',
'photo-1532009324734-20a7a5813719.jpg',
'photo-1524429656589-6633a470097c.jpg',
'photo-1530224264768-7ff8c1789d79.jpg',
'photo-1564135624576-c5c88640f235.jpg',
'photo-1541698444083-023c97d3f4b6.jpg',
'photo-1522364723953-452d3431c267.jpg',
'photo-1513938709626-033611b8cc03.jpg',
'photo-1507143550189-fed454f93097.jpg',
'photo-1493976040374-85c8e12f0c0e.jpg',
'photo-1504198453319-5ce911bafcde.jpg',
'photo-1530122037265-a5f1f91d3b99.jpg',
'photo-1516972810927-80185027ca84.jpg',
'photo-1550439062-609e1531270e.jpg',
'photo-1549692520-acc6669e2f0c.jpg']


def blur_and_resize(args):
    size,folder,img_name = args
    img = Image.open('session5/homework/images/'+img_name)
    img = img.filter(ImageFilter.GaussianBlur(25))
    img.thumbnail((size,size))
    img.save(f'session5/homework/{folder}/{img_name}')
    

def serial_runner(size):
    start = time.perf_counter()
    for img_name in img_names:
        args = (size,'processed',img_name)
        blur_and_resize(args)
    end = time.perf_counter()
    print(f"Serial processing time: {end-start} second(s)")

def parallel_runner(size):
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=8) as executor:
        executor.map(blur_and_resize,[(size,'processed2',name) for name in img_names])
    end = time.perf_counter()
    print(f'Parallel (process poolmap - 8 workers): {end-start:.4f} second(s).')

def multi_runner(size):
    start = time.perf_counter()
    with multiprocessing.Pool() as p:
        p.map(blur_and_resize,[(size,'processed3',name) for name in img_names])
    end = time.perf_counter()
    print(f'Multiprocessing time: {end-start} second(s).')    

if __name__ == '__main__':
    size = 3400
    serial_runner(size)
    parallel_runner(size)
    multi_runner(size)
