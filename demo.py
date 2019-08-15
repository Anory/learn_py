
def fun1(x, *args, **kwargs):
    print("x:", x)
    print("args:", args)
    print("kwargs:", kwargs)


t = (1, 2, 3, 4)
d = {"a": 1, "b": 2, "c": 3}
fun1(10, *t, **d)