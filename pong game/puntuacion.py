from turtle import Turtle

class Puntuacion(Turtle):
    def __init__(self):
        super().__init__()
        self.color("snow")
        self.penup()
        self.hideturtle()
        self.l_puntuacion=0
        self.r_puntuacion=0
        self.actualizaPuntos()
    
    def actualizaPuntos(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_puntuacion,align="center",font=("Courier",80,"normal"))
        self.goto(100,200)
        self.write(self.r_puntuacion,align="center",font=("Courier",80,"normal"))
    
    def l_puntos(self):
        self.l_puntuacion+=1
        self.actualizaPuntos()
    
    def r_puntos(self):
        self.r_puntuacion+=1
        self.actualizaPuntos()