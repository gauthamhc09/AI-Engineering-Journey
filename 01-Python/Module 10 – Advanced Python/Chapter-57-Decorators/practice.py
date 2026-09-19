
    
def my_decorator(orgn_func):
    
    def wrapper(name):
        print("*** Wrapping Paper Before ***")
        orgn_func(name)
        print("*** Wrapping Paper After ***")
        
    return wrapper

# boxed_gift = my_decorator(greet)
# boxed_gift()
@my_decorator
def greet(name):
    print(f"Hello World! - {name}")

# greet("Alice")

def universal_decorator(orgn_func):
    def wrapper(*args, **kwargs):
        print(" -- Start Here --")
        result = orgn_func(*args, **kwargs)
        print(" -- Stop Here --")
        return result
    return wrapper

@universal_decorator
def greet_unvi(name, age, city):
    print(f"Hello world - I am {name} my age is {age}. I am from {city}")
    
# greet_unvi("gautham", 34, "Bengaluru")

import time

def monitor_ai_latency(orgn_func):
    
    def wrapper(*args, **kwargs):
        print("TIme started")
        start_time = time.time()
        
        result = orgn_func(*args, **kwargs)
        
        end_time = time.time()
        print("TIme stopped")
        latency = end_time - start_time
        print(f"for runnning this func it took {latency} time")
        return result
    
    return wrapper

@monitor_ai_latency
def short_ai(user_prompt):
    time.sleep(1.2)
    return f"Hello I am a short AI - {user_prompt}"

@monitor_ai_latency
def long_ai(user_prompt):
    time.sleep(4.2)
    return f"Hello I am a short AI - {user_prompt}"
# if __name__ == "__main__":
#     qwen = short_ai("Qwen-2.5")
#     print(qwen)
    
#     openai = long_ai("OPENAI-5.6")
#     print(openai)
    
    

from functools import wraps

def uppercase_decorator(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_decorator
def greet(name):
    """Greets a person."""
    return f"hello {name}"

# print(greet("Angel"))
# print(greet.__name__)
# print(greet.__doc__)

def repeat(times):
    def decorator(func):
        def wrapper():
            for _ in range(times):
                func()
        return wrapper
    print(times)
    return decorator

@repeat(3)
def greet():
    print("Hello")

greet()