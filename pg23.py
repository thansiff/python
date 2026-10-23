d={}
n=int(input("Enter number of elements:"))
for i in range(n):
 key=input("enter key:")
 value=int(input("Enter value:"))
 d[key]=value
ascending = dict(sorted(d.items()))
descending = dict(sorted(d.items(),reverse=True))
print("ascending order:", ascending)
print("Descending order :",descending)
