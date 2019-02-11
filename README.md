# python_lst-tple
##Read me file will be having all the short cuts and theory about lists, tuples.
##when should we go for lists:
        If we want to represent a group of individual objects as a single entity where insertion order preserved and duplicates are allowed. lists is dynamic as on our requirement we can go for increasing and decreasing of the lists.
### sorting the lists: list1.sort(key = sortSecond) 
## can check the lists is empty or not by membership operators(i.e., not, not in )
## copy the original lists:
    a=[1,2,3,4,5,6]
    copy_list=list(a)
    print(a)    ###[1,2,3,4,5,6]
    print(copy_list)###[1,2,3,4,5,6]
    copy_list.append(6)##[1,2,3,4,5,6,6]
    print(a)###[1,2,3,4,5,6]
###to print a specified list after removing the 0th, 4th and 5th elements.
names=["hari", "krishna", "Iam", "from", "india"]       ### or we can take with pop and remove functions
names=[x for (i,x) in enumerate(names) if i not in (0,4,5)]   #where pop will delete index element and remove will delete specific name
print(names)
## we have a module called shuffle to shuffle the list: shuffle(lst)
###difference between 2 lists:
1 method: we can use sets                                                         
l1=[1,2,3,4]
l2=[1,2,3,4,5,6]
print((list(set(l1))))-(list(set(l2))))
## while inserting an element into lists using insert(), if the index is out of range insertion can be done at the most possible place.
n=[1,2,3,4,5]
n.insert(10,777)##[1,2,3,4,5,777]
n.insert(-10,777)##[777,1,2,3,4,5]
### pop and remove will be deleting elements where as pop will take index element and remove will take element number.
### how to access index in a list:
we have a method called enumerate
l1=[1,2,4,5,6,7]
for number_index, number in enumerate(l1):
    print(number_index, number)
### A string concatination like will be used to append first list to the second list (l1+l2)
###difference b/w append and extend in python is:
  l1=[1,2,3]
  l2=[5,6,7]      ##extend the list with out append:: l1[:0]=l2
  l1.append(l2)    ## print(l1)
  print(l1)
### frequency of elements in a list can be found by collections module
import collections
l1=[1,2,3,1,1,1,4,4,55,5,5]
print(collections.Counter(l1))
##replacement of elements is possible with slice operator as well.
s[:-1]=s2
***************************Tuples*******************************************
### to write a tuple that contain a single value, t1=(10,)
### as the tuples are immutable, changing the tuples can be done by concatination operation and deleting can be done by slicing method or we can change it by converting tuple to list and after deleting an element again to tuple
1. tuple1=(1,2,3,4,5)
tuple[2:]+(7,)+tuple[3:]
##conversion of tuples to string is:
tuples1=("h", "a", "r", "i")
str1="".join(tuples1)
print(str1)
2. tuple=(1,2,3,4,5,6,7)
tuple[0:1]+tuple[2:] ## item 2(1st element will be removed as the slicing operator doesnot include end operator(0:1)
###lists to tuples== tuple(list)
3. tuple1=(1,2,3,4,5,6,7,8)
list1=list(tuple1)
list1.remove(1)
tuple1=tuple(list1)
print(tuple1)
3. elements index can be found using index method
tuple1=("hello world")
print(tuple1.index("h"))
print(tuple1.index("o", 2))## from where you want to check the elements
print(tuple1.index("l", 4, 10))##from 4th to 10th element searching will be done
4. convert tuple in to dictionary
tuple1= ((1, "a"),(2, "b"))
print(dict((y,x) for x, y in tuple1))
just like in lists, reversing can be done with reversed function or slicing [::-1]
1: tuple1=("hari krishna")                      ### print(tuple(tuple1[::-1]))
x=reversed(tuple1)
print(tuple(x))
## remove empty tuples from list of tuples 
x=[(), (), (a,b), (c,g,j), (h,a), (), (), (',), ("")]
x=[t for t in x if t]
print(x)
