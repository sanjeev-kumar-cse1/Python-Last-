# class Atm:
#     def __init__(self, name , balance, pin):
#         self.name = name # Public specifier
#         self.__balance = balance
#         self.__pin = pin
# ac1 = Atm('rahul', 5000,123)
# print(ac1.name)



# class Atm:
#     def __init__(self, name , balance, pin):
#         self.name = name # Public specifier
#         self.__balance = balance
#         self.__pin = pin
# ac1 = Atm('rahul', 5000,123)
# print(ac1.name)
# print(ac1.balance) # this is give error due to out of class access




# class Atm:
#     def __init__(self, name , balance, pin):
#         self.name = name # Public specifier
#         self.__balance = balance
#         self.__pin = pin
# ac1 = Atm('rahul', 5000,123)
# print(ac1.name)
# print(ac1.balance) # this is give error due to out of class access
# print(ac1.pin) # attribute error





# class Atm:
#     def __init__(self, name , balance, pin):
#         self.name = name # Public specifier
#         self.__balance = balance
#         self.__pin = pin
# ac1 = Atm('rahul', 5000,123)
# print(ac1.name)
# print(ac1.balance) # this is give error due to out of class access
# print(ac1.pin) # attribute error




# class Atm:
#     def __init__(self, name , balance, pin):
#         self.name = name # Public specifier
#         self.__balance = balance
#         self.__pin = pin
# ac1 = Atm('rahul', 5000,123)
# print(ac1.name)
# print(ac1._Atm__balance) 
# print(ac1.pin) # this line give error and above line print






# class Atm:
#     def __init__(self, name , balance, pin):
#         self.name = name # Public specifier
#         self.__balance = balance
#         self.__pin = pin
# ac1 = Atm('rahul', 5000,123)
# print(ac1.name)
# print(ac1._Atm__balance) 
# print(ac1._Atm__pin) 




# class Atm:
#     def __init__(self, name , balance, pin):
#         self.name = name # Public specifier
#         self.__balance = balance
#         self.__pin = pin
        
#         #Method (Getter)
#     def display_details(self):
#         print(f'Name: {self.name}') 
#         print(f'Balance: {self.__balance}') # Getting the private attribute
#         print(f'Pin: {self.__pin}') # Getting the private attribute Pin
            
# ac1 = Atm('rahul', 5000,123)
# print(ac1.name)
# ac1.display_details()




# class Atm:
#     def __init__(self, name , balance, pin):
#         self.name = name # Public specifier
#         self.__balance = balance
#         self.__pin = pin
        
#         #Method (Getter)
#     def display_details(self):
#         return self.name, self.__balance, self.__pin
# ac1 = Atm('rahul', 5000,123)
# print(ac1.name)
# print(ac1.display_details())





# class Atm:
#     def __init__(self, name , balance, pin):
#         self.name = name # Public specifier
#         self.__balance = balance
#         self.__pin = pin
        
#         #Method (Getter)
#     def display_details(self):
#         return self.name, self.__balance, self.__pin
# ac1 = Atm('rahul', 5000,123)
# print(ac1.name)
# print(ac1._Atm__balance)
# details = ac1.display_details()
# print(details[2])






# class Atm:
#     def __init__(self, name , balance, pin):
#         self.name = name # Public specifier
#         self.__balance = balance
#         self.__pin = pin
        
#         #Method (Getter)
#     def display_details(self):
#         return self.name, self.__balance, self.__pin

#     def change_pin(self,new_pin): # setter method
#         self.__pin = new_pin
#         print('Your pin has been changed! ')

# ac1 = Atm('rahul', 5000,123)
# print(ac1.name)
# print(ac1._Atm__balance)
# details = ac1.display_details()
# print(details[2])    
# ac1.change_pin(345)
# print(ac1.display_details())



# class A:
#     def display(self):
#         print('Message from Class A')


# class B:
#     def display(self):
#         print('Message from Class B')

# class C(A , B):
#     pass
# c = C()
# print(c)





# class A:
#     def display(self):
#         print('Message from Class A')


# class B:
#     def display(self):
#         print('Message from Class B')

# class C(A , B):
#     pass
# c = C()
# c.display()






# class A:
#     def display(self):
#         print('Message from Class A')

# class B:
#     def display(self):
#         print('Message from Class B')

# class C(A , B):
#     pass
# c = C()
# print(C.mro()) # Method resolution order





# class Shape:
#     def area(self,length,breadth):
#         return length * breadth

# class Color:
#     def Show_color(self, color):
#         return f'This color is {color}'

# class Square(Shape, Color):
#     pass

# sq = Square()
# print(sq.Show_color('green'))







# class Shape:
#     def area(self,length,breadth):
#         return f'This area is {length * breadth}'

# class Color:
#     def Show_color(self, color):
#         return f'This color is {color}'

# class Square(Shape, Color):
#     pass

# sq = Square()
# print(sq.Show_color('green'))
# print(sq.area(5,5))




