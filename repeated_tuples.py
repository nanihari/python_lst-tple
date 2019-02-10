### find the repeated elements in a tuple
from collections import Counter
a=(1,2,3,4,5,6,7,8,9,1,1,1,2,2,2,3,3)
print(Counter(a))
print(5 in a)## check 5 exists in a or not
print("s" in a)
