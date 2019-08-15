import re

p = re.compile(r"OH", re.I)
r = p.match("oh,ye")
print(r)
print(r.string)
