'''
1. if student is not registred then access is denied 
  
   -if student is registred and fee not paid then access denied
   -if student is registred, fee is paid and time is valid then exam started
   -othewise exam is not stareted

'''

reg = input("Are you registered for the Exam? Enter yes/not -")
fee = input("Are you pay your Fee? Enter yes/not -")
curr_time = float(input("Enter Current Time (24 hours):-"))

if (reg == "yes"):

    if(fee != "yes"):
        print("Access Denied")

    elif(fee == "yes"  and  (curr_time > 10.00 and curr_time <= 17.00)):
        print("Exam started....")
    
else:
    print("Access Denied")
    