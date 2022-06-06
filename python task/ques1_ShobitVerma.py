print("Enter the length of the string\n")
rang=int(input())
for i in range(0,rang):
    print("enter the value",(i+1),"\n")
    flag =int(input())
    list.append(flag)

print("enter the order\n")
order=input()
if(order=="asc"):
    list.sort()
    print("the new list",list)
if(order=="desc"):
    list.sort()
    list.reverse()
    print("the new list",list)
if(order=="none"):
    
    print("the list",list)
