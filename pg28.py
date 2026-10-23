start=int(input("Enter starting range:"))
end=int(input("Enter ending range:"))
for n in range(start,end+1):
 if n >=1000 and n <=9999:
   if all(int(d) % 2==0 for d in str(n)):
         root=int(n**0.5)
         if root*root==n:
            print(n)
