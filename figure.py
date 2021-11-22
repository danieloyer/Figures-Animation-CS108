"""CS 108 Homework 6

This module implements a model for a rectangle figure in the animation. **DRIVER**

@author: Daniel Oyer (ddo4)
@date: Fall, 2021
"""


class Figure:
    """Figure models a singular rectangular figure to be rendered on a canvas."""
    def __init__(self, x, y, l, w, color):
        """initializes a rectangle figure"""
        self.x = x
        self.y = y
        self.l = l
        self.w = w
        self.color = color
        self.area = self.l * self.w

    def draw(self, drawing):
        """calculates coordinates and draws a rectangle figure"""
        x1 = int(self.x - self.l / 2)
        y1 = int(self.y - self.w/2)
        x2 = int(self.x + self.l/2)
        y2 = int(self.y + self.w/2)
        drawing.rectangle(x1, y1, x2, y2, self.color)