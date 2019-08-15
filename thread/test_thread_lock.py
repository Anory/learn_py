import threading
import time
balance = 0
# 先实例一个锁的对象
my_lock = threading.Lock()


# 实现多线程
# 使用Threading模块创建线程，直接从threading.Thread继承，然后重写__init__方法和run方法：
class CustomThread(threading.Thread):

    def __init__(self, n, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        self.n = n

    def change_it(self):
        """
        正常情况下balance的结果永远都会是0，但是在多线程并发的情况下会出现不是0的情况，有可能是数值加上去之后还没来得及
        减掉那边又有其他的线程加上新的数值了，使用线程锁可以解决这样的问题
        """
        global balance
        # 可以保证数据的准确性，在多个线程的情况下，后面的线程也是等待前面执行的线程执行完并释放锁之后才会执行
        # 当前面有被锁的线程在执行的时候后面有线程来的时候也只能等着（也叫死锁）
        with my_lock:
            balance += self.n
            time.sleep(1.5)
            balance -= self.n
            time.sleep(1)
            print("n is {}, balance is {}".format(self.n, balance))

    def run(self):
        for i in range(10000):
            self.change_it()


if __name__ == '__main__':
    t = CustomThread(5)
    t2 = CustomThread(8)
    t.start()
    t2.start()
    t.join()
    t2.join()
