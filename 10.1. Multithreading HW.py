import time
from threading import Thread


def numbers():
    for i in range(1, 11):
        time.sleep(1)
        print(i, flush=True)


def letters():
    for num in 'abcdefghij':
        time.sleep(1)
        print(num, flush=True)


thread1 = Thread(target=numbers)
thread2 = Thread(target=letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
