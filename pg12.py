a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if a>=b and a>=c:
 biggest=a
elif b>=a and b>=c:
 biggest=b
else:
 biggest=c
print("Biggest number=",biggest)
