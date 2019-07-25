

def test(num1, num2):
    return num1 / num2


def read_file():
    f = open("test.txt", "r")
    try:
        rest = f.read()  # 没有写编码格式参数执行到这里就会报错，不会再执行代码块后续代码print
        print(rest)
    except:  # 捕获到错误并打印提示信息
        print("err")
    finally:  # 执行必须执行的逻辑代码无论前面程序是否报错都会执行这段代码（文件打开之后必须关闭）
        f.close()
        print("文件关闭")


if __name__ == "__main__":
    # 捕获所有异常
    # try:
    #     r = test(5, 0)
    # except:
    #     print("除数不能为0")

    # 捕获指定异常
    # try:
    #     r = test(5, 0)
    # except ZeroDivisionError:
    #     print("除数不能为0")

    # # 捕获多个异常
    # try:
    #     r = test(5, 3)
    #     r = test(5, "e")
    # # 捕获异常信息并自定义命名为 e 最后打印出异常信息，方便排查问题
    # except (ZeroDivisionError, TypeError) as e:
    #     print(e)

    read_file()

