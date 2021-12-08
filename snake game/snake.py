from turtle import Turtle

POSICIONES_INICIALES=[(0,0),(-20,0),(-40,0)]
MUEVE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segmentos=[]
        self.creaSerpiente()
        self.head=self.segmentos[0]

    def creaSerpiente(self):
        for i in POSICIONES_INICIALES:
            nuevo=Turtle("square")
            nuevo.color("white")
            nuevo.penup()
            nuevo.goto(i)
            self.segmentos.append(nuevo)

    def mueve(self):
        for seg_num in range(len(self.segmentos)-1,0,-1):
            nuevaX=self.segmentos[seg_num-1].xcor()
            nuevaY=self.segmentos[seg_num-1].ycor()
            self.segmentos[seg_num].goto(nuevaX,nuevaY)
        self.head.forward(MUEVE)
    def add_segmento(self,posicion):
        nuevo=Turtle("square")
        nuevo.color("white")
        nuevo.penup()
        nuevo.goto(posicion)
        self.segmentos.append(nuevo)

    def resetear(self):
        for seg in self.segmentos:
            seg.goto(1000,1000)
        self.segmentos.clear()
        self.creaSerpiente()
        self.head=self.segmentos[0]

    def crece(self):
        self.add_segmento(self.segmentos[-1].position())
    def up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() !=UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() !=RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() !=LEFT:
            self.head.setheading(RIGHT)
    