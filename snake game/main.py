from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Ulises|Snake Game")
screen.tracer(0)


snake=Snake()
food=Food()
score=Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

juego_encendido=True
while juego_encendido:
    screen.update()
    time.sleep(0.1)
    snake.mueve()
    #detectar cuando come   
    if snake.head.distance(food)<15:
        food.masComida()
        snake.crece()
        score.incrementaPuntuacion()
    
    #detectar choque con la pared
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        score.resetear()
        snake.resetear()

    #detectar choque entre ella
    for segmento in snake.segmentos[1:]:
        if snake.head.distance(segmento)<10:
            score.resetear()
            snake.resetear()
screen.exitonclick()