class PetCat(object):
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if not isinstance(new_age, int):
            print("年龄必须是整数")
            return 0
        if new_age < 0 or new_age > 100:
            print("数值错误")
            return 0
        self.__age = new_age

    @property   # 将类的方法变成属性来调用
    def show_info(self):
        return "我叫{}，我今年{}岁".format(self.name, self.age)

    # 直接返回一个类的描述信息
    def __str__(self):
        return "这是一个猫类"


if __name__ == "__main__":
    cat = PetCat("小白", 4)
    # print(cat)
    # print("===================")
    # print(cat.show_info)
    # print("======================")
    cat.age = 800
    print(cat.show_info)

