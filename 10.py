list=[]
for i in range(100,200):
    temp=i
    sum=0
    while i>0:
        rem=i%10
        sum=sum+rem
        i=i//10
    if(sum%2==0):
        list.append(temp)
print("The sum of digits is an even number:",list)


