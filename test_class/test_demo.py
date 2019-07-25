from functools import wraps


def log(text=None):
    def decorator(func):
        @wraps(func)  # 将调用装饰器函数的原来文档说明和方法给还原回去
        def wrapper(*args):
            print("{}开始执行程序".format(text))
            print(args)
            rest = func(*args)
            print("{}结束执行程序".format(text))
            return rest
        return wrapper
    return decorator


@log("test")
def test():
    print("starting...........")


@log("add")
def add(a, b):
    """
    计算两个数的总和
    :param a:
    :param b:
    :return:
    """
    return a + b


if __name__ == "__main__":
    # test()
    r = add(5, 6)  # r 接收 wrapper的返回值 rest
    print(r)
