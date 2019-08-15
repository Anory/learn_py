class Cat(object):
    """
    类的继承,定义父类（基类）
    子类继承父类时可以增加新的方法或属性，也可以使用父类的，但是不能选择性的继承父类
    """
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("猫都要吃东西")

    def eat2(self):
        print("是他们的爷爷")


class PetCat(Cat):
    """
    继承父类Cat
    """
    def eat(self):
        """
        继承父类方法并添加自己的代码
        :return:
        """
        super().eat()
        print("猫还喜欢吃鱼")


class PastoralCat(PetCat):
    """
    田园猫继承PetCat
    """
    def eat(self):
        # super(PastoralCat, self).eat()  = super().eat() 可省略里面的内容
        super().eat()
        print("还喜欢吃零食")


class ShortCat(PetCat):
    """
    英短继承PetCat
    """
    def eat(self):
        # 在新的基类中有和父类一样的方法的时候叫重写父类方法/重载父类方法，可以说重写的方法不调用父类的方法的话就不会包含
        # 父类中被重写方法的功能
        """
        子类中没有调用父类的方法也可以称为方法重写。当父类的方法不符合子类的实物的行为时，都可对其进行重写，
        可在子类中定义一个这样的方法，即它与要重写的父类方法同名。这种子类包含与父类同名的方法的现象被称为方
        法重写，也被称为方法覆盖。可以说子类重写了父类的方法，也可以说子类覆盖了父类的方法。
        不显示调用当前类的父类的时候就不能调用父类的方法
        :return:
        """
        print("什么都喜欢吃")


if __name__ == "__main__":
    cat = PastoralCat("小白")
    cat.eat()
    print("=================")
    cat_s = ShortCat("小黑")
    cat_s.eat()
    # 当前类没有对应的方法的情况下会一直往它的父类找，找到就正常运行，父类也没有对应方法的情况下会报错
    cat_s.eat2()

    # 子类的判断     isinstance()方法判断实例
    print(issubclass(ShortCat, Cat))
