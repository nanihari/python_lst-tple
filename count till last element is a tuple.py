##program to count the elements in a list until an element is a tuple.
num=[10,20,30,(10,30),40]
count=0
for n in num:
    if isinstance(n,tuple):##The isinstance() function checks if the object (first argument) is an instance or subclass of classinfo class (second argument).
        break
    count+=1
print(count)

