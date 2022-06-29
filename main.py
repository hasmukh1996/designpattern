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

# composite.py

from abc import abstractmethod


class Commodity:
    @abstractmethod
    def get_price(self):
        pass


class Product(Commodity):
    def __init__(self, price):
        self.price = price

    def get_price(self):
        return self.price


class Box(Commodity):
    def __init__(self):
        self._children = []

    def add(self, item: Commodity):
        self._children.append(item)

    def remove(self, item: Commodity):
        self._children.remove(item)

    def get_price(self):
        price = 0
        for child in self._children:
            price += child.get_price()
        return price


# put some phones into a box
iphone13 = Product(1300)
pixel6 = Product(600)

phones = Box()
phones.add(iphone13)
phones.add(pixel6)

# put some consoles into a box
xbox = Product(300)
ps5 = Product(800)

consoles = Box()
consoles.add(xbox)
consoles.add(ps5)

# put the boxes in a even bigger box
moving_box = Box()
moving_box.add(phones)
moving_box.add(consoles)

# calculate prices
print(moving_box.get_price())
print(phones.get_price())
