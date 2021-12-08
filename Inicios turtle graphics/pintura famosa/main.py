# import colorgram

# colores=colorgram.extract("day 18 intermediate turtle/puntos.jpg",30)
# rgb_colors=[]
# for color in colores:
#     r=color.rgb.r 
#     g=color.rgb.g
#     b=color.rgb.b
#     nuevo_color=(r,g,b)
#     rgb_colors.append(nuevo_color)

# print(rgb_colors)
import turtle as t
import random

lista_colores=[(58, 106, 148), (224, 200, 110), (134, 84, 58), (223, 138, 62), (196, 145, 171), 
(234, 226, 204), (224, 234, 230), (142, 178, 203), (139, 82, 105), (208, 90, 69), (237, 225, 233), 
(188, 80, 120), (69, 105, 90), (133, 182, 135), (133, 133, 74), (64, 156, 92), (47, 156, 193), 
(183, 192, 201), (213, 177, 191), (19, 58, 92), (20, 68, 113), (113, 123, 149), (227, 174, 166), 
(172, 203, 183), (156, 206, 217), (69, 58, 47), (72, 64, 53), (111, 46, 59), (53, 70, 64)]

torti=t.Turtle()
t.colormode(255)
torti.shape("turtle")
torti.speed("fastest")
torti.penup()
torti.hideturtle()

torti.setheading(225)
torti.forward(320)
torti.setheading(0)
puntosTotales = 100

for i in range(1, puntosTotales + 1):
    torti.dot(20, random.choice(lista_colores))
    torti.forward(50)

    if i % 10 == 0:
        torti.setheading(90)
        torti.forward(50)
        torti.setheading(180)
        torti.forward(500)
        torti.setheading(0)

pantalla=t.Screen()
pantalla.exitonclick()