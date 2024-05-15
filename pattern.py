"""
n=int(input("Enter number: "))
while n>0:
    j=0
    while j<n:
        print("*",end=" ")
        j+=1
    print()
    n-=1
    """
"""
a=int(input("Enter the number:"))
b=0
print(b)
c=1
print(c)
i=1
while(i<a):
    sum=b+c
    print(sum)
    b=c
    c=sum
    i=i+1
"""
"""
a="python"
for i in a:
    if(i=='p'):
        continue
    elif(i=='T'):
        break
    elif(i=='y'):
        pass
    else:
        print(i)
"""
a=int(input("Enter a: "))
      
b=int(input("Enter b: "))
      
c=int(input("Enter c: "))

if a>b and a>c:
    print(a,"  is the largest")
elif b>c:
    print(b,"  is the largest")
else:
    print(c,"  is the largest")
