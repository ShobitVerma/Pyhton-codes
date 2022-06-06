print("Enter a string")
str=input()
l=len(str)
newstr=""
for i in range(0,l):
    pos=str[i]
    newstr=newstr+pos*2
print(newstr)
