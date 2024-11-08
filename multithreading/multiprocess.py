import multiprocessing
import time

def helper(num):
    print(f"Work {num} started...")
    print(f"word {num} end.")

# s = time.time()
# for i in range(5):
#     helper(i)
#     e = time.time()
#     t = e - s
#     print(f"this code runs in {t} sec....")

if __name__ == "__main__":
    start_time = time.time()
    processor = []
    for i in range(5):
        pp = multiprocessing.Process(target = helper , args=(i , ))
        processor.append(pp)
        pp.start()
    for i in processor:
        i.join()
    end_time = time.time()
    t = end_time - start_time
    print(f"this code runs in {t} sec....")