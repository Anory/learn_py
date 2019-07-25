"""
类装饰器，对已写好的类进行功能上的扩充，保持原来的功能不变
"""


# 吃东西装饰器写法一
# def eat(cls):
#     cls.eat = lambda self: print("{}喜欢吃鱼仔".format(self.name))
#     return cls


# # 吃东西装饰器写法二
def f(self):
    print("{}喜欢吃东西".format(self.name))
    print("完美")


def eat(cls):
    cls.eat = f
    return cls


@eat
class Cat(object):
    def __init__(self, name):
        self.name = name

    def play(self):
        pass


if __name__ == "__main__":
    cat = Cat("小黑")
    cat.eat()
