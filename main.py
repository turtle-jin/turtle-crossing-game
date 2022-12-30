import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing Game")
screen.listen()


player = Player()
car_manager = CarManager()
screen.onkeypress(player.up, "Up") # when calling methods inside listener, we dont add ( )
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.car_move()
    # print(car_manager.all_cars)
    # check if the turtle player collides with the car
    for cars in car_manager.all_cars:
        if player.distance(cars) <= 20:
            game_is_on = False
            scoreboard.game_over()

    # check if the turtle player has reached the top edge of the screen
    if player.ycor() >= 280:
        player.go_to_start()
        car_manager.level_up()
        scoreboard.level_upgrade()





screen.exitonclick()