from functools import reduce

try:

    salaries = input("Enter the salaries separated by space: ").split()

    salaries = list(map(float, salaries))

    high = list(filter(lambda x: x > 50000, salaries))

    total = reduce(lambda x, y: x + y, salaries)

    print("All Salaries:", salaries)
    print("High Salaries:", *high)
    print("Total Salary:", total)

except ValueError:
    print("Invalid input. Please enter valid numbers.")