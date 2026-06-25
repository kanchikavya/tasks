# check number is number is positive or not
n=int(input("enter a number: "))
if(n<0):
    print("negative number")
elif(n>0):
    print("positive number")
elif(n==0):
    print("neighter postive nor negative")
else:
    print("not a number")

#  python conditionals.py
# enter a number: 19
# positive number


# $ python conditionals.py
# enter a number: -2
# negative number

# $ python conditionals.py
# enter a number: 0
# _______________________________________________________________________
# check whether the given number is upper or lower case

# n=int(input("enter a number: "))
ch=input("enter a letter: ")
if(ord(ch)>=65 and ord(ch)<=90):
    print(ch,"is an upper case")
else:
    print(ch,"is an lower case")


s1=int(input("enter s1 marks: "))
s2=int(input("enter s2 marks: "))
s3=int(input("enter s3 marks: "))
s4=int(input("enter s4 marks: "))
s5=int(input("enter s5 marks: "))
s6=int(input("enter s6 marks: "))
if(s1>=35 and s2>=35 and s3>=35 and s4>=34 and s5>=35 and s6>=35):
    print(" the student is pass")
else:
    print("the student is fail")
