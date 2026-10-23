numbers = list(map(int,input("Enter integers:").split()))
positive = [x for x in numbers if x>0]
print("Positive numbers:",positive)
