n=int(input("Enter number of elements:"))
lst = []
for i in range(n):
 x=int(input("Enter element:"))
 lst.append(x)
total=0
for i in lst:
 total=total+i
print("sum=",total)
