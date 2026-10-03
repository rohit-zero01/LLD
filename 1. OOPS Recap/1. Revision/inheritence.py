class Animal():
    def __init__(self,  name, age):
        self.name  = name
        self.age = age

    def eat(self):
        print("I am eating")

    def sleep(self):
        print("I am sleeping")

    def move(self):                       #Polymorphism
        print("I am moving")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
        print("This is a dog init")

    def bark(self):
        print("I am barking")

    def display(self):
        print(f"My name is {self.name} and age is {self.age} and my breed is {self.breed}.")

    def move(self):                        #Polymorphism(even if the child and parent has the same method name,
        print("I am moving on 4 legs")     # the method from the child will run, it will completely override the
                                            # parents method with same name.
D1 = Dog("tony", 5, "indie")
D1.display()
D1.move()
#Concept of polymorphism and inheritence both are covered in this file, have to solve the poly problem still.