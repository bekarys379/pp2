i=0
total=0

while i<5:
    num=int(input())

    if num<0:
        continue   #skips negative numbers by using continue

    total+=num
    i+=1

print(total)
