#Class variables vs Instance variables

'''Class variables-Defined inside the class but outside any method. Shared by all instances of the class
If you change it via the class, it affects all instances. If you change it with an instance, 
it creates an instance variable that overrides the class variable for that object'''

class Student:
    school = "ABC School"

s1 = Student()
s2 = Student()

print(s1.school)  # ABC School
print(s2.school)  # ABC School


Student.school = "XYZ School"
print(s1.school)  # XYZ School
print(s2.school)  # XYZ School


del s1 #deleting an object