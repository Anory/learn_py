# 将列表或者元组转换为迭代器

list_1 = [1, 2, 3, 4, 5, 6, 7]
l_1 = iter(list_1)
# 获取迭代器下一个值,迭代完之后再迭代的话会报错
a = l_1.__next__()
a1 = next(l_1)
print(a)
print(a1)


tuple_1 = [1, 2, 3, 4, 5, 6, 7]
t_1 = iter(tuple_1)
b = t_1.__next__()
print(b)
