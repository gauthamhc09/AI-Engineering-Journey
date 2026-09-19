from abc import ABC, abstractmethod

class Payment(ABC):
    
    def log_transaction(self):
        print("Logging Transaction")
        
    @abstractmethod
    def pay(self):
        pass
    
class CreditCardPayment(Payment):
    
    def pay(self):
        print("Credit card payment")
        
class UPIPayment(Payment):
    
    def pay(self):
        print("UPI payment")
    
payments = [CreditCardPayment(), UPIPayment()]

class Animal:
    
    def sound(self):
        print("sound")

class Dog(Animal):
    
    def sound(self):
        print("Boww")
        
class Cat(Animal):
    
    def sounndd(self):
        pass

animals = [Dog(), Cat()]


for animal in animals:
    animal.sound()
    
for payment in payments:
    payment.log_transaction()
    
class LLM(ABC):

    @abstractmethod
    def generate_text(self, prompt: str):
        pass
    
class OPENAI(LLM):
    
    def generate_text(self, prompt):
        print(f"Open AI, {prompt}")
        
class gemini(LLM):
    
    def generate_text(self, prompt):
        print(f"Open AI, {prompt}")
        
models = [OPENAI(), gemini()]

for model in models:
    model.generate_text("hello")