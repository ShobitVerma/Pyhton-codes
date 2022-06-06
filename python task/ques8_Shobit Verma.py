print("Enter a string")
str=input()
l=len(str)
sum=0
for i in range(0,l):
    if(ord(str[i])>=48 and ord(str[i])<=57):
        sum=sum+int(str[i])
print("sum is",sum)  
