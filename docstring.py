def add_numbers(* args):
    """
    Adds variable number of integers and return the total
    """
    return sum(args)
print(add_numbers(10,20))
print(add_numbers(5,15,25,35))
print("\nFunction description:")
print(add_numbers.__doc__)

