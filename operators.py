# Arithematic Operators 
#logical Operators
#Relational Operators
#Assignment Operators
#membership operators
#bitwise operators
#identity Operators

#Arthimetic operators
a=15
b=10

print("sum ",a+b )
print("sub ",a - b )
print("mul ",a * b )
print("div ",a /b )
print("rem ",a % b )
print("power ",a ** b )
print("floor ",a // b )
# swap two number
a=10
b=20
print("a: ",a, "b: ",b)
a= a + b
b= a - b
a= a - b
print("a: ",a , "b: ",b)

#relational operators
a=20
b=10
print("equal: ", a ==b)
print("not equal: ", a != b)
print("greater equal:  ", a >=b)
print("less than equal: ", a <=b)
print("greaterThan: ", a>b)
print("lessThan:  ", a < b)

#Logical Operators

a=10
b=20
print("and: ",a and b)
print("or: ", a or b)
print("not: ", not b)

#Assignment operators

a=10
b=20
a+=10
print(a)
a-=12
print(a)
a*=5
print(a)
b=40
b/=10
print(b)
b//=10
print(b)
b=30
b%=5
print(b)
b=60
b **=5
print(b)

#bitwise operators
a=10
b=20
print("a and b: ",a & b)
print("a or b: ",a | b)
print(" not b: ", ~b)
print("a left shift 1: ",a<<1)
print("b  right shift 2: ",b>>2)
print("a  xor b: ",a ^ b)

#identity operator
a=[20,30,40,60]
print(20 in a)

print(70 in a)
print(10 not in a)

#identity operators

a=10
y=10
print(a is y)
x=20
z=x
print(z is x)
print(z is not x)