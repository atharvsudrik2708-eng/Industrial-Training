'''wap to calculate discount on product .
if price > 5000  and price <= 10000 then discount is 5% 
if price > 10000 and price <= 50000 then discount is 10% 
if price > 50000 then discount is 20%
else no discount. find final price after discount
'''
dis=0
price = float(input("Enter the price: "))

if(price>5000 and price<= 10000):
    dis = price * 5/100
    print("Final price after discount is ", price-dis)

elif(price>10000 and price <= 50000):
    dis = price * 10/100
    print("Final price after discount is ", price-dis)

elif(price>50000):
    dis= price * 20/100
    print("Final price after discount is ", price-dis)

else:
    print("No discount. Final price is ",price- dis)


print("Discount is",dis)

    
    

