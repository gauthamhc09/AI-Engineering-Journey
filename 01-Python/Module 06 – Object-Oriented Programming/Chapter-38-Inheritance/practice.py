class Employee:
    
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        return f"I am {self.name}"
    

class Developer(Employee):
    pass

developer = Developer("Gautham")

# print(developer.introduce())

print(type(developer))

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_info(self):
        print(f"Vehicle brand: {self.brand} ")
    
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
        
    def show_info(self):
        return f"Car: {self.brand} {self.model}"
    

       
car1 = Car("Toyota", "Corolla")
print(car1.show_info())


class A:
    def show_info(self):
        print("A")
        
class B:
    def show_info(self):
        print("B")
        
class C(A, B):
    pass

c = C
print(c.__mro__)
