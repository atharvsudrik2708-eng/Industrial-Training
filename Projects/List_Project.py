shopping_list = []
while (True):
    print("-----Shopping List Manager-----")
    print("1.Add Item")
    print("2.Display Items")       
    print("3.Search Items")
    print("4.Remove Item")
    print("5.Count Items")

    choice = int(input("Enter your Choice:"))

    if choice == 1:
        item = input("Enter Item Name:")
        shopping_list.append(item)
        print("Item added Successfully.")

    elif choice == 2:
        print(shopping_list,end=" ")
        
    elif choice == 3:
        search_item = input("Enter Item name to Search :")

        if search_item in shopping_list:
            print("Item Found in Shopping list.")
        else:
            print("Item is not Found in shopping list.")
    
    elif choice == 4:
        remove_item = input("Enter Item name to Remove:")

        if remove_item in shopping_list:
            shopping_list.remove(remove_item)
            print("Item Removed Successfully.")
        else:
            print("Item is not Preasent in shopping list.")

    elif choice == 5:
        tot_items = len(shopping_list)
        print("Total items in shopping List is :",tot_items)

    elif choice == 6:
        print("Exiting Program.")
        break    
    
    else :
        print("Invalid Choice.")
        print("Enter your choice again:")
