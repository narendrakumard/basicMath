
n=int(input("enter num:"))
x=n
num=0
while(n>0):
    rem=n%10
    num+=pow(rem,3)
    n=n//10
if(x==num):
    print(x,"is armstrong number")
else:
    print(x,"is not armstrong number")
