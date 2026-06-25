n=int(input("enter a number: "))
temp=n
s_sum=0
# length=len(str(n))
while(temp>0):
    digits=temp%10
# print(digits)
    s_sum +=digits ** len(str(n))
    temp=temp//10
# print(sum)
if(s_sum==n):
    print(n,"is armstrong")
else:
    print(n,"is not a armstrong")

