# class = blueprint
# object = 
# __init__ = memory allocate for the current variable



# class villa:
#     pass
# brother_ghr = villa()
# tumhara_ghr = villa()
# print(brother_ghr) # different memory address
# print(tumhara_ghr) # different memory address



# class villa: 
#     boundary = 'Fencing' # class attribute

#     def __init__(self, color_diya): # constructor
#         self.color = color_diya # jo object create hota hai use hi hum

# brother_ghr = villa('Green')
# tumhara_ghr = villa('Yellow')
# print(brother_ghr.color) # Green
# print(tumhara_ghr.color) # Yellow




# # For count how many objects are here
# class Counter:
#     count = 0  # \ class variable for counting objects , this is also class-attribbute

#     def __init__(self, color_diya):  # constructor
#         Counter.count += 1  # increase count each time an object is created

# obj1 = Counter()
# # obj2 = Counter()
# # obj3 = Counter()
# # obj4 = Counter()
# # obj5 = Counter()
# # obj6 = Counter()
# print("Total Counter created:", Counter.count)





class villa: 

    def __init__(self, color_diya): # constructor
        self.color = color_diya # jo object create hota hai use hi hum

    def change_color(self, new_color):
        self.color = new_color
        
tumhara_ghr = villa('Yellow')
print(f'at the time of the home creation: {tumhara_ghr.color}') # Yellow

tumhara_ghr = villa('Voilet')
print(f'The color of your house has been changed: {tumhara_ghr.color}') # Voilet

