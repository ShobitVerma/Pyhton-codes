print("enter first number")
a=int(input())
print("enter mathematical operator")
oper=input().strip()
print("enter second number")
b=int(input())
res=0.0
if(oper=="+"):
    res=a+b
if(oper=="-"):
    res=a-b
if(oper=="/"):
    res=a/b
if(oper=="*"):
    res=a*b
print("Result is ", res)