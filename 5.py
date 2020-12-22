print("введите x1")
x1=int(input())
print("введите y1")
y1=int(input())
print("введите x2")
x2=int(input())
print("введите y2")
y2=int(input())
if y1==y2 and x1==x2:
    print("это одна точка")
elif y1==y2:
    print("y = ",y1)
elif x1!=x2:
    k=(y1-y2)/(x1-x2)
    b=y2-k*x2
    print("y =",k,"* x","+",b)
elif x1==x2:
    print("x=",x1)