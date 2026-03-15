students=[]
n=int(input("Enter number of students: "))

for i in range(n):
    name=input("Enter Name: ")
    age=int(input("Enter Age: "))
    marks=int(input("Enter mark: "))

    student=(name,age,marks)
    students.append(student)

print("Student Records")

for s in students:
    print("Name:",s[0],", Age:",s[1],", Marks:",s[2])
