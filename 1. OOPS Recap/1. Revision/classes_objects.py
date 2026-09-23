class Student:       #Class
# Varibable inside class is called as attributes
    name = ""       #Attributes
    age = 0
    gender = ""

#Function inside class is called as method.
#it is compulsory to pass self as first parameter in method inside class.
    def set_info(self):             #Method
        self.name = input("Enter your name: ") 
        self.age = int(input("Enter your age: "))
        self.gender = input("Enter your gender: ")
    

    def display(self):    #Method
        print(f"My name is {self.name}, age is {self.age} and gender is {self.gender}")

s1 = Student()      #Object
s1.set_info()
s1.display()