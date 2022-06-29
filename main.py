# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#Decorator

def div(a,b):
    print(a/b)

div(5,10)

def smart_div(func):
    def inner(a,b):
        if a < b :
            a,b = b ,a
            return func(a,b)
    return inner

div = smart_div(div)
div(5,10)

# decorator_func_py
def entry_exit(func):
    def wrapped_func():
        print(f"Entering {func.__name__}")
        func()
        print(f"Exiting {func.__name__}")

    return wrapped_func


@entry_exit
def my_func():
    print("Inside my_func")


my_func()


# decorator_class.py

class EntryExit:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print(f"Entering {self.func.__name__}")
        self.func()
        print(f"Exiting {self.func.__name__}")


entry_exit = EntryExit  # enforce PEP8 compliance. useful? debatable!


@entry_exit
def my_func():
    print("Inside my_func")


my_func()

