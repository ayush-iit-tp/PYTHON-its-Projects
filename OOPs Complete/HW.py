
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0
        for mark in self.marks:
            sum += mark
        print("Hi...", self.name,"!. Your average score is:",sum/3)

s1 = Student("Tony Stark", [99,98,94])
s1.get_avg()
s1.name = "Iron Man"
s1.get_avg()
s2 = Student("Bruce Banner", [99,100,98])
s2.get_avg()