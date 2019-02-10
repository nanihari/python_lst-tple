##to generate & print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).
lst=list()
for i in range(1,31):
    lst.append(i**2)

print(lst[:5])
print(lst[-5:])
