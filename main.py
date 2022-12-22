from turtle import Turtle, Screen
from player import Player
from dot import Dot

# Variables 
multiplier = 1.5

# Scren setup
screen = Screen()
screen.setup(500, 500)
screen.title("Dots Game")
screen.bgcolor("#98EDCD")

# Create objects for player and dot
ply = Player()
enemy = Dot()


screen.exitonclick()