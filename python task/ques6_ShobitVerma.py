print("Enter the lower limit ")
ll=int(input())
print("Enter the upper limit")
ul=int(input())
flag=0
list=[]
for i in range(ll,ul+1):
    for j in range(2,i):
        if (i%j==0):
         flag=1
    if(flag==0):
        list.append(i)
    flag=0
print("The prime nos are ",list)


