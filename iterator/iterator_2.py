

class Iterator(object):
    """
    创建一个迭代器的类
    1、类中实现__iter__( )方法和__next__( )方法：我们只要在自定义的类中实现了这两个方法，这个类的实例对象就是迭代器，
    不仅可以用for ... in循环，也可以用next( )遍历。
    2、iter( )函数：iter( )函数可用来返回一个迭代器对象，iter( )函数只传入一个参数时，参数必须为可迭代对象
    （list、tuple、str等）。
    """
    value = 0

    def __next__(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value * self.value

    def __iter__(self):
        return self


if __name__ == "__main__":
    # 实例生成一个迭代器
    pow = Iterator()
    # pow是可遍历的迭代器，for循环默认执行next()方法
    for i in pow:
        print(i)
