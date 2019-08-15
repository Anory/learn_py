

class Cat(object):
    tag = "猫科动物"

    def __init__(self, name):
        self.name = name

    @classmethod
    # 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
    def show_info(cls, name):
        return cls(name)
        # 相当于类的实例化最后把传进来的name变量绑定在了类的实例变量上所以后面在调用show_info2 的时候能打印出里面的信息
        # cat = Cat(name)
        # return cat

    def show_info2(self):
        print("类的属性：{0}， 实例的属性：{1}".format(self.tag, self.name))


if __name__ == "__main__":
    # 调用@classmethod(不需要类的实例化，可以直接声明一个变量接收show_info 方法返回的参数)
    cat = Cat.show_info("大黄")
    cat.show_info2()
