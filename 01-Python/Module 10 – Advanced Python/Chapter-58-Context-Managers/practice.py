# class MyContext:

#     def __enter__(self):
#         print("Entering context")

#     def __exit__(self, exc_type, exc_value, traceback):
#         print("Exiting context")


# with MyContext():
#     print("Inside context")

class MyContext:
    def __enter__(self):
        print("Entering context")
        return "Hello from context"

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")


# with MyContext() as value:
#     print(value)

class FileSession:
    def __enter__(self):
        print("Opening session")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing session")


# with FileSession():
#     print("Working...")

from contextlib import contextmanager

@contextmanager
def session():
    # print("Opening session")
    try:
        yield "Session is ready"
    finally:
        print("Closing session")


# with session() as value:
#     print(value)

from contextlib import contextmanager

@contextmanager
def managed():
    print("Start")
    try:
        yield
    finally:
        print("Cleanup")

# with managed():
#     print("Doing work")
#     raise ValueError("Oops")

from contextlib import contextmanager

@contextmanager
def managed():
    try:
        yield
    except ValueError:
        print("Handled")
    print("After with")
        
# with managed():
#     raise ValueError("Oops")

from contextlib import contextmanager

@contextmanager
def managed():
    print("Acquire")
    try:
        yield "resource"
    finally:
        print("Release")

with managed() as item:
    print(item)
    raise RuntimeError("Failure")

print("Finished")