numbers=input("Enter number separated by space:")
num_list=[int(x) for x in numbers.split()]
odd_list=[num for num in num_list if num%2!=0]
print("Original List:",num_list)
print("List after removing even numbers:", odd_list)
