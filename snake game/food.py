from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("dark turquoise")
        self.speed("fastest")
        self.masComida()
    
    def masComida(self):
        ranX=random.randint(-280,280)
        ranY=random.randint(-280,280)
        self.goto(ranX,ranY)