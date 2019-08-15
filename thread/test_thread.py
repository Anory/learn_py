# 实现线程的第一种方式
import threading


def loop():
    n = 0
    while n < 5:
        # 通过对象的name属性获取当前线程的名字
        now_thread = threading.current_thread().name
        print("[loop]now thread name:{}".format(now_thread))
        print(n)
        n += 1


def test_loop():
    now_thread = threading.current_thread().name
    print("now thread name:{}".format(now_thread))
    # 创建子线程loop_thread，子线程运行loop函数里面的代码
    t = threading.Thread(target=loop, name="loop_thread")
    t.start()
    t.join()


if __name__ == '__main__':
    test_loop()
