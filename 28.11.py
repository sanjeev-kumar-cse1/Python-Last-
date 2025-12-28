# def greet():
#     print("Hellow,Vinay")
# greet()



# def decorator(func):
#     def wrapper():
#         print('Yeh functionality incraese kr rha hai')
#         func()
#     return wrapper
# @decorator
# def greet():
#     print("Hellow,Vinay")
# greet()




# def decorator(func):
#     def wrapper():
#         print('Yeh functionality incraese kr rha hai')
#         func()
#     return wrapper
# @decorator
# def greet():
#     print("Hellow,Vinay")
# greet()
# @decorator
# def hi():
#     print('This message from hi function')
# hi()




# from abc import ABC , abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass
#     @abstractmethod
#     def stop(self):
#         pass
#     def dashboard(self):
#         pass
# class Car(Vehicle):
#     def start(self):
#         print('The car will startr from key')
#     def stop(self):
#         print('car stoped')
# class Bike(Vehicle):
#     def start(self):
#         print('The bike will start from kick or self ')
#     def stop(self):
#         print('Bike stoped ')
# c = Car()
# c.start()
# b = Bike()
# b.start()



from abc import ABC , abstractmethod

class Payment(ABC):
    @abstractmethod
    def payment(self):
        pass
    def offer(self):
        print('This offer is from credit-card')
class CreditCardPayment(Payment):
    def payment(self):
        print('The payment is done by the credit card.')
class UPI(Payment):
    def payment(self):
        print('The payment done by UPI')
upi = UPI()
upi.payment()
credit = CreditCardPayment()
credit.payment()
credit.offer()
