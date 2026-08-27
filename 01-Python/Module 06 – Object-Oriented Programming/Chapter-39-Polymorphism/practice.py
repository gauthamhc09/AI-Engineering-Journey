class Animal:
    def speak(self):
        print("Animal speaks")


class Dog():
    def speak(self):
        print("Woof")


class Cat():
    def speak(self):
        print("Meow")
        
animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal.speak()