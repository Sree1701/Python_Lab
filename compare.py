def compare(S1,S2,n):
    if S1[:n]==S2[:n]:
        return True
    else:
        return False
S1=input("Enter First string:")
S2=input("Enter Second string:")
n=int(input("Enter number of character to compare:"))
result=compare(S1,S2,n)
if result:
    print("The First ",n,"characters are the same.")
else:
    print("The First ",n,"characters are different.")

