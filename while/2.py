i=0
tot=0
while i<5:
    if tot>10:
        break #prevents the continuation of the loop if the sum exceeds 10, using break
    tot+=int(input())
    i+=1


print(tot)