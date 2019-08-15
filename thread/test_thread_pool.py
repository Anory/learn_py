import time
import threading
from concurrent.futures import ThreadPoolExecutor
from multiprocessing.dummy import Pool


def run(n):
    print(threading.current_thread().name, n)


# 线程池第一种实现方法(方便管理线程以及合理分配资源，做到线程的复用)
def use_pool():
    t1 = time.time()
    n_list = range(1000)
    pool = Pool(10)  # 线程池里面设置10个线程(允许系统最多同时运行10个线程)
    pool.map(run, n_list)  # 参数：需要运行的方法， 被运行方法里面的参数（参考map方法）
    pool.close()
    pool.join()
    print(time.time() - t1)


# 第二种实现方法
def use_executor():
    t1 = time.time()
    n_list = range(1000)
    # 用with 方法实现先执行完线程再打印时间差
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(run, n_list)
    print(time.time() - t1)


if __name__ == '__main__':
    # use_pool()
    use_executor()