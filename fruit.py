def print_list(list,idx=0):
    if(idx == len(list)):
       return
    print(list[idx])
    print_list(list,idx+1)

fruit = ["Banana","Apple","Papaya","Guava","Litchi","Orange"]
print_list(fruit)
