contacts={}

print("1.Add Contact")
print("2.View Contacts")
print("3.Search Contact")
print("4.Delete Contact")
print("5.Exit")
while True:
  print("Enter Choice: ")
  choice=int(input())

  if choice==1:
    name=input("Enter Name: ")
    phone=input("Enter Phone Number: ")
    if name in contacts:
        print("Contact already exists")
    else:
        contacts[name]=phone
        print("Contact added successfully")

  elif choice==2:
    if contacts:
     print("Contacts:")
     for name, phone in contacts.items():
        print(f"{name}: {phone}")
    else:
       print("Contact not found")

  elif choice==3:
   name=input("Enter Name to search: ")
   if name in contacts:
      print(name,":",contacts[name])
   else:
      print("Contact not found")

  elif choice==4:
   name=input("Enter Name to delete: ")
   if name in contacts:
      del contacts[name]
      print("Contact deleted successfully")
   else:
      print("Contact not found")

  elif choice==5:
   print("Exiting contact book....")
   break

  else:
   print("Invalid choice") 
