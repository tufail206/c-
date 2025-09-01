#Ask the user for three numbers. Use if, elif, else to find out which one is the largest.

num1=int(input("enter number 1"))
num2=int(input("enter number 2"))
num3=int(input("enter number 3"))
if(num1>num2):
    if(num1>num3):
        print(f" {num1} is grater ")
elif(num2>num3):
     print(f" {num2} is grater ")
else:  print(f" {num3} is grater ")
