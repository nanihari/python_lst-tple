##program to remove key values pairs from a list of dictionaries.
list1= [{'key1':'value1', 'key2':'value2'}, {'key1':'value3', 'key2':'value4'}, {'key3' : 'value4', 'key2' : 'value3'}]
list2=[{k: v for k, v in d.items() if k!="key1" and k!="key2"} for d in list1]
print("new list after deleting a list of dictionaries is:")
print(list2)
