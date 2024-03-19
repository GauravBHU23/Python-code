dict = {
    "Name" : "Gaurav",
    "Cgpa" : 9.6,
    "Marks" : [98,90,88],
    "RollNumber" : 9,
    "idnumber" : 23,
    "age" : 22,
    "Subject" : ["java","C","C++"]




}
print(dict)
print(dict["Name"])
print(dict["age"])
print(dict["Subject"])
dict["Name"] = ["Saurav"]
dict["Surname"] = ["Gaurav"]
print(dict)

null_dict = {}
null_dict["Name"] = "Codingwithgaurav"
print(null_dict)