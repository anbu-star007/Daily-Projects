emails=set()

while True:
    print("1.Enter Email")
    print("2.View Registered Emails")
    print("3.Remove Email")
    print("4.Exit")

    choice=int(input("Enter Choice: "))

    if choice==1:
        email=input("Enter Email:")
        if email in emails:
            print("Email already registered")
        else:
            emails.add(email)
            print("Email registered successfully")

    elif choice==2:
        print("Registered Emails:")
        for email in emails:
            print(email)

    elif choice==3:
        email=input("Enter Email to remove:")
        if email in emails:
            emails.remove(email)
            print("Email removed successfully")
        else:
            print("Email not found")

    elif choice==4:
        break
    
    else:
        print("Invalid choice")