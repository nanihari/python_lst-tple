## find the second largest, largest, second smallest and smallest in a list
def find_slssmsl(list1):
    length=len(list1)
    list1.sort()
    print(list1)
    print("largest element is:", list1[-1])
    print("second largest is:", list1[-2])
    print("second smallest is:", list1[1])
    print("smallest is:",list1[0])
list1=[1,24,34,68,90,12,45,78,24]
print(find_slssmsl(list1))
