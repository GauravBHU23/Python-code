nums = (1,4,9,16,25,36,49,64,81,100)
x =36
i = 1
while i <len(nums):
    if(nums[i]==x):
        
        print("Finding the Number is :",i)
        break
    else:
        print("Not a find number")
        i +=1
print("end of loops")