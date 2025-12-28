# # This is only for digit
# a = int(input("Enter Num1: ")) 
# b = int(input("Enter Num2: ")) 
# print(a+b)





# # This is also for digit
# a = int(input("Enter Num1: ")) 
# b = int(input("Enter Num2: ")) 
# print(a+b)
# def hello():# This block of code is runable
#     print('Hello from function')
# hello()





# #  This is also for digit but string pass then 'def' block is not work
# a = int(input("Enter Num1: ")) 
# b = int(input("Enter Num2: ")) 
# print(a+b)
# def hello():# This block of code not run
#     print('Hello from function')
# hello()




# try:
#     a = int(input("Enter Num1: ")) 
#     b = int(input("Enter Num2: "))
#     print(a+b)
# except: #if any passing string value
#     print("Some thing unusual has happpend")
# def hello():# This block of code is runable
#     print('Hello from function')
# hello()




# try:
#     a = int(input("Enter Num1: ")) 
#     b = int(input("Enter Num2: "))
#     print(a+b)
# except: #if any passing string value
#     pass
#     # print("Some thing unusual has happpend")
# def hello():# This block of code is runable
#     print('Hello from function')
# hello()




# try:
#     a = int(input("Enter Num1: ")) 
#     b = int(input("Enter Num2: "))
#     print(a+b)
# except ValueError as e: #if any passing string value
#     print("Some thing unusual has happpend", e)
# def hello():# This block of code is runable
#     print('Hello from function')
# hello()




# try:
#     a = int(input("Enter Num1: ")) 
#     b = int(input("Enter Num2: "))
#     c=a+b
# except ValueError as e: #if any passing string value
#     print("Some thing unusual has happpend", e)
# else:
#     print("This is the else block")
#     print("This is the result",c)
# def hello():# This block of code is runable
#     print('Hello from function')
# hello()




# try:
#     print("Try block is running")
#     a = int(input("Enter Num1: ")) 
#     b = int(input("Enter Num2: "))
#     c=a+b
# except ValueError as e: #if any passing string value
#     print("Except block is running")
#     print("Some thing unusual has happpend", e)
# else:
#     print("Else block is running")
#     print("This is the else block")
#     print("This is the result",c)
# def hello():# This block of code is runable
#     print('Hello from function')
# hello()




# try:
#     print("Try block is running")
#     a = int(input("Enter Num1: ")) 
#     b = int(input("Enter Num2: "))
#     c=a+b
# except ValueError as e: #if any passing string value
#     print("Except block is running")
#     print("Some thing unusual has happpend", e)
# else:
#     print("Else block is running")
#     print("This is the else block")
#     print("This is the result",c)
# finally:
#     print("This is always run finally block")
# def hello():# This block of code is runable
#     print('Hello from function')
# hello()




# age = int(input("Enter you age: ")) 
# if age < 0:
#     raise("Please enter your valid age")
# else:
#     print("This is your age:", age)




# # If any give their own age is in negative
# age = int(input("Enter you age: ")) 
# if age < 0:
#     raise Exception("Please enter your valid age")
# else:
#     print("This is your age:", age)




# def age_valid(age):
#     if age < 0:
#         raise Exception ("Please enter your valid age...")
#     print('your age is verified...')
# try:
#     age = int(input("enter your age: "))
#     age_valid(age)
# except:
#     print("something has happend")




def age_valid(age):
    if age < 0:
        raise Exception ("Please enter your valid age...")
    print('Your age is verified...')
try:
    age = int(input("Enter your age: "))
    age_valid(age)
except Exception as e:
    print("Something has happend,", e)
