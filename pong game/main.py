
from turtle import Turtle,Screen
from jugador import Jugador
from pelotita import Pelotita
import time
from puntuacion import Puntuacion

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Ulises JE | Pong")
screen.tracer(0)

r_jugador=Jugador((350,0))
l_jugador=Jugador((-350,0))
ball=Pelotita()
puntuacion=Puntuacion()

screen.listen()
screen.onkey(r_jugador.ir_arriba,"Up")
screen.onkey(r_jugador.ir_abajo,"Down")
screen.onkey(l_jugador.ir_arriba,"w")
screen.onkey(l_jugador.ir_abajo,"s")

jugando=True
while jugando:
    time.sleep(ball.mueve_rapido)
    screen.update()
    ball.mueve()

    #detecta el choque con la pared superior o inferior
    if ball.ycor()>280 or ball.ycor()<-280:
        #debe rebotar
        ball.rebotay()
    
    #detecta choque con r_jugador
    if ball.distance(r_jugador)<50 and ball.xcor()>320 or ball.distance(l_jugador)<50 and ball.xcor()<-320:
        ball.rebotax()
        
    #detecta cuando el jugador de la derecha pierde
    if ball.xcor()>380 :
        ball.resetear()
        puntuacion.l_puntos()
        

    #detectar cuando el jugador de la izquierda pierde
    if ball.xcor()<-380 :
        ball.resetear()
        puntuacion.r_puntos()


screen.exitonclick()