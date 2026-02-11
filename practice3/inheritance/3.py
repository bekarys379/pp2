#Using super() function. Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

class parent:
  def __init__(self, name, lname):
    self.name=name
    self.lastname=lname

  def printname(self):
    print(self.name, self.lastname)

class Student(parent):
  def __init__(self, name, lname):
    super().__init__(name, lname)

x = Student("Mike", "Olsen")
x.printname()
