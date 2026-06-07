''' 
wap to enter numbers till user wants and at the end it should display sum of all the numbers entered.
'''
sum = 0
num = 0

while(True):
    msg = input("Do you Want to Enter Number.(yes / no):")

    if( msg == "yes"):
        num = int(input("Enter number:"))
        sum = sum + num
    else:
        print(f"Sum of Entered Numbers are {sum}")
        break

