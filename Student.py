a=int(input("Tamil:"))
b=int(input("English:"))
c=int(input("Mathematics:"))
d=int(input("Science:"))
e=int(input("Social Science:"))
total=a+b+c+d+e
print("Total",total)
average=total/5
print("Average Percentage:",average,"%")
if(average<35):
 print("Arrear")
elif(average>=35 and average<=40):
 print("Pass")
elif(average>40 and average<=60):
 print("Good")
elif(average>60 and average<=70):
 print("Better")
elif(average>70 and average<=80):
 print("Excellent")
elif(average>80 and average<=100):
 print("Extraordinary")