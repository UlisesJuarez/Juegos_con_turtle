from turtle import Turtle

class Pelotita(Turtle):

    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.shape("circle")
        self.penup()
        self.mueveX=10
        self.mueveY=19
        self.mueve_rapido=0.1   

    def mueve(self):
        nuevaX=self.xcor()+self.mueveX
        nuevaY=self.ycor()+self.mueveY
        self.goto(nuevaX,nuevaY)

    
    def rebotay(self):
        self.mueveY*=-1
    
    def rebotax(self):
        self.mueveX*=-1
        self.mueve_rapido *=0.9
    
    def resetear(self):
        self.goto(0,0)
        self.mueve_rapido=0.1
        self.rebotax()