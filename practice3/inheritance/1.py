'''Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.'''

#first we will create a class name parent

class parent:
    def __init__(self, name, lname):
        self.name=name
        self.lname=lname

    def printname(self):
        print(self.name, self.lname)


x=parent("AAA", "BBB")
x.printname()


class student(parent): #we create a class named Student, which will inherit the properties and methods from the Person class:
    pass #we use 'pass' when we dont need any other additional properties

a = student("John", "Doe")
a.printname()
