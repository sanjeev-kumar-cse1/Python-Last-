# def add(a,b):
#     print("Addition is performing")
#     return a + b

# a = int(input("Enter first num: "))
# b = int(input("Enter second num: "))
# print("Input has been taken.")

# result = add(a,b)

# print("The result is stored into the result varialbe.")
# print(result)




# Why we need file handling?
# Data store permanently, unlike the variable which we use into the python file.
# They store the data temporary , so, we use the files to store the data permanently.
# To read and write the data efficiently.



# Readline: read one line at a time
# Readlines: read all line at a time in a single list
# Read: Read all line at a time


# #open('filename','mode')
# file = open('data.txt','a') # write
# file.write("\n This is the new files created with the write")
# file.close()

# # file = open('data.txt','r') # read
# # content = file.read()
# # print(content)
# # file.close()
# # # file.read() # After close file will not be readable by any


# file = open('data.txt','r') # read
# # print(len(file.read()))
# # print(file.read())
# # print(file.tell())
# # file.seek(0)
# # print(file.tell())
# # print(file.read())
# # file.close()


# print(file.readline())
# print(file.readlines())
# print(file.read())





file = open('students.txt','r')
print(file.read())




