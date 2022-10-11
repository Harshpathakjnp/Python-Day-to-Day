class Students:
    def __init__(self,name,roll):
        self.name = name
        self.roll_Number = roll
    def printStudent(self):
        print("My Name is ",self.name ,"and my roll Number is ",self.roll_Number)

s1 = Students("Harsh",38)
s2 = Students("Abhishek",12)
Students.printStudent(s1)