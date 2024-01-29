list=[20,30,15,108,200,48,501]
list2=[]
for x in list:
    if(x<50):
        f=x+50
        list2.append(f)
    elif(x>100):
        f=x+100
        list2.append(f)
    elif(x>50 and x<100):
        f=x+0
        list2.append(f)
print(list)
print(list2)
