#using bool for while

con=True
x=0
a=int(input())
if a<=0:
     print("end")
while con:
     x+=1
     print(x)
     if x>=a:
         con=False

