import re

# 将正则表达式 "^1([2-9]{2})([0-9]{4})([0-9]{4})" 进行编译，返回一个正则表达式的对象（re.I 表示正则表达式不区分大小写的匹配）
# 在以后的工作中推荐对正则进行编译之后在进行调用（可以提升一些运行的速度）
pattern = re.compile(r"^1([2-9]{2})([0-9]{4})([0-9]{4})", re.I)
# 通过dir方法查看对象里面的信息或者可用的函数/方法
print(dir(pattern))

# 在通过match方法进行匹配，返回匹配的对象，没有匹配上就返回一个None
rest = pattern.match("13265556550")
print("匹配成功的对象信息：", rest)