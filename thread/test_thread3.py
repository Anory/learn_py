import threading
import time
balance = 0


# 实现多线程
# 使用Threading模块创建线程，直接从threading.Thread继承，然后重写__init__方法和run方法：
class CustomThread(threading.Thread):

    # 用魔法方法的原因是考虑到有可能会传入一些其他的参数
    def __init__(self, n, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        self.n = n

    def change_it(self):
        """
        正常情况下balance的结果永远都会是0，但是在多线程并发的情况下会出现不是0的情况，有可能是数值加上去之后还没来得及
        减掉那边又有其他的线程加上新的数值了，使用线程锁可以解决这样的问题
        """
        global balance
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
