string = input("Ente a string:")
if len(string)>2 :
    new_string = string[-1] + string[1 : -1] + string[0]
else:
    new_string = string
print("Modified String:", new_string)
