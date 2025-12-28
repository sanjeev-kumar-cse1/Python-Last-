# class Student:
#     school = 'DIP'

# student1 = Student()
# student2 = Student()
# print(student1.school)
# print(student2.school)



# class Student:
#     school = 'DIP'
#     sub = 'English'

# student1 = Student()
# student2 = Student()
# print(student1.school)
# print(student1.sub)

# print(student2.sub)




# class Student:
#     school = 'DIP'
#     sub = 'English'

#     def __init__(self,name, age, rollno): # constructor
#         self.name = name # instance attribute
#         self.age = age 
#         self.rollno = rollno

# student1 = Student('Aayush', 24, 12) # here is Ayush is object 
# student2 = Student('Rahul', 25, 2)
# print(student1.school)
# print(student1.sub)
# print(student1.name)
# print(student2.name)




# class Student:
#     school = 'DIP'
#     sub = 'English'

#     def __init__(self,name, age, rollno): # constructor
#         self.name = name # instance attribute
#         self.age = age 
#         self.rollno = rollno

#     def display(self):
#         print(f'Name: {self.name}')
#         print(f'age: {self.age}')
#         print(f'rollno: {self.rollno}')

# student1 = Student('Aayush', 24, 12) # here is Ayush is object 
# student2 = Student('Rahul', 25, 2)

# student1.display()






# class Student:
#     school = 'DIP'
#     sub = 'English'

#     def __init__(self,name, age, rollno): # constructor
#         self.name = name # instance attribute
#         self.age = age 
#         self.rollno = rollno

#     def display(self):
#         print(f'Name: {self.name}')
#         print(f'age: {self.age}')
#         print(f'rollno: {self.rollno}')
#         print(f'school: {self.school}')

# student1 = Student('Aayush', 24, 12) # here is Ayush is object 
# student2 = Student('Rahul', 25, 2)

# student1.display()




# class Student:
#     school = 'DIP'
#     sub = 'English'

#     def __init__(self,name, age, rollno): # constructor
#         self.name = name # instance attribute
#         self.age = age 
#         self.rollno = rollno

#     def display(self):
#         print(f'Name: {self.name}')
#         print(f'age: {self.age}')
#         print(f'rollno: {self.rollno}')
#         print(f'school: {Student.school}')

# student1 = Student('Aayush', 24, 12) # here is Ayush is object 
# student2 = Student('Rahul', 25, 2)

# student1.display()




# This is QUESTION
# You are building a employee management system . company = TCS
# salary, name , age, department
# create a class Employee having class and instance attributes and display their details
# add one more method to change the employee salary  6000 -> 7000

# class Dad:
#     paise = 50000

# class Child(Dad):
#     pass

# rahul = Child()
# print(rahul.paise)





# class Dad:
#     paise = 50000

# class Child(Dad):
#     def __init__(self,car):
#         self.car = car
#     def display(self):
#         print(f'Mere pass papa ke paise ka access hai {self.paise}')
#         print(f'Mere pass {self.car} hai')
# rahul = Child('BMW')
# print(rahul.display())





# class Dad:
#     paise = 50000

#     def __init__(self,land):
#         self.land = land
# class Child(Dad):
#     def __init__(self,car,land):
#         super().__init__(land) # take attribute from the P to C class
#         self.car = car
#     def display(self):
#         print(f'Mere pass papa ke paise ka access hai {self.paise}')
#         print(f'Mere pass {self.car} hai')
#         print(f'Unki jamin {self.land}')
# rahul = Child('BMW','Jaipur')
# print(rahul.display())





class Dad:
    paise = 50000

    def __init__(self,land):
        self.land = land
class Child(Dad):
    def __init__(self,car,land):
        super().__init__(land) # take attribute from the P to C class
        self.car = car
    def display(self):
        print(f'Mere pass papa ke paise ka access hai {self.paise}')
        print(f'Mere pass {self.car} hai')
        print(f'Unki jamin {self.land}')
rahul = Child('BMW','Jaipur')
print(rahul.display())
