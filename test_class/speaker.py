class People(object):
    # 重写People类的构造方法，并将参数n、a赋值给实例属性name、age
    def __init__(self, n, a):
        self.name = n
        self.age = a

    # 自定义实例方法speak（），实现格式化输出
    def speak(self):
        print("{}说:我{}岁".format(self.name, self.age))


class Speaker(object):
    # 重写Speaker类的构造方法，并将参数n、c、t赋值给实例属性name、career、topic
    def __init__(self, n, c, t):
        self.name = n
        self.career = c
        self.topic = t

    # 自定义实例方法speak（），实现格式化输出
    def speak(self):
        print("我叫{},我是一个{},我演讲的主题是{}".format(self.name, self.career, self.topic))


class Student(Speaker, People):
    pass


s = Student('Jonh', '演说家', 'Python')

# s对象调用父类的speak( )方法
s.speak()
# 格式化打印Student是否为Speaker的子类
print(issubclass(Student, Speaker))
# 格式化打印Student是否为People的子类
print(issubclass(Student, People))
