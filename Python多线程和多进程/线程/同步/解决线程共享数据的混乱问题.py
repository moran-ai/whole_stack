from threading import *

num = 0


def run():
    lock.acquire()  # 加锁
    print(f'线程{current_thread().name}开始执行')
    global num
    for i in range(500000):
        num += 1
    print(f'线程{current_thread().name}执行完毕，num的值是{num}')
    lock.release()  # 解锁


if __name__ == '__main__':
    # 创建锁
    lock = Lock()
    threads = []
    for i in range(5):
        t1 = Thread(target=run)
        t1.start()
        threads.append(t1)

    for i in threads:
        i.join()

    print(f'主线程结束,全局变量num的值是{num}')
