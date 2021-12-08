#Make a spirograph
import turtle as t
import random

torti=t.Turtle()
t.colormode(255)
torti.shape("turtle")

def colorAleatorio():
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        color=(r,g,b)
        return color


torti.speed("fastest")
def dibuja(size):
        for i in range(int(360/size)):
                torti.color(colorAleatorio())
                torti.circle(100)
                torti.setheading(torti.heading()+10)


dibuja(5)
pantalla=t.Screen()
pantalla.exitonclick()