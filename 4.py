import random
a=[]
for i in range(3):
   a.append([random.randint(0,5) for p in range(15)])
max = 0
sum1=0
sum2=0
sum3=0
for j in range(15):
    sum1+=a[0][j]
if sum1>max:
    max=sum1
for j in range(15):
    sum2+=a[1][j]
if sum2>max:
    max=sum2
for j in range(15):
    sum3+=a[2][j]
if sum3>max:
    max=sum3
print(max)