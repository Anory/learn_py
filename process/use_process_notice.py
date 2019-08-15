import random
import time
from multiprocessing import Process, Queue, current_process


# 进程之间的通信
class WriteProcess(Process):
    # 传入管理进程通信的queue实例对象
    def __init__(self, q, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.q = q

    def run(self):
        c_list = [
            "第一行内容",
            "第二行内容",
            "第三行内容",
            "第四行内容",
        ]
        for line in c_list:
            print("写入内容：{}，进程名字：{}".format(line, current_process().name))
            self.q.put(line)
            # 每写一次休息1-5分钟
            time.sleep(random.randint(1, 2))


class ReadProcess(Process):
    # 传入管理进程通信的queue实例对象
    def __init__(self, q, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.q = q

    def run(self):
        while True:
            content = self.q.get()
            print("读取内容：{}, 进程名字：{}".format(content, self.name))


if __name__ == '__main__':
    # 通过queue队列共享数据
    q = Queue()
    w = WriteProcess(q)
    w.start()
    r = ReadProcess(q)
    r.start()
    # 等待写子进程执行完毕再执行主进程
    w.join()
    # r.join()
    # 由于读进程是死循环，永远不会结束所以等待写进程执行完毕之后强制停止读进程
    r.terminate()
