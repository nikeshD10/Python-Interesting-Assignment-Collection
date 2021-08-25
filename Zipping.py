"""Write a program that combines two lists of equal length by alternatingly
taking elements, e.g.
[‘a’, ‘b’, ‘c’], [1, 2, 3] -> [‘a’, 1, ‘b’, 2, ‘c’, 3]"""

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
zipped = list(zip(list1, list2))
print(zipped)

list3 = []
for(l1, l2) in zip(list1, list2):
    list3.append(l1)
    list3.append(l2)
print(list3)