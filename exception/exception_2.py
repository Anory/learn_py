"""
自定义异常
"""


class ApiException(Exception):
    """
    自定义异常类，继承Exception父类
    """
    # 定义两个默认参数
    err_code = ""
    err_msg = ""

    def __init__(self, err_code=None, err_msg=None):
        """
        :param err_code:错误码
        :param err_msg:错误信息
        """
        # 是对实例属性err_code进行快速赋值，首先判断当前实例中是否具有对应的err_code属性值，若有，则将该值赋予当前实例；若没有，则将当前实例初识化时传入的参数err_code赋予当前实例
        # 如果类变量err_code有值就用类变量的值， 如果没有就用传入的 err_code
        self.err_code = self.err_code if self.err_code else err_code
        self.err_msg = self.err_msg if self.err_msg else err_msg

    # 返回对象的描述信息
    # 当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
    def __str__(self):
        return "错误码：{0} -- 错误信息msg：{1}".format(self.err_code, self.err_msg)


class PramsException(ApiException):
    """
    继承ApiException异常类，默认继承ApiException的所以功能
    """
    err_code = "40003"
    err_msg = "除数不能为0"


# 触发异常
def div_num(num1, num2):
    # 两个数必须为整数
    # 如果其中一个数不是整数就触发自定义异常类
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise ApiException("40001", "两个数必须为整数")
    # 除数不能为0
    elif num2 == 0:
        raise PramsException()
    return num1 / num2


if __name__ == "__main__":
    # 调用触发异常的方法捕获异常并打印异常信息
    # 异常捕获从小到大 PramsException 是 ApiException 的子类，好处是方便排查问题
    try:
        div = div_num(4, 0)
        print(div)
    except PramsException as e:
        print("参数错误")
        # 打印异常类中 __str__() 魔法方法中返回的信息
        print(e)
    except ApiException as e:
        print("出错了")
