###Write a Python program to flatten a shallow list.
import itertools
l1=[[2,4,3],[1,5,6], [9], [7,9,0]]
l2=list(itertools.chain(*l1))
print(l2)

