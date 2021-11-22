"""CS 108 Homework 6

This module implements a GUI for the rectangle figure animation. **GUI**

@author: Daniel Oyer (ddo4)
@date: Fall, 2021
"""

from guizero import Box, Drawing, PushButton, App, Text
from figure import Figure
from helpers import get_random_color
from random import randint


class FigureAnimation:
    """Figure Animation runs an animation of rectangular figures being added to a drawing canvas."""

    def __init__(self, app):
        """Builds the figures interface"""
        self.figure_list = []
        app.title = "Squares"
        self.area_text = 0
        app.text_size = 12
        unit = 500
        control_unit = unit + 50
        app.width = unit
        app.height = control_unit

        # Widgets
        box = Box(app, layout='grid', width=unit, height=unit + control_unit)
        self.drawing = Drawing(box, width=unit, height=unit, grid=[0, 0, 4, 1])
        PushButton(box, text='clear', grid=[0, 2], align='left', command=self.clear_frame)
        PushButton(box, text='quit', grid=[3, 2], align='right', command=app.destroy)
        self.area_text = Text(box, text='total area: {}'.format(self.area_text), grid=[2, 2])
        self.drawing.bg = 'black'
        self.drawing.when_clicked = self.clear_frame
        app.repeat(30, self.draw_frame)
        app.repeat(30, self.calculate_area)

    def calculate_area(self):
        area = 0
        for i in self.figure_list:
            area += i.area
        self.area_text.value = 'total area: {}'.format(area)

    def draw_frame(self):
        """sets figure drawing on the canvas"""
        x = randint(0, app.width)
        y = randint(0, app.height)
        l = randint(10, 50)
        w = randint(5, 30)
        draw_figure = Figure(x, y, l, w, color=get_random_color())
        self.figure_list.append(draw_figure)
        draw_figure.draw(self.drawing)

    def clear_frame(self):
        """clears the canvas by mouse-click or pressing clear button"""
        self.figure_list = []
        self.drawing.clear()


app = App()
figure1 = FigureAnimation(app)
app.display()
