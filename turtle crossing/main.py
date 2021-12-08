import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player=Player()
car=CarManager()
score=Scoreboard()
screen.listen()
screen.onkey(player.go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()

    #detecta colision con los carros
    for carrito in car.all_cars:
        if carrito.distance(player)<20:
            game_is_on=False
            score.game_over()
    
    #detecta cuando la tortuga cruzo
    if player.crossing():
        player.go_to_start()
        car.level_up()
        score.increase_level()
            
screen.exitonclick()