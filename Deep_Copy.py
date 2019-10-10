"""
When a deep copy in Python creates a new object, it inserts into the new object copies of the objects in the original
object. In other words, it copies an object into another. This means any changes we make to the copy do not reflect
in the original.
"""

import copy

list1 = [1, 2, 3, 4, 5]

print(list1)
list2 = copy.deepcopy(list1)
list1.append(11)
list1[0] = 9
list2.append(10)
print("List2: ", list2)
print("List1: ",list1)
