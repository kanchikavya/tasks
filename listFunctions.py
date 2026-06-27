# sum of the list
l=[1,2,3,4]
sum=0
for i in range(len(l)):
    sum +=l[i]
print(sum)

# product of the list
l=[1,2,3,4]
product=1
for i in range(len(l)):
    product *=l[i]
print(product)

# max element of the list
l=[1,2,3,4]
max1=0
for i in range(len(l)):
    if(max1<l[i]):
        max1=l[i]
print(max1)
# min element of the list
l=[1,2,3,4]
min1=100000
for i in range(len(l)):
    if(min1>l[i]):
        min1=l[i]
print(min1)

# length  of the list
l=[1,2,3,4]
count=0
for i in range(len(l)):
   count+=1
print(count)