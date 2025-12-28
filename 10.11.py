# # In Python, exceptions are events that disrupt the normal flow of a program's execution due to an error or an unexpected condition. They are a mechanism for handling runtime errors gracefully, preventing program crashes, and allowing for robust error management.


# a = int(input("enter value"))
# b = int(input("enter value"))
# res = a / b  # a =10 ,b = 0 here not divisible
# print(res)



# # This gives error
# a = int(input("enter value"))
# b = int(input("enter value"))
# res = a / b
# print("Hello")
# print(res)


# a = int(input("enter value "))
# b = int(input("enter value "))
# try:
#     res = a / b
# except ZeroDivisionError:
#     print("Some thing is wrong , and number will not divisible by 0")
# print("This will run in any condition ")



# a = int(input("enter value "))
# b = int(input("enter value "))
# try:
#     res = a / b
# except ZeroDivisionError as e:
#     print("Some thing is wrong and number will not divisible by 0", e) # if b!=0 then this is not print
# print("This will run in any condition.")



# # Here code is runable but after giving the value occurs errors because here 'c' is not defined
# a = int(input("enter value "))
# b = int(input("enter value "))
# try:
#     res = a / b
# except ZeroDivisionError as e:
#     print("Some thing is wrong and number will not divisible by 0", e)
# print("This will run in any condition.")
# print(c)


# THis is runable
# try:
#     print(c)
# except:
#     print("Something ")
# print("This is the line  ")


# # error
# try:
#     print(c)
# except NameError as e:
#     print("Something happened.", e)
# print("This is the line run after except.")
# print(c)



# # Indentation error handle
# age = 20
# try:
#     if age > 18:
#         print("This is")
# except IndentationError as e:
#     print("Something happened.", e)
# print("This is the line run after except.")




# a = "10"
# try:
#     b = int(a)
# except ValueError as e:
#     print(e)



# try:
#     with open('file.txt', 'r') as f:
#         print( f.read())
# except FileNotFoundError as e:
#     print(e)
# print("THis is exception")



# try:
#     with open('file.txt', 'w') as f:
#         f.write("This is the text")
# except FileNotFoundError as e:
#     print(e)
# print("THis is exception")



try:
    with open('file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError as e:
    print(e) # Here any error may be give.
else: 
    print(content)
finally:
    print("This will run always")
print("THis is exception handle")