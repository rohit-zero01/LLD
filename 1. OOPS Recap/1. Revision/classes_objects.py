class Student:       #Class
# Varibable inside class is called as attributes
#Initializer or constructor is a special method which is automatically called when object is created.
    def __init__(self, name, age, gender):      #Initializer or constructor
        self.name = name
        self.age = age                  
        self.gender = gender

# Function inside class is called as method.
# it is compulsory to pass self as first parameter in method inside class.

    def display(self):    #Method
        print(f"My name is {self.name}, age is {self.age} and gender is {self.gender}")

s1 = Student("John", 20, "Male")      #Object
# s1.set_info("John", 20, "Male")  
s1.display()