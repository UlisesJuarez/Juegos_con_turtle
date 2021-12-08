from turtle import Turtle

class Jugador(Turtle):
    def __init__(self,posicion):
        super().__init__()
        self.shape("square")
        self.color("snow")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(posicion)
    
    def ir_arriba(self):
        nuevaY=self.ycor()+20
        self.goto(self.xcor(),nuevaY)

    def ir_abajo(self):
        nuevaY=self.ycor()-20
        self.goto(self.xcor(),nuevaY)





