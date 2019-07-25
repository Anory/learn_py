class Vehicle(object):
    # 自定义Vehicle类属性
    trans_type = "SUV"

    # 自定义实例的初始化方法
    def __init__(self, speed, size):
        self.__speed = speed
        self.size = size

    # 自定义实例方法show_info，打印实例的速度和体积
    def show_info(self):
        print("我的所属类型为：{}，速度：{}km/h，体积：{}".format(self.trans_type, self.__speed, self.size))

    # 自定义实例方法move,打印“我已向前移动了50米”
    def move(self):
        print("我已向前移动了500米")

    # 自定义实例方法set_speed，设置对应的速度值
    def set_speed(self, new_speed):
        self.__speed = new_speed

    # 自定义实例方法get_speed，打印当前的速度值
    def get_speed(self):
        print("我的时速为：{}km/h".format(self.__speed))

    # 自定义实例方法speed_up，实现对实例的加速
    def speed_up(self):
        speed2 = self.__speed + 10
        print("我的速度由{}km/h提升到了{}km/h".format(self.__speed, speed2))

    # 自定义实例方法speed_down，实现对实例的减速
    def speed_down(self):
        speed3 = self.__speed - 15
        print("我的速度由{}km/h下降到了{}km/h".format(self.__speed, speed3))

    # 自定义实例方法transport_identify，实现对实例所属类型的判断
    def transport_identify(self):
        if isinstance(self, Vehicle) == 1:
            print("类型匹配")
        else:
            print("类型不匹配")


if __name__ == "__main__":
    tool_1 = Vehicle(20, (3.6, 1.9, 1.75))

    # 调用实例方法 打印实例的速度和体积
    tool_1.show_info()
    # 调用实例方法 实现实例的前移
    tool_1.move()
    tool_1.set_speed(120)
    # 调用实例方法 打印当前速度
    tool_1.get_speed()
    # 调用实例方法 对实例进行加速
    tool_1.speed_up()
    # 调用实例方法 对实例进行减速
    tool_1.speed_down()
    # 调用实例方法 判断当前实例的类型
    tool_1.transport_identify()
