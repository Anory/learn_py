import re


# 正则分割(返回列表)
test_str = "one1Tow2three3Four44"
# 以数字作为分割点进行分割
p = re.compile(r"\d+")
rest = p.split(test_str, 2)  # 分割2次（分割次数也可以不填）
print(rest)
