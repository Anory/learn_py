import re


# 正则替换
test_str = "one1Tow2three3Four44"
p = re.compile(r"\d+")
# 将数字替换成 @ 符号， 第一个参数可以是字符、正则或者函数
# 替换次数可不填
rest = p.sub("@", test_str)
print(rest)

# 原始替换方式
rest_origin = test_str.replace("1", "@").replace("2", "@").replace("3", "@").replace("44", "@")
print(rest_origin)


# 正则调换字符串收尾位置
test_str2 = "hello world"
p2 = re.compile(r"(\w+) (\w+)")
# 传入正则（分组的位置）
rest2 = p2.sub(r"\2 \1", test_str2)
print(rest2)


# 使用函数配合正则完成字符串位置调换并修改内容
rest3 = p2.sub(lambda m: m.group(2).upper() + " " + m.group(1), test_str2)
print(rest3)
