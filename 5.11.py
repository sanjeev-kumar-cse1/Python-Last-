
# # CSV Module : 
# import csv  # This line open the data .csv file as in read mode
# with open('data.csv', 'r') as data: # This line read the content of csv module
#     content = csv.reader(data)
#     for row in content:
#         print(row)

# with open('data.csv','w') as data:
#     writer = csv.writer(data)
#     writer.writerow(['Name', 'Age', 'Branch'])
#     writer.writerow(['Sanjeev', 20, 'CSE'])
#     writer.writerow(['Kumar', 30, 'EE'])




import csv
with open('data.csv','a', newline='') as data:
    writer = csv.writer(data)
    row = int(input("Here you have to enter your rows: "))
    i = 1
    writer.writerow(['Name', 'Age', 'Branch'])
    while i <= row:
        Name = input("Enter name: ")
        Age = int(input("Enter Age: "))
        Branch = input("Enter Branch: ")
        writer.writerow([Name, Age, Branch])
        i += 1
