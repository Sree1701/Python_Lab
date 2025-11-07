from Armstrong import is_armstrong
low = int(input("Enter lower limit:"))
high = int(input("Enter upper limit:"))
print(f"Armstrong number between {low} and {high}:")
for i in range(low,high+1):
    if is_armstrong(i):
        print(i)
