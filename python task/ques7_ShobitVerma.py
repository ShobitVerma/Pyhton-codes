print("enter the range of list")
rang= int(input())
list=[]
for i in range(0,rang):
    print("enter the element of list")
    ele=input()
    list.append(ele)
freq=0
max=0
maxval=""
for i in list:
    freq=list.count(i)
    if(freq>max):
       max=freq
       maxval=i
print("the value with max frequency is ",maxval) 
print("with frequency",max)        
