def factorial(n):
    if n == 0 or n == 1:
       return 1
    return n*factorial(n-1)
n=int(input("Enter number of terms:"))
total =0
for i in range(1,n+1):
   total +=(i**i)/factorial(i)
print("sum of series=",total)
