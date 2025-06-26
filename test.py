#Single level inheritance
# class A:
#     def test1(x):
#         print("this")


# class B(A):
#     def test2(x):
#         print("Hello")
# t=B()
# t.test1()
# t.test2()

# def my_function():
#   print("Hello from a function")

# my_function()



###SINGLE LEVEL WITH SUPER() Functionclass A():class A():
#     def __init__(self,brand,color):
#         self.brand= brand
#         self.color=color

#     def show(self):
#         print(f"{self.brand} car is {self.color}")

# obj= A("BMW","Blue")
# obj.show()
#     def __init__(self,brand,color):
#         self.brand= brand
#         self.color=color

#     def show(self):
#         print(f"{self.brand} car is {self.color}")

# obj= A("BMW","Blue")
# obj.show()
# class Parent:
#     def show1(self):
#         print("Parent")

# class Child(Parent):
#     def show2(self):
#         super().show()  #super function is used to call methods from parent class/base class.
#         print("Child")

# c = Child()
# c.show1()

###HYBRID INHERITACE
# class A:
#     def funA(self):class A():
#     def __init__(self,brand,color):
#         self.brand= brand
#         self.color=color

#     def show(self):class A():
#         print(f"{self.brand} car is {self.color}")

# obj= A("BMW","Blue")
# obj.show()
#         print("R")

# class D(B,C):
#     def funD(self):
#         super().funA()
#         print("T")
# class A():
#     def __init__(self,brand,color):
#         self.brand= brand
#         self.color=color

#     def show(self):
#         print(f"{self.brand} car is {self.color}")

# obj= A("BMW","Blue")
# obj.show()
# obj= D()
# # obj.funA()
# # obj.funB()
# # obj.funC()
# obj.funD()

###inheritance(single) with self paramater (reference to current instance of class)
# class Empolyee():
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def show(self):
#         print(f"{self.name} earns {self.salary}")
        

# class Developer(Empolyee):
#     def __init__(self, name, salary, language):
#         self.name = name
#         self.salary = salary
#         self.language = language

#     def show_dev(self):  
#         print(f"{self.name} codes in {self.language}")

# ev = Developer("Sarthak", "55000", "Python")
# ev.show()
# ev.show_dev()


##class and object
## a blueprint of creating object
##An instance of class
class A():
    def __init__(self,brand,color):
        self.brand= brand
        self.color=color

    def show(self):
        print(f"{self.brand} car is {self.color}")

obj= A("BMW","Blue")
obj.show()


##Inheritance (one class can use the feature of another class)
 
class A():
    def sarth1(self):
        print("HELLO")
class B(A):
    def sarth2(self):
        print("WORLD")

o=B()
o.sarth1()
o.sarth2()


##Encapsulation = hiding internal details of ho things work/ Protecting data using private variables (_ or __).
class Account():
    def __init__(self,balance):
        self.__balance=balance  ##private variable
    
    def show_balance(self):
        print(f"Balance is: {self.balance}")
acc=Account(2000)
acc.show_balance()


###Polymorphism = Same function behaves different depending on the object / one method , different behaviour

class Cat():
    def speak(self):
        print("M")

class Dog():
    def speak(self):
        print("B")

for animal in [Cat(),Dog()]:
    animal.speak()

##function 
def test():
    print("Hello")

test()



























        