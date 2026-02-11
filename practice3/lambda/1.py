#A lambda function is a small anonymous function (a function without a name).

''' structure of lambda function
lambda arguments:expression

and it returns expression as value

example:
'''

add=lambda x, y:x*y
print(add(2, 3)) #returns 6


#We can also print it without assigning a variable:

print((lambda x, y:x*y)(5, 4)) #prints 20



#doubling lambda function

def myfunc(n):
  return lambda a:a*n

mydoubler=myfunc(2) #myfunc gets executed and then returns a, where mydoubler gets 2 as value

print(mydoubler(11)) #and then once we use print, mydoubler function executes, multiplying 11 by 2 and printing 22


#TRIPLING FUNCTION

def tripfunc(n):
    return lambda a:a*n

n=int(3)
tripler=tripfunc(n) #now tripler=a*3
x=5
print(tripler(5))