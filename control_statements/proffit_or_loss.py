cost_price = float(input("Enter the Cost Price:"))
selling_price = float(input("Enter the selling Prcie:"))

if (selling_price > cost_price):
    print("profit is ", selling_price - cost_price)
else:
    print("loss is ", cost_price - selling_price)   