n=int(input("Enter num"))
num=1
x=n
while(n>0):
    num*=n
    n-=1
print("{} != {}".format(x,num))
