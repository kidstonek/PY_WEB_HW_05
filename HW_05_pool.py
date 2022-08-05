from multiprocessing import Pool, current_process, cpu_count
from datetime import datetime


def factorize(number):
    rez = []
    for i in range(1, number+1):
        if number % i == 0:
            rez.append(i)
    return rez


def callback(result):
    # for i in result:
    #     print(i)
    pass


if __name__ == '__main__':
    script_start = datetime.now()
    with Pool(cpu_count()) as pross:
        pross.map_async(factorize, [128, 255, 99999, 10651060], callback=callback)
        pross.close()
        pross.join()

    script_end = datetime.now()
    print((script_end - script_start).total_seconds())
