from turtle import Turtle,Screen
import random


#dibuja figuras geometricas desde un triangulo hasta un decahedro con colores aleatorios

torti=Turtle()
torti.shape("turtle")
colors=["cornflower blue","midnight blue","medium sea green","lime green","green yellow","dark khaki","yellow",
        "gold","saddle brown","firebrick","crimson","rosy brown","deep pink"]

#dibuja un cuadrado
# for i in range(4):
#     torti.forward(100)
#     torti.left(90)

#linea punteada
# for i in range(15):
#     torti.forward(10)
#     torti.penup()
#     torti.forward(10)
#     torti.pendown()

def dibuja_figura(num_lados):
    angulo=360/num_lados
    for i in range(num_lados):
        torti.forward(80)
        torti.right(angulo)

for i in range(3,10):
    torti.color(random.choice(colors))
    dibuja_figura(i)

pantalla=Screen()
pantalla.exitonclick()
