import time
import random
from multiprocessing import Process, Lock


class ProcessLock(Process):
    def __init__(self, file_name, num, lock):
        super().__init__()
        self.num = num
        self.lock = lock
        self.file_name = file_name

    def run(self):
        # 在for循环外面加了进程锁之后，每一个后面的进程需要等前一个进程执行完并释放之后才会执行（可以对比下不加锁的结果）
        try:
            # 添加多个lock.acquire()也会出现死锁
            self.lock.acquire()
            for i in range(5):
                content = "要写入的内容进程名字：{}， 进程id：{}， 进程自定义id：{}\n".format(self.name, self.pid, self.num)
                with open(self.file_name, "a+", encoding="utf-8") as f:
                    f.write(content)
                    time.sleep(random.randint(1, 3))
                    print(content)
        finally:
            # 添加锁之后需要记得释放，不然会出现死锁
            self.lock.release()

        # 可以用with的语法完成添加和释放锁
        # with self.lock:
        #     for i in range(5):
        #         content = "要写入的内容进程名字：{}， 进程id：{}， 进程自定义id：{}\n".format(self.name, self.pid, self.num)
        #         with open(self.file_name, "a+", encoding="utf-8") as f:
        #             f.write(content)
        #             time.sleep(random.randint(1, 3))
        #             print(content)


if __name__ == '__main__':
    f_name = "test.txt"
    # 也可以用RLock实现多重锁（具体用法看视频）
    lock = Lock()
    for i in range(5):
        p = ProcessLock(f_name, i, lock)
        p.start()
