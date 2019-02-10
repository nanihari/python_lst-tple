def remove(duplicates):
    final_res=[]
    for number in duplicates:
        if number not in final_res:
            final_res.append(number)

    return final_res
print(remove([1,2,4,1,1,1,4,4,4]))

### we can do this by sets
a=[1,2,4,1,1,1,4,4,4]
uni_items=[]
duplicates=set()
for x in a:
    if x not in duplicates:
        uni_items.append(x)
        duplicates.add(x)
print(duplicates)


