#Ask the user for three numbers. Use if, elif, else to find out which one is the largest.
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

if num1 >= num2 and num1 >= num3:
    print(f"{num1} is the greatest")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is the greatest")
else:
    print(f"{num3} is the greatest")
