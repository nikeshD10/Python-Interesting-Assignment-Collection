print("--------------welcome to marksheet app--------------------------")
name= input("Name of a student : ")
marks1 = int(input("marks obtains in Maths : "))
marks2 = int(input("marks obtains in English : "))
marks3 = int(input("marks obtains in Science : "))
marks4 = int(input("marks obtains in Computer : "))
marks5 = int(input("marks obtains in History : "))

average = (marks1+marks2+marks3+marks4+marks5)/5



print("********************************MARKSHEET*************************")
print("Student NAme:", name)
print("************************************************************")
print("Subject \t\t Total \t\t MarksObtains")
print("************************************************************")
print("Maths \t\t 100 \t\t ", marks1)
print("English \t\t 100 \t\t ", marks2)
print("Science \t\t 100 \t\t ", marks3)
print("Computer \t\t 100 \t\t ", marks4)
print("History \t\t 100 \t\t ", marks5)
print("************************************************************")
print("Your Average marks is : ", average)
print("\t\t Grading \t\t")
if 70 <= average <= 100:
    print("Excellent!!!! its 'A'")
elif 60 <= average <= 69:
    print(" Welldone  its 'B' ")
elif 50 <= average <= 59:
    print("Keep Trying its 'C'")
elif 43 <= average <= 49:
    print(" Need to work hard 'D'")
elif 40 <= average <= 42:
    print("Lots a lots of hardworking should be done 'E'")
elif 0 <= average <= 39:
    print("SORRY !! better luck next time its 'F'")
print("************************************************************")
print("\t\t Thsnk You \t\t")