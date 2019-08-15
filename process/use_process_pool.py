from multiprocessing import current_process, Pool
import random
import time


def run(file_name, num):
    with open(file_name, "a+", encoding="utf-8") as f:
        # 实例current_process()用以获取进程名字和id
        now_process = current_process()
        content = "进程名字：{}，进程id：{}，序号：{}".format(now_process.name, now_process.pid, num)
        f.write(content)
        f.write("\n")
        time.sleep(random.randint(1, 3))
        print(content)
    return "OK"


if __name__ == '__main__':
    f_name = "pool.txt"
    # 创建进程池
    pool = Pool(2)
    for i in range(10):
        rest = pool.apply(run, args=(f_name, i))
        print("{}----{}".format(i, rest))
    # 关闭池子，防止继续添加进程任务
    pool.close()
    # 等待所有子进程结束再结束主进程
    pool.join()

