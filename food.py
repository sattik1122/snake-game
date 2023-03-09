from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

    def new_food(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
