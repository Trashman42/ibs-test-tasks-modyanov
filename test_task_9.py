import time
from threading import Thread


def countdown(name):
    print(f'{name} starts')
    for i in range(10, 0, -1):
        print(f'{name}: {i}')
        time.sleep(2)
    print(f'{name} ends')


p1 = Thread(target=countdown, args=('thread111',), daemon=True)
p2 = Thread(target=countdown, args=('thread666',), daemon=True)
p1.start()
time.sleep(1)
p2.start()
p2.join()
p1.join()
