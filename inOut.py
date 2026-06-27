# 1.Missing input()
n=int
print(n)
# Correct
n=int(input("Enter a number: "))
print(n)
# 2.Not converting input to integer 
#  Wrong
a=input("Enter first number: ")
b=input("Enter second number: ")
print(a+b)
# Correct
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(a+b)
# 3. Missing closing parenthesis
# Wrong
print("Hello"
# Correct
print("Hello")
# 4. Using variable before input

#  Wrong

print(n)
n = int(input())

#  Correct

n = int(input())
print(n)
# 5. Printing string instead of variable
#  Wrong

name=input("Enter name: ")
print("name")

name = input("Enter name: ")
print(name)
# 6. Invalid integer input

# Wrong

n = int(input())

# Input:

# abc

# Error:

# ValueError

# Correct

try:
    n = int(input())
    print(n)
except ValueError:
    print("Enter a valid number")
# 7. Missing comma in print()
# Wrong
a=10
print("Value =" a)
# Correct
a = 10
print("Value =", a)
# 8. Using = instead of ==
#  Wrong
n=int(input())
if n=10:
    print("Ten")
#  Correct
n=int(input())
if n==10:
    print("Ten")
# Input Functions
input()
int(input())
float(input())
# Output Functions
print()
print(a)
print("Value =", a)
print(a, end=" ")
print(a, b, sep="-")