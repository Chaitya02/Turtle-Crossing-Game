from turtle import Screen
from player import Player
from car import Car
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = Car()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "space")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    if player.ycor() >= 280:
        scoreboard.level_up()
        player.reset()
        car_manager.speed_up()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            is_game_on = False
            scoreboard.game_over()


screen.exitonclick()
