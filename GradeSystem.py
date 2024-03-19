marks = int(input("Enter The Student marks:"))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"
print("The Number of Student Marks Grade: ",grade)

