# # square pattern
n=int(input("enter a number: "))
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()

# # triangle pattern
n=int(input("enter a number: "))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

# # number pattern
n=int(input("enter a number: "))
for i in range(n):
    for j in range(1,i+1):
        print(j,end=" ")
    print() 


# # 
# #  4. Repeated Number Triangle 

n=int(input("enter a number: "))
for i in range(n+1
):
    for j in range(1,i+1):
        print(i,end=" ")
    print()


#  5. Alphabet Triangle
 
n=5

for i in range(n):
    val=65
    for j in range(i):
        print(chr(val),end=" ")
        val+=1
    print()  

# inverted triangle

n=int(input("enter a number: "))
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()


# inverted number triangle
n=int(input("enter a number: "))
for i in range(n):
    for j in range(1,n-i):
        print(j,end=" ")
    print()


# # continuous number pattern
n=int(input("enter a number: "))
num=1
for i in range(n+1):
    for j in range(i):
        print(num,end=" ")
        num +=1
    print()

# # right angle star triangle
n=int(input("enter a number: "))
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

# pyramid star triangle
n=int(input("enter a number: "))
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2 * i+1):
        print("*",end=" ")
    print()



