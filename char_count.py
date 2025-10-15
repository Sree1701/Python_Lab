text=input("Enter a String:")
for char in set(text):
    print(f"'{char}':{text.count(char)}")

