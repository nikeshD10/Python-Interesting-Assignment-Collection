def quad_eqn():
    print("Compare the Quadratic Equation with ax^2 + bx + c.")
def roots(a, b, c):
    D = (b**2 - 4*a*c)**0.5
    r_1 = (-b+D)/(2*a)
    r_2 = (-b-D)/(2*a)
    print("x1: {0}".format(r_1))
    print("x2: {0}".format(r_2))
if __name__ == "__main__":
    quad_eqn()
    a = input("Enter the value of a: ")
    b = input("Enter the value of b: ")
    c = input("Enter the value of c: ")
    roots(int(a), int(b), int(c))

