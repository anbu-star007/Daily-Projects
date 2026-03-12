def power(base, exponent):
  
    if exponent == 0:
        return 1
    if exponent < 0:
        return 1 / power(base, -exponent)
    
    return base * power(base, exponent - 1)


base,exponent=map(int,input("Enter base and exponent:").split())
result = power(base, exponent)
print("Result:",result)