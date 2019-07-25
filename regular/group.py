import re


def test_group():
    test_str = "hello, world"
    test = re.compile(r"world")
    rest = test.search(test_str)
    # 如果rest对象存在就执行if分支里面的代码（使用group的时候需要注意，因为没有匹配对象的情况调用group的话会报错）
    if rest:
        # group 方法里面的num 参数是需要正则有分组的情况下才能使用的，正则没有分组的话就不用传参直接调用就好了
        print(rest.group())  # 打印匹配成功的字符串
        # 因为正则没有写分组所以打印的是空元组
        print(rest.groups())


def test_id_card():
    test_id = "450922199204230492"
    test1 = re.compile(r"(\d{6})(\d{4})((\d{2})(\d{2}))(\d{3})([0-9]|X)")
    # 分组命名
    test2 = re.compile(r"(?P<number>\d{6})(?P<years>\d{4})((?P<month>\d{2})(?P<day>\d{2}))(\d{3})([0-9]|X)")
    rest =test2.search(test_id)
    if rest:
        # 正则里面有分组所以可以添加num参数
        print(rest.group(1))
        # 因为正则有写分组所以返回的是分组的元组
        print(rest.groups())
        # 打印分组命名的匹配数据
        print(rest.groupdict())


if __name__ == "__main__":
    test_group()
    test_id_card()
