import os
import time
from multiprocessing import Process


# 进程的简单实现（一）
def do_sth(name):
    """
    进程需要做的事情
    :param name: str
    """
    print("打印的名字：{}, pid：{}".format(name, os.getpid()))
    time.sleep(5)
    print("进程需要做的事情")


# 方法二，继承Process类重写run方法
class MyProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.my_name = name

    def run(self):
        print("My_Process：{}, pid：{}".format(self.my_name, os.getpid()))
        time.sleep(5)
        print("进程需要做的事情")


if __name__ == '__main__':
    # p = Process(target=do_sth, args=("my process", ))
    p = MyProcess("my_process")
    p.start()
    p.join()
