import threading
import time

number = 0
lock = threading.Lock()


def plus(lk):
    global number
    lk.acquire()
    for _ in range(10000):
        number += 1
    print('子线程%s运算结束后， number = %s' % (threading.current_thread().getName(), number))
    lk.release()

if __name__ == '__main__':
    for i in range(2):
        t = threading.Thread(target= plus, args= (lock,))
        t.start()
    time.sleep(2)
    print('主线程结束后，number = ', number)



