#The *args and **kwargs


def fir(*args): #When we put arg we do not know how much parameters we will input
    print(args)

fir(1, 2, 3, 4)
print(fir(1,2,3,4)) #it first executes function and returns the tuple, then the print() function will print "None"


def fir(*anyvar):
    return anyvar

x=map(int, input().split())

res=fir(*x) #it returns the tuple we created from parameters
print(res)


def my_function(*arg): 
  print("The youngest child is " + arg[2])

kids=("John", "Jane", "Jim", "Jill")

my_function(*kids)







'''kwargs = “keyword arguments”

** in the function definition collects any number of named arguments into a dictionary.'''


def my_function(**kwargs):
    print(kwargs)

mydict={"Bekarys" : 17, "AAA" : 20}

my_function(**mydict) #prints {'Bekarys': 17, 'AAA': 20}





#ACCESING VALUES

def my_function(**kwargs):
    print("Name:", kwargs["name"])
    print("City:", kwargs["city"])
    print("Age:", kwargs["age"])

somedictt={'name':'Bekarys', 'city':'Almaty', 'age':17}

my_function(**somedictt)



#Combining *args and **kwargs

def comb_func(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)


x=map(int, input().split())
some_dict={'name':'Bekarys', 'age':17}

comb_func(*x, **some_dict)



