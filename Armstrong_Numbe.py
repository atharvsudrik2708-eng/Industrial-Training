num = int(input('enter number'))
sum =0
rem =0
org = num

while num > 0:
    rem = num  % 10
    sum = sum + rem ** 3
    num = num // 10
 
if org == sum:
    print ("Armstrong number")
else :
    print("Not Armstrong number") 