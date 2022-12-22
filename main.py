from turtle import Turtle, Screen
from player import Player
from dot import Dot

import time

# Variables 
multiplier = 1.2
move_amount = 1

# Scren setup
screen = Screen()
screen.setup(500, 500)
screen.title("Dots Game")
screen.bgcolor("#98EDCD")

# Create objects for player and dot
enemy = Dot()
ply = Player()

# Check for key presses
screen.listen()
screen.onkey(ply.up, "w")
screen.onkey(ply.down, "s")
screen.onkey(ply.left, "a")
screen.onkey(ply.right, "d")

# Create the main game loop
game_is_running = True

while game_is_running:
    ply.move(move_amount)
    
    if ply.is_colliding_with_enemy(enemy.get_position()):
        ply.increase_size(multiplier)
        enemy.move()
    
    if ply.is_colliding_with_wall(screen.screensize()):
        game_is_running = False
        screen.clearscreen()
        screen.bgcolor("black")

screen.exitonclick()