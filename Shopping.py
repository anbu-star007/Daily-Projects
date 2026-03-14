cart=[]

while True:
    print("1.Add Item")
    print("2.View Cart")
    print("3.Remove Item")
    print("4.Total Bill")
    print("5.Exit")

    choice=int(input("Enter Choice: "))
    if choice==1:
        item=input("Enter Item: ")
        price=float(input("Enter Price: "))
        cart.append((item,price))
    
    elif choice==2:
        print("\nCart Items:")
        for i in cart:
            print(i[0],"-",i[1])

    elif choice==3:
        item=input("Enter item to remove: ")
        for i in cart:
            if i[0]==item:
                cart.remove(i)
                print("Item Removed")
                break

    elif choice==4:
        total=0
        for i in cart:
            total+=i[i]
        print("Total Bill:",total)

    elif choice==5:
        print("Thank you for shopping")
        break

    else:
      print("Invalid choice")    

