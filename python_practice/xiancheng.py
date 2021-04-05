import _thread
import logging
import threading
from time import sleep, ctime

logging.basicConfig(level=logging.INFO)

loops = [2, 4]


# _thread使用实例
# def loop(nloop, nsec, lock):
#     logging.info(f"start loop{nloop}  at" + ctime())
#     sleep(nsec)
#     logging.info(f"start loop{nloop}  at" + ctime())
#     lock.release()
#
#
# def main():
#     logging.info("start all at" + ctime())
#     locks = []
#     nloops = range(len(loops))
#     #根据进程数循环获取锁
#     for i in nloops:
#         lock = _thread.allocate_lock()
#         lock.acquire()
#         locks.append(lock)
#     #起线程
#     for i in nloops:
#         _thread.start_new_thread(loop, (i, loops[i], locks[i]))
#     for i in nloops:
#         while locks[i].locked(): pass
#     logging.info("end all at"+ctime())

# #threading使用实例
# def loop(nloop, nsec):
#     logging.info(f"start loop{nloop}  at" + ctime())
#     sleep(nsec)
#     logging.info(f"start loop{nloop}  at" + ctime())
#
# def main():
#     logging.info("start all at" + ctime())
#     threads = []
#     nloops = range(len(loops))
#     #起线程
#     for i in nloops:
#         t = threading.Thread(target= loop, args=(i, loops[i]))
#         threads.append(t)
#     for i in nloops:
#         threads[i].start()
#     #等threads0是不是结束，如果没有结束就会阻塞main不然它执行
#     for i in nloops:
#         threads[i].join()
#     logging.info("end all at"+ctime())


# 推荐使用以下方式实现多线程

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)


def loop(nloop, nsec):
    logging.info(f"start loop{nloop}  at" + ctime())
    sleep(nsec)
    logging.info(f"start loop{nloop}  at" + ctime())


def main():
    logging.info("start all at" + ctime())
    threads = []
    nloops = range(len(loops))
    # 起线程
    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)
    for i in nloops:
        threads[i].start()
    # 等threads0是不是结束，如果没有结束就会阻塞main不然它执行
    for i in nloops:
        threads[i].join()
    logging.info("end all at" + ctime())


if __name__ == '__main__':
    main()
