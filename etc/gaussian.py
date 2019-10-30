import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import cv2


def get_image(url):
    return mpimg.imread(url)


def edges(img):
    base = np.ones((5, 5))
    middle_x = 2
    middle_y = 2
    kernel = np.array([[gaussian(value, x, y, middle_x, middle_y) for x, value in enumerate(row)]
                       for y, row in enumerate(base)])
    return cv2.filter2D(img, -1, kernel)


def gaussian(value, x, y, middle_x, middle_y):
    """
    I'm not sure if this is technically a Gaussian. The idea is that the kernel exponentially decays
    as the distance gets farther from the center.
    :param value: The base value.
    :param x: The x coordinate.
    :param y: The y coordinate.
    :param middle_x: The middle of the image's x coordinate.
    :param middle_y: The middle of the image's y coordinate.
    :return: The value after the Gaussian shift.
    """
    delta_x = x - middle_x
    delta_y = y - middle_y
    distance = np.sqrt(delta_x ** 2 + delta_y ** 2)
    multiplier = 1 - np.exp(-distance)
    return value * multiplier


def show(img):
    plt.imshow(img)
    plt.show()

# Read Image
url = 'https://cdn.sstatic.net/Sites/stackoverflow/img/logo.png'
img = get_image(url)
show(img)

edgy = edges(img)
show(edgy)
