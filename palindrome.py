n=int(input())
temp=n
s=0
while n>0:
    num=n%10
    s=s*10+num
    n=n//10
print(s)
if s==temp:
    print("palindrome")
else:
    print("Not a palindrome")
