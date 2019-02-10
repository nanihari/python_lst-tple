##program to find all the values in a list are greater than a specified number.
Lst1=[1,2,3,90,56,99,12,56,89]
lst2=[2,56,78,4,45,78,12,56,89]
print(all(x>=12 for x in Lst1))
print(all(x>=45 for x in lst2))


###find out the numbers of elements that are greater than a specified function in list
Lst1=[1,2,3,90,56,99,12,56,89]
n=int(input("enter the number that you want to find out number of items:"))
numbers=[]
for x in Lst1:
    if n<x:
        numbers.append(x)
print(numbers)

