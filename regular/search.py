import re


test_str = "hello World"
# 使用search
test = re.compile(r"world", re.I)
s_rest = test.search(test_str)
print(s_rest)

# 使用match
m_rest = test.match(test_str)
print(m_rest)

# search 和 match 的区别：search会从第一个字符开始匹配，匹配上之后就返回一个匹配成功的对象，如果匹配完字符串之后还是没有
# 匹配上的就会直接返回None， match直接匹配第一个字符串，没有匹配上就直接返回None，匹配上就返回一个对象（查找方式不同）
