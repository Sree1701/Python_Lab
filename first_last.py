colors=input("Enter color names seperated by commas:")
color_list=colors.split(",")
color_list=[color.strip() for color in color_list]
print("Color List:",color_list)
print("First Color:",color_list[0])
print("Last Color:",color_list[-1])
