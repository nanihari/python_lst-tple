# python_lst-tple
# exercises on lists and tuples, tried to cover all the methods on lists and tuples
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

