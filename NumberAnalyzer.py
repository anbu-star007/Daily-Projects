def is_Even(n):
  if n>0:
    if n%2==0:
        print("The number is even")
    else:        
        print("The number is odd")

def is_prime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                print("The number is not prime")
                break
        else:
            print("The number is prime")
    else:
        print("The number is not prime")

def sum(n):
   if n>0:
    s=0
    while n>0:
       s += n % 10
       n = n//10
    print("The sum of digits is:", s)

def factorial(n):
    if n<0:
        print("Factorial is not defined for negative numbers")
    elif n==0 or n==1:
        print("The factorial of", n, "is 1")
    else:
        fact=1
        for i in range(2,n+1):
            fact=fact*i
        print("The factorial of", n, "is", fact)

n=int(input("Enter a number: "))
is_Even(n)
is_prime(n)
sum(n)
factorial(n) 