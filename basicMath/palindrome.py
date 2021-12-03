
n=int(input("enter num:"))
x=n
num=0
while(n>0):
    rem=n%10
    num=num*10 + rem
    n=n//10
if(x==num):
    print(x,"is palindrome")
else:
    print(x,"is not a palindrome number")
