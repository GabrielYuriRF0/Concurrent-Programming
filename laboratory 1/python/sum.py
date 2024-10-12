import os
import sys
from multiprocessing import Process

def do_sum(path):
    _sum = 0
    with open(path, 'rb',buffering=0) as f:
        byte = f.read(1)
        while byte:
            _sum += int.from_bytes(byte, byteorder='big', signed=False)
            byte = f.read(1)
    print(f"{path} : {_sum}")

if __name__ == "__main__":
    paths = sys.argv[1:]
    threads = []
    
    for path in paths:
    #many error could be raised error. we don't care
        thread = Process(target=do_sum, args=(path, ))
        thread.start()
        threads.append(thread)


    for thread in threads:
        thread.join()
    

