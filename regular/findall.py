import re

# 找出大小写字母
test_str = "one1Tow2three3Four44"
# 编译正则表达式
p = re.compile(r"[a-z]+", re.I)
# 使用编译的对象
rest = p.findall(test_str)
print(rest)
# 字符拼接
rest1 = "".join(rest)
print(rest1)

# 不用编译
# 直接传入正则表达式、需要被匹配的内容以及模式
all_str = re.findall(r"[a-z]+", test_str, re.I)
print(all_str)
