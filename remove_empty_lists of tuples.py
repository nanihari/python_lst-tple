### remove empty tuples from a list of tuples
x=[(), (), ("a", "b"), ("c", "h"), ("l", ),('', )]
x=[t for t in x if t]
print(x)

