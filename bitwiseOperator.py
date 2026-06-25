#bitwise operators: &,|,~,<< ,>> ,^
a=10
b=20
print("a and b: ",a & b)
print("a or b: ",a | b)
print(" not b: ", ~b)
print("a left shift 1: ",a<<1)
print("b  right shift 2: ",b>>2)
print("a  xor b: ",a ^ b)

x=10
y=10
print("xor oparation same values: ",x ^ y) 
# output: 0
# __________________________________________________________________
n=int(input("enter a number: "))
if(n & 1):
    print(n,"is even")
else:

    print(n,"is odd")  

# output: 18 is even

# __________________________________________________________
x=25
print(x << 1)  
# output: 50
print(x>> 2)

# output : 6