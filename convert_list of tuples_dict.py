lst=[("x", 1), ("x", 2), ("x", 3), ("y", 12), ("y", 13), ("y",45), ("z", 34), ("z",67)]
d={}
for a,b in lst:
    d.setdefault(a, []).append(b)
print(d)
