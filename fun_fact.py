def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
n= int(input("Enter n:"))
s=0
for i in range(1,n+1):
    s+=(i**3)/fact(i)
print("Sum of series:",round(s,2))

