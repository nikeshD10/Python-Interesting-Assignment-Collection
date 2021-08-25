marksDetail=[["name","maths","english","physics","computer","nepali"],
             ["john",88,86,76,66,76],
             ["sam",77,67,87,67,56],
             ["anna",67,65,67,76,65],
             ["ben",87,78,67,77,57],
             ["jeff",90,80,79,88,70]]
for i in range(1,len(marksDetail)):
    totalMarks=0
    for j in range(1,len(marksDetail[i])):
        totalMarks+=marksDetail[i][j]
        
print(marksDetail[i][j])
print("Average of",marksDetail[i][0],"is:",totalMarks/(len(marksDetail[i])-1))
