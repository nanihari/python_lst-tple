##matching numbers in 2 differenent lists
def matching_lsts(l1,l2):
    result=False
    for x in l1:
        for y in l2:
            if x==y:
                result=True
                return result
l1=[1,2,3,4,5,6,7]
l2=[1,0,9,9,8,8,0]
print(matching_lsts(l1,l2))


