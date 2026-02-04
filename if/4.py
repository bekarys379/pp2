a=int(input())
b=int(input())
if b-a<0:
     print("first")
elif a-b>0:
     print("second")
elif a!=b:
    print("third") #you can have as many as you need elif statements, it will choose block that is True and skip the rest