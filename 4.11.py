# book = open('data4.txt', 'w')
# # print(book.read())
# book.write("This is my book.")
# book.write("This is my book for not sale.")
# book.close()

# # book = open('data4.txt', 'w')
# # book.write("This is my book for not sale new line.")
# # book.close()

# book = open('data4.txt', 'a')
# book.write("\nThis is my book for not sale new line.")
# book.close()





# notebook = open('notebook4.txt','w')
# notebook.write("This is the text from the write mode")
# # notebook.writeline('This is writeline')
# # notebook.writelines('This is  writelines')
# notebook.writelines(['\nThis is', '\n writelines'])
# notebook.close()




# notebook = open('notebook4.txt','r')
# print(notebook.tell()) # This is 0 start this count words length

# print(notebook.readline()) # First line print and give space
# print(notebook.readline()) # This print another line and space
# print(notebook.readline()) # This print another line and space
# print(notebook.tell()) # here is 67 word length
# print(notebook.seek(0)) # here fix 0 so print 0 seek time

# print(notebook.readline()) # If all line printed then again starting line print




## error show
# with open('notebook.txt') as notebook:
#     print(notebook.read())
# print(notebook.read())



# with open('notebook4.txt') as notebook4:
#     for line in notebook4.readlines:
#         print(line)
        
        
        
        
with open('notebook4.txt') as notebook4: # file automatic close
    print(notebook4.read(20))