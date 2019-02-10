##program to create the clone of a tuple.
from copy import deepcopy
tuple_1=("hari", 123, [], False)
tuplex_clone=deepcopy(tuple_1)
tuplex_clone[2].append(56)
print(tuplex_clone)
print(tuple_1)

