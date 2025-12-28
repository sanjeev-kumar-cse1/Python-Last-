# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
    
#     def deposite(self,money):
#         self.balance += money
#         print('Paise to jama ho gy')
    
#     def check_bal(self):
#         print(f'Your balance is {self.balance}')

# obj1 = BankAccount('Rahul', 2000)

# obj1.deposite(6000) # paise account me dala or a 2000 me add ho jaaega
# obj1.check_bal()





# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

# prd_list = [Product('Pen',10),Product('car',120000),Product('Books',1000)]
# for product in prd_list:
#     print(product.name)
#     print(product.price)





# class GrandFather:
#     property = 'Dada ji ke pass bahot paise hai'

# class Father(GrandFather):
#     pass

# class Child(Father):
#     pass

# father = Father()
# child = Child()
# # print(father.property)
# print(child.property)




# class GrandFather:
#     property = 'Dada ji ke pass bahot paise hai'

# class Father(GrandFather):
#     bike = 'Apache-Bike'

# class Child(Father):
#     pass

# father = Father()
# child = Child()
# # print(father.property)
# print(child.property)
# print(child.bike)






# class Animal:
#     def eat(self):
#         print('Animal eats')
# class Dog(Animal):
#     def barks(self):
#         print('Dog barks')
# class Puppy(Dog):
#     def cry(self):
#         print('Puppy cry')
        
# animal = Animal()
# dog = Dog()
# puppy = Puppy()

# # animal.eat()
# dog.eat()
# puppy.eat()
# puppy.cry()
# puppy.barks()





# class Animal:
#     def eat(self):
#         print('Animal eats')
# class Dog(Animal):
#     def barks(self):
#         print('Dog barks')
# class Puppy(Dog):
#     def cry(self):
#         print('Puppy cry')
#     def display(self):
#         self.cry()
#         self.barks()
#         self.eat()
        
# animal = Animal()
# dog = Dog()
# puppy = Puppy()

# puppy.display()




# class Person:
#     def get_name(self):
#         self.name = input('Enter your name: ')

# class Student(Person):
#     def get_marks(self):
#         self.marks = int(input('Enter your marks: '))
# class Result(Student):
#     def result(self):
#         print(self.name)
#         print(self.marks)

# re = Result()
# re.get_name()
# re.get_marks()
# re.result()








class Person:
    def get_name(self):
        self.name = input('Enter your name: ')

class Student(Person):
    def get_marks(self):
        self.marks = int(input('Enter your marks: '))
class Result(Student):
    pass

re = Result()
re.get_name()
re.get_marks()
print(re.name)
print(re.marks)