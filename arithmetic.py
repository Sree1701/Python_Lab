num1=float(input("Enter A:"))
num2=float(input("Enter B:"))
addition=num1+num2
subtraction=num1-num2
multiplication=num1*num2
if num2 != 0:
    division = num1/num2
else:
    division = "Not defined"
print("Addition:",addition)
print("Subtraction:",subtraction)
print("Multiplication:",multiplication)
print("Division:",division)
