
class Point(object):
    # 自定义Point类的构造(初始化)方法
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # 自定义Point类对象的格式化输出函数(string())

    def string(self):
        print("{X:{0,Y:{1}}", format(self.x, self.y))


class Circle(Point):
    # 自定义Circle类的构造(初始化)方法/重新父类构造方法
    def __init__(self, x, y, radius):
        # 子类调父类的三种方法
        # super().__init__(x, y)
        # super(Circle, self).__init__(x, y)
        Point.__init__(self, x, y)
        self.radius = radius
    # 自定义Circle类对象的格式化输出函数(string())

    def string(self):
        print("该图形初始化点为：{{X:{0},Y:{1}}};{{半径为：{2}}}".format(self.x, self.y, self.radius))


class Size(object):
    # 自定义Size类的构造(初始化)方法
    def __init__(self, width, height):
        self.width = width
        self.height = height
    # 自定义Size类对象的格式化输出函数(string())

    def string(self):
        print("{Width：{0}, Height：{1}}".format(self.width, self.height))


class Rectangle(Point, Size):
    # 自定义Rectangle类的构造(初始化)方法，并在方法中调用父类的初始化方法以完成初始化
    def __init__(self, x, y, width, height):
        Point.__init__(self, x, y)
        Size.__init__(self, width, height)
    # 自定义Rectangle类对象的格式化输出函数(string())

    def string(self):
        print("该图形初始化点为：{{X：{0}, Y：{1}}}; 长宽分别为：{{Width：{2}, Height：{3}}}".format(self.x, self.y,
                                                                                  self.width, self.height))


if __name__ == "__main__":
    # 实例化Circle对象，圆心为（5,5），半径为8
    c = Circle(5, 5, 8)
    c.string()
    # 实例化Rectangle对象，顶点位置（15,15），长和宽分别为15和15
    r1 = Rectangle(15, 15, 15, 15)
    r1.string()
    # 实例化Rectangle对象，顶点位置（40,30），长和宽分别为11和14
    r2 = Rectangle(40, 30, 11, 14)
    r2.string()
