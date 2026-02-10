#   find the factorial of numbers using loops
""" 

created on tue feb 10 2026 
@author : dipak 
"""

n = int(input("enter number:"))
fact = 1 

for i in range (1,n+ 1):
  fact = fact*i
print("factorial:", fact)
