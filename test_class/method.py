

class Cat(object):
    tag = "猫科动物"

    def __init__(self, name):
        self.name = name

    @classmethod
    def show_info(cls, name):
        return cls(name)
        # 相当于类的实例化最后把传进来的name变量绑定在了类的实例变量上所以后面在调用show_info2 的时候能打印出里面的信息
        # cat = Cat(name)
        # return cat

    def show_info2(self):
        print("类的属性：{0}， 实例的属性：{1}".format(self.tag, self.name))


if __name__ == "__main__":
    # 调用@classmethod
    cat = Cat.show_info("大黄")
    cat.show_info2()
