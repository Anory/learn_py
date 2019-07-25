class Cat(object):
    # 类自定义属性
    tag = "这是一个猫科动物"

    def __init__(self, name, age):
        # 对象自定义属性（针对实例化对象）
        self.name = name
        # 定义私有属性外部不能直接访问
        self.__age = age

    # 外部无法直接访问私有属性所以需要提供一个获取私有属性的方法给外部调用
    def get_age(self):
        return self.__age

    # 由于外部无法直接修改私有属性，所以需要提供一个修改私有属性的方法给外部调用修改
    def set_age(self, new_age):
        self.__age = new_age

    def catch(self):
        print("猫可以抓老鼠")

    def eat(self):
        print("猫可以吃东西")

    def get_cat_info(self):
        print("{}的年龄是{}岁".format(self.name, self.__age))


if __name__ == "__main__":
    # 类的实例化对象，将变量指向给了cat对象， 谁实例化了对象self就指向谁
    cat = Cat("小黑", 2)
    # 不是私有属性可以直接访问
    print(cat.name)
    # print(cat.age)  # 不能直接访问私有变量和直接外部修改变量
    # 调用set_age()方法访问age变量
    print(cat.get_age())
    cat.get_cat_info()
    # 修改不是私有属性
    cat.name = "小白"  # 不是私有属性可以直接修改
    cat.get_cat_info()
    # 调用修改私有属性的方法进行修改
    cat.set_age(5)
    cat.get_cat_info()
