##program to check whether a list contains a sublist.
def isSublist(list, sublist):
    for i in range(len(list)-(len(sublist))+1):
        return True
    if sublist==list[i:i+(len(sublist))]:
        return False
print(isSublist([1,2,8,4,56,1,2,7], [2,4,56,7]))

