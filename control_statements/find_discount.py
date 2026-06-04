'''
wap to find discount according to condition -
1. if festival sell is on and user having membership then discount is 30%

   if user having non membership then discount is 20%

2. is festival sell is off and 

   -if user having membership and cart value is >= 5000 then discount is 20%

   -if user having membership and cart value is < 5000 then discount is 10%

   -if user doesn't having membership , else no discount
'''

fes_sale = "on"
mem = input("Do you have a Membership ? y/n - ")
cart_value  = float(input("Enter Cart Value :"))
dis_price = 0

if (fes_sale == "on"):

    if (mem == "y"):
        dis_price = cart_value*0.30
        print("Discounted price:",dis_price)

    else:
        dis_price = cart_value*0.20
        print("Discounted price:",dis_price)

else:

     if (mem == "y" and cart_value >= 5000):
        dis_price = cart_value*0.20
        print("Discounted price:",dis_price)

     elif (mem == "y" and cart_value < 5000):
        dis_price = cart_value*0.10
        print("Discounted price:",dis_price)

     else:
        print("No Discounted")
  
print("Final Price :",cart_value-dis_price)
