tup = (1,4,9,16,25,36,49,64,81,100,49)
x = 49

idx = 0
for nums in tup:
    if(nums == x):
        print("The Number is found idx.", idx)
        break
    idx += 1
    
