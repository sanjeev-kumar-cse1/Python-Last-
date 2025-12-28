#Multiple Inheritance

# class Mother:
#     def __init__(self):
#         self.home_mng = 'Home Management' # instance attribute

# class Father:
#     def __init__(self):
#         self.finance_mng = 'Finance Management'

# class Child(Mother, Father):
#     def __init__(self):
#         Mother.__init__(self)
#         # Father.__init__(self)

# child = Child() #Here we are instanciating the obj or instance
# print(child.home_mng)
# # print(child.finance_mng)





# class Mother:
#     def __init__(self):
#         self.home_mng = 'Home Management' # instance attribute

# class Father:
#     def __init__(self):
#         self.finance_mng = 'Finance Management'

# class Child(Mother, Father):
#     def __init__(self):
#         Mother.__init__(self)
#         Father.__init__(self)
#     def display(self):
#         print(f'Property1 : {self.home_mng}')
#         print(f'Property2 : {self.finance_mng}')

# child = Child() #Here we are instanciating the obj or instance
# print(child.home_mng)
# child.display()




# # This  is not good code please improve
# class A:
#     def __init__(self):
#         self.li = []
# class B(A):
#     def add_value(self, value):
#         super().__init__(li)
#         self.li.append(value)

# class C(B):
#     def display(self):
#         print(self.li)

# c = C()
# print(c)
# c.add_value('sanjeev')




# class Student:
#     def __init__(self, name, marks,rollno):
#         self.name = name
#         self.marks = marks
#         self.rollno = rollno
# s1 = Student('Sanjeev', 54, 12)
# print(s1.marks)



# class Student:
#     def __init__(self, name, marks,rollno):
#         self.name = name
#         self.marks = marks
#         self.rollno = rollno
# s1 = Student('Sanjeev', 54, 12)
# s1.marks = 90
# print(s1.marks)





# class Student:
#     def __init__(self, name, marks,rollno,num):
#         self.name = name
#         self._marks = marks # private attribute
#         self.__num = num # Protected attribute
#         self.rollno = rollno 
# s1 = Student('Sanjeev', 54, 12,124232)
# # s1.marks = 90 # this can never change to the original marks
# print(s1._marks)
# print(s1._Student__num)





# class Student:
#     def __init__(self, name, marks,rollno,num):
#         self.name = name
#         self._marks = marks 
#         self.rollno = rollno
# s1 = Student('Sanjeev', 54, 12,124232)
# print(s1.name)
# print(s1.rollno)





# class Student:
#     def __init__(self, name, marks,rollno):
#         self.__marks = marks 
#         self.name = name
#         self.rollno = rollno

#     def display_marks(self):
#         print(self.__marks)
#     def change_marks(self,new_marks):
#         self.__marks = new_marks

# s1 = Student('Sanjeev', 54, 12)
# s1.display_marks()
# s1.change_marks(50)
# s1.display_marks()



# class ATM:
#     def __init__(self,pin,name,balance):
#         self.__pin = pin
#         self.name = name
#         self.__balance = balance
#     def verify_pin(self,user_pin):
#         if self.__pin == user_pin:
#             print('User is verified')
#     def change_pin(self, new_pin):
#         self.__pin = new_pin

# atm_card = ATM(1234, 'ayush',60000)

# atm_card.verify_pin(1234)





# class ATM:
#     def __init__(self,pin,name,balance):
#         self.__pin = pin
#         self.name = name
#         self.__balance = balance
#     def verify_pin(self,user_pin):
#         if self.__pin == user_pin:
#             print('User is verified')
#     def change_pin(self, new_pin):
#         self.__pin = new_pin
#     def show_pin(self):
#         print(f'Your pin {self.__pin}')
# atm_card = ATM(1234, 'ayush',60000)

# atm_card.verify_pin(1234)
# atm_card.change_pin(4321)
# atm_card.show_pin()






# class ATM:
#     def __init__(self,pin,name,balance,dob):
#         self.__pin = pin
#         self.name = name
#         self.__balance = balance
#         self.__dob = dob
#     def verify_pin(self,user_pin):
#         if self.__pin == user_pin:
#             print('User is verified')
#     def change_pin(self, new_pin):
#         self.__pin = new_pin
#     def show_pin(self):
#         if self.__dob == input('Enter your dob: '):
#             print(f'Your pin {self.__pin}')
# atm_card = ATM(1234, 'ayush',60000,'04/04/2000')

# atm_card.verify_pin(1234)
# atm_card.change_pin(4321)
# atm_card.show_pin()



class ATM:
    def __init__(self,pin,name,balance,dob):
        self.__pin = pin
        self.name = name
        self.__balance = balance
        self.__dob = dob
    def verify_pin(self,user_pin):
        if self.__pin == user_pin:
            print('User is verified')
    def change_pin(self, new_pin):
        self.__pin = new_pin
    def show_pin(self):
        if self.__dob == input('Enter your dob: '):
            print(f'Your pin {self.__pin}')
        else:
            print('Please, enter the correct detail.')
atm_card = ATM(1234, 'ayush',60000,'04/04/2000')

atm_card.verify_pin(1234)
atm_card.change_pin(4321)
atm_card.show_pin()
