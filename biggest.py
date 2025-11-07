num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))
if num1 == 0 and num2 == 0 and num3 == 0:
    print("All numbers are zero.")
else:
    if num1 >= num2 and num1 >= num3:
        biggest = num1
    elif num1 >= num2 and num1 >= num3:
        biggest = num
    else:
        biggest = num3
        print("The biggest number is:", biggest)

