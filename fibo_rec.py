def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
terms = int(input("Enter the number of terms:"))
print("Fibonacci Series:")
for i in range (terms):
    print(fibo(i), end=" ")
print()
<<<<<<< HEAD
=======

>>>>>>> bff5627974ac07c8a1ff4e7bcc5a041663087ef2
