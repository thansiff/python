def add(*args):
    """Return the sum of all given numbers."""
    return sum(args)
n = int(input("How many numbers?"))
numbers=[]
for i in range(n):
   numbers.append(int(input("Enter number:")))
print("sum=",add(*numbers))
print("Docstring:",add.__doc__)
