def compare(s1,s2,n):
  return s1[:n] == s2[:n]
s1=input("enter first string:")
s2=input("enter second string:")
n=int (input("Enter n:"))
print(compare(s1,s2,n))

