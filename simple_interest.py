def calculate_simple_interest(principle,time,is_senior_citizen):
    if is_senior_citizen:
        rate=12
    else:
        rate=10
    interest=(principle*rate*time)/100
    return interest
principle=float(input("Enter the principle amount:"))
time=float(input("Enter the time(in years):"))
age=int(input("Enter your age:"))
is_senior_citizen = age>=60
interest = calculate_simple_interest(principle,time,is_senior_citizen)
print(f"\nSimple Interest = {interest:.2f}")
<<<<<<< HEAD
=======

>>>>>>> bff5627974ac07c8a1ff4e7bcc5a041663087ef2
