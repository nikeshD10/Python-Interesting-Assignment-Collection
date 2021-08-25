"""Write a program that performs element-wise addition on 2 lists of
numbers having the same length and outputs another list containing the
sums, e.g.
[1, 2, 3, 4, 5, 6] + [1, 2, 3, 4, 5, 6] -> [2, 4, 6, 8, 10, 12]"""


list1 = [1, 2, 3, 4, 5, 6]
list2 = [1, 2, 3, 4, 5, 6]
list3 = []
for x in range(0, len(list1)):
     list3.append(list1[x] + list2[x])
print(list3)



