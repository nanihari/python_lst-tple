##program to check if all dictionaries in a list are empty or not.
l=[{},{1},{1,2}]
l2=[{},{},{}]
print(all(not d for d in l))
print(all(not d for d in l2))

