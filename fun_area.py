def square(s):
    return s*s
def rect(l,b):
    return l*b
def tri(b,h):
    return 0.5*b*h

s=float(input("Square Side:"))
l=float(input("Rectangle Length:"))
b=float(input("Rectangle Breadth:"))
bt=float(input("Triangle Base:"))
h=float(input("Triangle Height:"))
print("Square area:",square(s))
print("Rectangle area:",rect(l,b))
print("Triangle area:",tri(bt,h))

