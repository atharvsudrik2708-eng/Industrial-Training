'''
wap to calculate electricity bill 
1) if units in 0 to 100 then 2rs per unit is charges
2) if units in 100 to 250 then 4rs per unit is charges
3) if units are > 250 then 6rs per unit is charges
claculate total bill.
'''
curr_readings = int(input("Enter Current Readings:"))
last_readings = int(input("Enter Last Readings:"))
units = curr_readings-last_readings
bill = 0

print("Current Reading:",curr_readings)
print("Last Reading:",last_readings)

if(units>0 and units<=100):
    print("Bill is Rs",units*2)
elif(units>100 and units<=250):
    print("Bill is Rs",units*4)
else:
    print("Bill is Rs",units*6)





