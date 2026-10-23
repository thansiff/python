list1 = list(map(int,input("enter first list:").split()))
list2 = list(map(int,input("enter second list:").split()))
if len(list1)==len(list2):
 print("(a)Lists are of the same length")
else:
 print("(a)Lists are not of the same length")
if sum(list1)==sum(list2):
 print("(b)Lists are equal")
else:
 print("(b)Lists are not equal")
if set(list1).intersection(set(list2)):
 print("(c) Avalue occurs in both lists")
else:
 print("(c)No common value")

