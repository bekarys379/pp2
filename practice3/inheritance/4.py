#Multiple inheritance-a class inherits from more than one parent class.

'''class student(parent1, parent2):
    pass'''

#for example

class father:
    def __init__(self, hair, eyes):
        self.hair=hair
        self.eyes=eyes

class mother:
    def __init__(self, height, nose):
        self.height=height
        self.nose=nose


p1=father("black", "green")

p2=mother("tall", "good")

class son(father, mother):
    def __init__(self, hair, eyes, height, nose):
        father.__init__(self, hair, eyes)
        mother.__init__(self, height, nose)

c = son("black", "green", "tall", "good")
print(c.eyes)  
print(c.hair)   
print(c.height) 
print(c.nose)  

