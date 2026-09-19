from functools import wraps

def add_stars(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("⭐⭐⭐ START STARS ⭐⭐⭐")
        func(*args, **kwargs)
        print("⭐⭐⭐ END STARS ⭐⭐⭐")
    return wrapper

def add_hashes(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("### START HASHES ###")
        func(*args, **kwargs)
        print("### END HASHES ###")
    return wrapper

# @add_stars
# @add_hashes
# def display_message():
#     print('Hello')

# display_message()

# def display_message():
#     print('Hello')

# display_message = add_stars(add_hashes(display_message))

def first(func):

    def wrapper():
        print("First")
        func()

    return wrapper


def second(func):

    def wrapper():
        print("Second")
        func()

    return wrapper


@first
@second
def hello():
    print("Hello")
    
# hello()

def first(func):

    def wrapper():
        print("First before")
        func()
        print("First after")

    return wrapper


def second(func):

    def wrapper():
        print("Second before")
        func()
        print("Second after")

    return wrapper


@first
@second
def hello():
    print("Hello")


hello()