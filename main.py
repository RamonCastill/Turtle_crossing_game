import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Crossing Turtle Game")
screen.tracer(0)

scoreboard = Scoreboard()

player = Player()

screen.listen()
screen.onkey(player.up, "Up")

cars = []
for _ in range(0, 30):
    new_car = CarManager()
    cars.append(new_car)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in cars:
        car.move()

    for car in cars:
        if car.xcor() < -300:
            car.go_back()
    for car in cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() == player.finish:
        player.restart()
        scoreboard.increase_score()
        for car in cars:
            car.reset_position()


screen.exitonclick()
