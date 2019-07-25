# 生成器是一个特殊的迭代器也可以用next()和__next__()以及遍历方法
def pow():
    yield 1
    yield 2
    yield 3
    yield 4


def pow_num():
    for i in range(5):
        yield i * i


if __name__ == "__main__":
    # rest = pow()
    # print(rest.__next__())
    # print(rest.__next__())
    # print(next(rest))
    # print(next(rest))
    # for i in rest:
    #     print(i)
    rest = pow_num()
    for i in rest:
        print(i)
