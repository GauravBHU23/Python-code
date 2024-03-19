Student = {
    "name" : "Gaurav Kumar",
    "Subject" :  {
        "phy" : "97",
        "che" : "99",
        "math" : "98"

    }
}
#nested class Dictionary
print(Student)
print(Student["Subject"])
print(Student["Subject"] ["che"])
print(len(Student))
print(list(Student.keys()))
print(Student.values())
print(list(Student.values()))
pairs = list(Student.items())
print(pairs[0])