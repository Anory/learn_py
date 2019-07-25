test_str2 = "hello world"


def f(m):
    return m.group(2).upper() + " " + m.group(1)

a = f(test_str2)
print(a)
