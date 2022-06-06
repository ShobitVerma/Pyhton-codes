import random
list=[]

for i in range (0,100): #a random array 
    num=random.randint(1,99)
    list.append(num)

for i in list :#counting the duplicate no with its freq
    coun=list.count(i)
    if(coun>1):
        print("duplicate no. is ", i,"with frequency",coun)
    for j in range (0,coun):
       list.remove(i)