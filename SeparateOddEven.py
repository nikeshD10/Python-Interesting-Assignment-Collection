"""a = [2, 3, 6, 8, 9, 12, 15, 18, 24, 22, 33, 112]

for i in a:
    if i % 2 == 0 and i % 3 == 0:
        print(i)"""



n = [43, 23, 21, 44, 56, 75]
odd_i = []
even_i = []
for i in range(0, len(n)):
    if i % 2:
        even_i.append(n[i])
    else:
        odd_i.append(n[i])
print(odd_i)


