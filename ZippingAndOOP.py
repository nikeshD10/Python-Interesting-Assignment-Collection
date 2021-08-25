list1 = [1, 2, 3, 4, 5]
list2 = ["one", "two", "three", "four", "five"]

zipped = list(zip(list1, list2))
print(zipped)


unzipped = list(zip(*zipped))
print(unzipped)




class car():
    def __init__(self, name, speed, horsepower, color):
         self.name = name
         self.speed = speed
         self.horsepower = horsepower
         self.color = color
    def sentence(self, show):
         if show:
             print("The car named as %s has the speed of %s with horsepower %s which has color %s." %(self.name, self.speed, self.horsepower, self.color))
         else:
             print("Sorry the value is not true")
car1 = car("mercides", 200, 1000, "black")
car1.sentence(show=False)

