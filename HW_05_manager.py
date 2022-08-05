from multiprocessing import Process, Manager
from datetime import datetime


def factorize(name, number, fin):
    rez = []
    for i in range(1, number+1):
        if number % i == 0:
            rez.append(i)
    fin[name] = rez


a, b, c, d = 128, 255, 99999, 10651060


if __name__ == '__main__':
    script_start = datetime.now()
    manager = Manager()
    m = manager.dict()
    p1 = Process(target=factorize, args=('a', a, m))
    p2 = Process(target=factorize, args=('b', b, m))
    p3 = Process(target=factorize, args=('c', c, m))
    p4 = Process(target=factorize, args=('d', d, m))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    print(m)

    script_end = datetime.now()
    print((script_end - script_start).total_seconds())
