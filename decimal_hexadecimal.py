n=int(input())
l=[]
while n!=0:
    c=n%16
    l.append(c)
    n=n//16
l.reverse()
for i in l:
    print(i,end="")