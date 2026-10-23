color_list1 = input("Enter colors in list 1:").split()
color_list2 = input("Enter colors in list 2:").split()
print("Colors in list1 but not in list2:")
for color in color_list1:
 if color not in color_list2:
   print(color)

