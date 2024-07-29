import threading as td
import argparse
from time import sleep
from random import randint

class Barrier:
    count = 0
    mutex = td.Lock()
    semaphore = td.Semaphore(0)

    def __init__(self, threadsNumber):
        self.threadsNumber = threadsNumber
    
    def wait(self):
        self.mutex.acquire()
        try:
            self.count += 1
        finally:
            self.mutex.release()
        
        if (self.count == self.threadsNumber):
            self.semaphore.release()
        
        self.semaphore.acquire()
        self.semaphore.release()      


def threadCode(threadsTimes,idTime, barrier):
    sleep(randint(0,5))
    s = randint(0,10)
    threadsTimes[idTime] = s
    barrier.wait()
    if(idTime == 0):
        sleep(threadsTimes[idTime])
    else:
        sleep(threadsTimes[idTime - 1])

    
def main():
     parser = argparse.ArgumentParser(description="Lê um número inteiro que representa a quantidade de threads que devem ser criadas")
     parser.add_argument("input", help="Número de threads")
     args = parser.parse_args()
     threadsNumber = int(args.input)
     threads = []
     threadsTimes = [0] * threadsNumber
     barrier = Barrier(threadsNumber)

     for i in range(0,threadsNumber):
        thread =  td.Thread(target=threadCode, args=(threadsTimes,i,barrier, ))
        thread.start()
        threads.append(thread)
    
     for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()