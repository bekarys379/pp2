#The __init__() function is called automatically every time the class is being used to create a new object.


class parent:
    def __init__(self, name, lname):
        self.name=name
        self.lname=lname

    def printname(self):
        print(self.name, self.lname)


x=parent("AAA", "BBB")
x.printname()

    #When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

  

class Student(parent):
    def __init__(self, name, lname):
        parent.__init__(self, fname, lname) #To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
  