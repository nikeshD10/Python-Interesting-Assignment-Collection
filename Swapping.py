#swapping the number
"""
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
if a > b:
    a = a + b
    b = a - b
    a = a - b
    print("After Swapping:\n ")
    print("The value of a: ", a)
    print("The value of b: ", b)
if a == b:
    print("Sorry the Value of two elements is same. Please select a different number.")

if a < b:
    b = a + b
    a = b - a
    b = b - a
    print("After Swapping:\n ")
    print("The value of a: ", a)
    print("The value of b: ", b)
"""



                            # Anothe method using the third elements:

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
x = b
b = a
a = x
print("After swapping: ")
print("Thw value of a: ", a)
print("The value of b: ", b)

