

# 面向对象编程
class IterRange(object):
    """
    用迭代器实现range方法
    """
    def __init__(self, start, end):
        self.start = start - 1
        self.end = end

    def __next__(self):
        self.start += 1
        if self.start >= self.end:
            raise StopIteration
        return self.start

    def __iter__(self):
        return self


# 面向过程编程
def generator_range(start, end):
    """
    生成器实现range方法
    """
    start -= 1
    while True:
        if start >= end - 1:
            break
        start += 1
        yield start


if __name__ == "__main__":
    # rest = IterRange(5, 10)
    # for i in rest:
    #     print(i)
    gen = generator_range(5, 10)
    for i in gen:
        print(i)
