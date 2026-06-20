

# # sum of digits  1234 -->10
# n=1234
# s_sum=0
# while(n>0):
#     temp=n%10
#     s_sum+=temp
#     n//=10
# print(s_sum)

# #reverse of digits 
# n=1234
# rev=0
# while(n>0):
#     temp=n%10
#     rev=rev *10 +temp
#     n//=10
# print(rev)

# #count digits in a number 
# n=12345
# count=0
# while(n>0):
#     temp=n%10
#     count +=1
#     n//=10
# print(count)

# #even or odd
# n=int(input("enter a number: "))
# if(n & 1==0):
#     print(n,"is even number")
# else:
#     print(n,"is odd number")

# # ______________________________
# n=int(input("enter a number: "))
# if((n//2) **n):
#     print(n,"is  even")
# else:
#     print(n,"is odd")

# # prime or not prime

# n=int(input("enter a number: "))
# for i in range(2,n):
#     if(n%i==0):
#         print(n,"is not a prime number")
#         break
# else:
#     print(n,"is prime number")


# # find factorial of a number
# n=int(input("enter a number: "))
# fact=1
# for i in range(1,n):
#     fact= fact * i
# print(fact)

# find factors of a number 

# n=int(input("enter a number: "))
# for i in range(1,n):
#     if(n%i==0):
        # print(n)


# check palindrome number

# n=121
# m=n
# rev=0
# while(n>0):
#     temp=n%10
#     rev=rev *10 +temp
#     n//=10
# # print(rev)
# if(m==rev):
#     print(m,"is a palindrome")
# else:
#     print(m,"is not a palindrome")

# check armstrong number
n=int(input("enter number: "))
s_sum=0
temp=n
while(temp>0):
    digit=temp%10
    s_sum+=digit** len(str(n))
    temp//=10
# print(s_sum)
if(s_sum==n):
    print("is armstrong number")
else:
    print("is not armstrong number")

# find the factors of a given number
n=int(input("enter a number: "))
for i in range(1,n+1):
    if(n%i==0):
        print(i,end=" ")
    
#find gcd of 2 numbers
a=int(input("enter first number: "))
b=int(input("enter second number: "))
gcd=1
if a<b:
    smaller=a
else:
    smaller=b
for i in range(1,smaller +1):
    if (a % i==0 and b % i==0):
        gcd=i
print(gcd)



