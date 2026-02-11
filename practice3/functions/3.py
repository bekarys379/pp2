#Difference between return and print

def dif1(a, b):
    print("Result is:", a+b)

def dif2(a, b):
    return a+b

a=5
b=2
x=dif1(a, b)
print("x is:", x) #will print <'x is: None'>
y=dif2(a, b) 
print("y is:", y)  #will print <'y is: 7'>
#So we see that print() displays result while return returns a value