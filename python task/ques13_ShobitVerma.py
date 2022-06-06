print("enter the range of list")
rang= int(input())
list=[]
for i in range(0,rang):
    print("enter the element of list")
    ele=input()
    list.append(ele)


for i in list:
     coun=list.count(i)
     if(coun%2==1):
         print("the element that has odd count is ",i)
         for j in range(0,coun):
            list.remove(i)
    

