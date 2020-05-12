from alarm import Alarm
from script import Script
import multiprocessing
import sys

if __name__ == '__main__':
    alarm = Alarm(seconds=5)

    p1 = multiprocessing.Process(target=Script.main)
    p2 = multiprocessing.Process(target=alarm.run)

    p_list = [p1, p2]

    for p in p_list:
        p.start()

    while True:
        if p1.is_alive() is False or p2.is_alive() is False:
            if p1.is_alive():
                p1.terminate()
                sys.exit(1)
            else:
                p2.terminate()
                sys.exit(0)
