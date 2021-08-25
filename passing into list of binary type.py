
a = ["1", "1", "0", "0", "1"]
b = ["1", "0", "0", "0", "1", "0"]

a1 = list(int(x, 2) for x in list(a))
print(a1)


for i in a:
    print(i)