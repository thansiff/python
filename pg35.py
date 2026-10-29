def simple_interest(p,t,senior):
 if senior:
   r = 12
 else:
  r = 10
 return(p*r*t)/100
p = float(input("Enter principal amount:"))
t = float(input("Enter time in year:"))
senior=input("are you a senior citizen?(yes/no):")
if senior.lower()=="yes":
   senior = True
else:
   senior =False
print("simple interest =",simple_interest(p,t,senior))
