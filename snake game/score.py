from turtle import Turtle

ALINEAR="center"
ESTILOS=("Arial",20,"normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("Juegos con turtle graphics/snake game/score.txt") as data:
            self.high_score=int(data.read())
        self.color("snow")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.actualizaPuntuacion()
    
    def actualizaPuntuacion(self):
        self.clear()
        self.write(f"Score:{self.score}  High score:{self.high_score}",align=ALINEAR,font=ESTILOS)

    def resetear(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("Juegos con turtle graphics/snake game/score.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.actualizaPuntuacion()
    # def juegoTerminado(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER",align=ALINEAR,font=ESTILOS)
        
    def incrementaPuntuacion(self):
        self.score+=1
        self.actualizaPuntuacion()
    

        