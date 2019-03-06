# 最大公约数计算
a=int(input('please enter 1st num:'))
b=int(input('please enter 2nd num:'))
s=a*b
while a%b!=0:
    a,b=b,(a%b)  
else:
    print(b,'is the maximum common divisor')
    print(s//b,'is the least common multiple')
