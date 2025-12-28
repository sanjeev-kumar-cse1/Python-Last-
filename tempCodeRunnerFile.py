
class Student:
    school = 'DIP'
    sub = 'English'

    def __init__(self,name, age, rollno): # constructor
        self.name = name # instance attribute
        self.age = age 
        self.rollno = rollno

student1 = Student('Aayush', 24, 12) # here is Ayush is object 
student2 = Student('Rahul', 25, 2)
print(student1.school)
print(student1.sub)
print(student1.name)
print(student2.name)

