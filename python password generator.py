import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="0123456789"
symbol="[]{}()#$&;._"
all=lower+upper+number+symbol
length=8
# p=random.sample(all,length)
# print(p)
password="".join(random.sample(all,length))
print("Your Password is: ",password)