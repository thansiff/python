from Armstrong import armstrong

a = int(input("Enter lower limit: "))
b = int(input("Enter upper limit: "))

for n in range(a, b + 1):
    if armstrong(n):
        print(n)
