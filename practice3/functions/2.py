#Parameters

def sec_func(n):    #Here we can put our parameters that will be in the function 
    print("This function prints an", n) 

a=int(2)
sec_func(a) #Will print 2

def another_second_function(a, b):
    print((a**2+b**2)**(1/2)) 

x=3
y=4
another_second_function(x, y)    #we declare x and y, and input them as our parameters. It will print 5.0
