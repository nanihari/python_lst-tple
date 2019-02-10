##program to sort a tuple by its float element.
items = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print(sorted(items, key = lambda x: float(x[1]), reverse = True))
