import turtle as t
import random


#Random walk

torti=t.Turtle()
t.colormode(255)
torti.shape("turtle")

def colorAleatorio():
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        color=(r,g,b)
        return color

direcciones=[0,90,180,270]
torti.pensize(10)
torti.speed("fastest")
for i in range(150):
        torti.color(colorAleatorio())
        torti.forward(30)
        torti.setheading(random.choice(direcciones))

pantalla=t.Screen()
pantalla.exitonclick()