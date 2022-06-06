print("Enter your credit card no.")
numb=input()
numb=numb.replace(" ","")
l=len(numb)
str=numb[l-4:l]
for i in range(0,(l-4)):
   str="*"+str
print(str)