n = int(input("Enter The Value of n: "))

def natural(n):
    if(n==0):
      return 0
    return natural(n-1) + n
print(natural(n))
