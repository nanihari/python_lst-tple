##program to count the number of elements in a list within a specified range.
def count_of_range(lst,min,max):
    character=0
    for x in lst:
        if min<=x<=max:
            character+=1
    return character
lst=[10,20,20,20,40,40,50,60,70,80,90]
lst2=["a", "b", "c", "d", "e", "f", "g", "d"]
print(count_of_range(lst,20,80))
print(count_of_range(lst2,"c","f"))

