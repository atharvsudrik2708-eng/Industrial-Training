n = int(input("enter any number:"))
sum = 0

if(n % 2 != 0):
    n = n-1

while(n>0):
    sum = sum + n
    n -= 2

print("sum is ",sum)    



