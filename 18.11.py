# # Question solve

# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand

# class Bike(Vehicle):
#     def __init__(self, brand, milage):
#         super().__init__(brand)
#         self.milage = milage
# splender = Bike('Hero', 60)
# print(splender.brand)
# print(splender.milage)




# class Shape:
#     def __init__(self, shape):
#         self.shape = shape
# class Circle(Shape):
#     def __init__(self, shape):
#         super().__init__(shape)
#     def area(self,radius):
#         print(3.14 * (radius ** 2))
# c = Circle('Circle')
# print(c.area(10))



# class Teacher:
#     def __init__(self,name ,age):
#         self.name = name
#         self.age = age
# class MathTeacher(Teacher):
#     def __init__(self,name ,age,sub):
#         super().__init__(name,age)
#         self.sub = sub
#     def details(self):
#         print(f'Name: {self.name}')
#         print(f'age: {self.age}')
#         print(f'Subject: {self.sub}')
# math = MathTeacher('Rahul',45, 'Math')
# math.details()