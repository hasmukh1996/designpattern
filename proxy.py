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

# proxy.py

import io
import time

from PIL import Image as PILImage
from abc import ABC, abstractmethod


class Image(ABC):
    @abstractmethod
    def show(self):
        pass


class RealImage(Image):
    _IMAGE_PATH = "resources/programmer-meme.jpg"

    def __init__(self):
        img_bytes = self._load_image()
        self._image = PILImage.open(io.BytesIO(img_bytes))

    def _load_image(self):
        with open(self._IMAGE_PATH, "rb") as img:
            return bytearray(img.read())

    def show(self):
        self._image.show()


class ProxyImage(Image):
    def __init__(self):
        self._real_image = None

    def show(self):
        if self._real_image is None:
            self._real_image = RealImage()
        self._real_image.show()


# instantiate objects
proxy_image = ProxyImage()
real_image = RealImage()

proxy_image.show()
time.sleep(1)
