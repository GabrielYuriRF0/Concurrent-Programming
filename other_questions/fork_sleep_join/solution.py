import argparse
import threading
from time import sleep
from random import randint

def threadCode():
    sleep(randint(1,5))


def threadCodeWithSemaphore(semaphore):
    threadCode()
    semaphore.release()


def main():
        parser = argparse.ArgumentParser(description="Lê um número inteiro que representa a quantidade de threads que devem ser criadas")
        parser.add_argument("input", help="Número de threads")
        parser.add_argument("--use_semaphores", action="store_true", help="Usar semáforos para esperar as threads")
        args = parser.parse_args()
        threadsNumber = int(args.input)
        useSemaphore = args.use_semaphores
        semaphore = threading.Semaphore(0)
        threads = []

        if(useSemaphore):
            for i in range(0, threadsNumber):
                 thread = threading.Thread(target=threadCodeWithSemaphore, args=(semaphore, ))
                 thread.start()

            for i in range(0, threadsNumber):
                 semaphore.acquire()
        else:
            for i in range(0, threadsNumber):
                    thread = threading.Thread(target=threadCode)
                    thread.start()
                    threads.append(thread)
            
            for thread in threads:
                thread.join()

        print(f'A quantidade de threads criadas foi de {threadsNumber}')

if __name__ == "__main__":
    main()


