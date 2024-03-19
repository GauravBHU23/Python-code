marks = {}

x = int(input("Enter the Number Of Physics:"))
marks.update({"phy" : x})
x = int(input("Enter the Number Of Chemistry:"))
marks.update({"chem" : x})
x = int(input("Enter the Number Of Math:"))
marks.update({"math" : x})

print(marks)
