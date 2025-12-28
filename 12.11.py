# student_name = 'Rahul'
# batch_name = 'A20'
# mobile_number = 1234
# def display(name, batch, mob):
#     print(f'Name {name}')
#     print(f'Batch {batch}')
#     print(f'Mob {mob}')
# display(student_name,batch_name,mobile_number)




# student_name = 'Rahul'
# batch_name = 'A20'
# mobile_number = 1234
# student_name2 = 'RahulK'
# batch_name2 = 'A201'
# mobile_number2 = 12345
# def display(name, batch, mob):
#     print(f'Name {name}')
#     print(f'Batch {batch}')
#     print(f'Mob {mob}')
# display(student_name,batch_name,mobile_number)

# def change_mob(new_num):
#     global mobile_number
#     mobile_number = new_num
# change_mob(67890)
# print('After changing the mobile: ' , mobile_number)





# class Student:
#     def __init__(self, name, age, marks): # constructor 
#         self.name = name # attributes
#         self.age = age 
#         self.marks = marks

# a1 = Student('Ayush', 12,14)
# print(a1) # <__main__.Student object at 0x000001FE47C61940>
# print(a1.name) # name print




# class Student:
#     def __init__(self, name, age, marks): # constructor 
#         self.name = name # attributes
#         self.age = age 
#         self.marks = marks

# a1 = Student('Ayush', 12,14)
# a2 = Student('Ayush kum', 12,14)
# print(a1) # <__main__.Student object at 0x000001FE47C61940>
# print(a1.name) # name print
# print(a1.name, a1.age, a1.marks) 

# print(a2.name)





# class Student:
#     def __init__(self, name, age, marks): # constructor 
#         self.name = name # attributes
#         self.age = age 
#         self.marks = marks

# a1 = Student('Ayush', 12,14)
# a2 = Student('Ayush kum', 12,14)
# print(a1) # <__main__.Student object at 0x000001FE47C61940>
# print(a1.name) # name print
# print(a1.name, a1.age, a1.marks) 

# print(a2.name)




# class Student:
#     def __init__(self, name, age, marks): # constructor 
#         self.name = name # attributes
#         self.age = age 
#         self.marks = marks
#     def display_details(self):
#         print(f'Name: {self.name}') # self take current objject property
# a1 = Student('Ayush', 12,14)
# a2 = Student('Ayush kum', 12,14)
# a2.display_details()




# class Student:
#     def __init__(self, name, age, marks): # constructor 
#         self.name = name # attributes
#         self.age = age 
#         self.marks = marks
#     def display_details(self):
#         print(f'Name: {self.name}') # self take current objject property
#         print(f'Age: {self.age}') 
#         print(f'Marks: {self.marks}') 
# a1 = Student('Ayush', 12,14)
# a2 = Student('Ayush kum', 12,14)
# a2.display_details()




# class Student:
#     def __init__(self, name, age, marks): # constructor 
#         self.name = name # attributes
#         self.age = age 
#         self.marks = marks
#     def display_details(self):
#         print(f'Name: {self.name}') # self take current objject property
#         print(f'Age: {self.age}') 
#         print(f'Marks: {self.marks}') 
# a1 = Student('Ayush', 12,14)
# a2 = Student('Ayush kum', 12,14)
# a2.display_details()
# a1.display_details()




class Student:
    def __init__(self, name, age, marks): # constructor 
        self.name = name # attributes
        self.age = age 
        self.marks = marks
    def display_details(self):
        print(f'Name: {self.name}') # self take current objject property
        print(f'Age: {self.age}') 
        print(f'Marks: {self.marks}') 
    def change_marks(self,new_marks):
        self.marks = new_marks
        print('Your marks has been changed.')
a1 = Student('Ayush', 12,14)
a2 = Student('Ayush kum', 12,14)
a2.display_details()
# a1.display_details()
a1.change_marks(50)
a1.display_details()


