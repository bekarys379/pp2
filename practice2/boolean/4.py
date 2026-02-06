code=str(input())
correct=len(code)>=9
print("Valid", correct) #prints if length of input is bigger than 9
if correct==False:
    print("incorrect")