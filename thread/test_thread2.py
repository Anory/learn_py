import threading


# 第二种实现线程的方法(面向对象实现)
class LoopThread(threading.Thread):
    n = 0

    def run(self):
        while self.n < 5:
            now_thread = threading.current_thread().name
            print("[loop]now thread name:{}".format(now_thread))
            print(self.n)
            self.n += 1


if __name__ == '__main__':
    """
    通过调用Thread类的start()方法来启动一个线程，这时此线程处于就绪（可运行）状态，并没有运行，一旦得到cpu时间片，
    就开始执行run()方法，这里方法 run()称为线程体，它包含了要执行的这个线程的内容，Run方法运行结束，此线程随即终
    止。通俗的理解为start()方法包含了运行run()方法
    """
    now_thread = threading.current_thread().name
    print("now thread name:{}".format(now_thread))
    t = LoopThread(name="loop_thread_oop")
    t.start()
    t.join()
