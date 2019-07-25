class PetCat(object):

    # 原定义好的实例属性不希望在实例化之后被随意修改可以用slots
    __slots__ = ("name", "age")

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property   # 将类的方法变成属性来调用
    def show_info(self):
        return "我叫{}，我今年{}岁".format(self.name, self.age)

    # 直接返回一个类的描述信息
    def __str__(self):
        return "这是一个猫类"


# 子类继承父类也会继承slots的方法，只允许修改和访问原来定义好的属性
class HuaCat(PetCat):
    # 在父类原来的属性的基础上再加上自定义属性
    __slots__ = ("color")
    pass


def eat():
    print("猫喜欢吃鱼")


if __name__ == "__main__":
    # cat = PetCat("小白", 4)
    # print(cat.show_info)
    # # 给cat实例添加新的属性
    # cat.color = "白色"
    # print(cat.color)
    # # 给cat实例添加新的方法/函数
    # cat.eat = eat
    # cat.eat()

    # # 使用slots之后不允许给实例添加新的属性
    # cat.color = "白色"
    #
    # # 使用slots之后不允许给实例添加新的方法
    # cat.eat = eat
    # cat.eat()

    white_cat = HuaCat("小白", "3")
    print(white_cat.show_info)
    # 子类已添加了color属性所以可以再添加新的属性
    white_cat.color = "白色"
    print(white_cat.color)
    # 修改实例变量
    white_cat.name = "白白"
    print(white_cat.show_info)

