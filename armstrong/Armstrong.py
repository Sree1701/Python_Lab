def is_armstrong(n):
    num = n
    s = 0
    d = len (str(n))
    while(n>0):
        r=n%10
        s +=r**d
        n//=10
    return s == num

