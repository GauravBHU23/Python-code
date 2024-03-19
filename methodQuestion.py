class Student:
    def __init__(self,marks,name):
        self.name = name
        self.marks = marks
        
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum  += 8
        print("Hii", self.name, "Your Avg Score is:", sum/3)

s1 = Student("Gaurav saurav", [45,67,98])
s1.get_avg()

