# s="hi hello ravi garu  "
# l=[ val if val=='a' or val=='e' or val=='i' or val=='o' or val=='u'  else val for val in s]
# print(l)

s="hi hello ravi garu"
vow=[]
cons=[]
l=[ vow.append(val) if(val=='a' or val=='e' or val=='i' or val=='o' or val=='u') else cons.append(val) for val in s]
print(l)

print(vow)
print(cons)