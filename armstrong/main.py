from Armstrong import is_armstrong
low = int(input("Enter lower limit:"))
high = int(input("Enter upper limit:"))
print(f"Armstrong number between {low} and {high}:")
for i in range(low,high+1):
    if is_armstrong(i):
        print(i)
<<<<<<< HEAD
=======

>>>>>>> bff5627974ac07c8a1ff4e7bcc5a041663087ef2
