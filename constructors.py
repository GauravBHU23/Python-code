class Student:
  college_name = "Bhu College"
  name = "anonymous"

  def __init__(Self,fullname,marks):
      Self.name = fullname
      Self.marks = marks
      print("Adding a new Student in database..")
s1 = Student("Gaurav",97)
print(s1.name,s1.marks)
s2 = Student("Saurav",90)
print(s2.name,s2.marks)
print(s2.college_name)
print(Student.college_name)
print(s1.name)