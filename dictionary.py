#factors of a numbers
n=int(input("enter a number:"))
i=1

while(n>0):
    if(n%i==0):
        print(i)
    i+=1



# # Sum of first N numbers
print("\n")
n=int(input("enter a number: "))
sum=0
for i in range(n+1):
    sum+=i
print(sum,end=" ")

# Check even or odd
print("\n")
n=int(input("enter a number: "))
if(n%2==0):
    print(n,"is even number")
else:
    print(n,"is not even number")
# # /////
print("\n")
n=int(input("enter a number: "))
if(n & 1==0):
    print(n,"is even number")
else:
    print(n,"is not even number")


# Factorial
print("\n")
n=int(input("enter a number: "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)



# Count digits in a number
print("\n")
n=int(input("enter a number: "))
count=0
while(n>0):

    n=n//10
    count+=1
print(count,"number of digits")

# Reverse a number
print("\n")
n=int(input("enter a number: "))
rev=0
temp=n
while(n>0):
    temp=n%10
    rev=rev*10+temp
    n=n//10
print(rev)

# Sum of digits
print("\n")
n=int(input("enter a number: "))
sum=0
temp=n
while(n>0):
    temp=n%10
    sum+=temp
    n=n//10
print(sum)


# Check palindrome number
print("\n")
n=int(input("enter a number: "))
rev=0
temp=n
while(n>0):
    digit=n%10
    rev=rev*10+digit
    n=n//10
if(temp==rev):
    print("is a palindrome")
else:
    print("is not a palindrome")

# Check Armstrong number
print("\n")

n=int(input("enter a number: "))
temp=n
total=0
while(n>0):
    digit=n%10
    total=total+len(str(n))
    n=n//10
if(temp==total):
    print("is a Amstrong number")
else:
    print("is not a amstrong number")
# Check prime number
print("\n")

n=int(input("enter a number: "))
if(n<=1):
    print("not a prime number")
else:
    for i in range(2,n):
        if(n%i==0):
            print("not a prime number")
            break
    else:
        print("is a prime number")
            


#  GCD/HCF of two numbers
print("\n")
a = int(input("Enter a number: "))
b=int(input("enter a number: "))
gcd=1
for i in range(1,a+1):
    if(a%i==0 and b%i==0):
        gcd=i

print(gcd)

# LCM of two numbers
print("\n")

a = int(input("Enter a number: "))
b=int(input("enter a number: "))

# lcm=1
if (a>b):
    lcm=a
else:
    lcm=b

while True:
    if(lcm%a==0 and lcm%b==0):
        print("lcm=",lcm)
        break
    lcm+=1

print(lcm)



