#the __init__ constructor method

'''__init__() is a special method in Python classes
Its called automatically when you create a new instance of the class'''

class studen:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def greet(self):
        print("Nice to meet you, my name is", self.name)


s1=studen("Bekarys", 17)
s1.greet()