

class ShortInputException(Exception):
    """
    自定义异常类
    """
    def __init__(self, length, atleast):
        self.length = length
        self.atleast = atleast


def test_main():
    """
    触发并捕获异常
    :return:
    """
    text = "abc"
    try:
        if len(text) < 5:
            raise ShortInputException(len(text), 5)
    except ShortInputException as e:
        print("ShortInputException:输入长度为{}，应该输入的长度为{}".format(e.length, e.atleast))
    finally:
        print("当前输入的字符是{}".format(text))


test_main()
