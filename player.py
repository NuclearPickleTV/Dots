from turtle import Turtle
from dot import Dot

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Player:
    """The Player of the game"""

    def __init__(self):
        super().__init__()
        self.size = 0.5

        self.circle = Turtle()
        self.circle.shape("circle")
        self.circle.color("red")
        self.circle.shapesize(self.size)
        self.circle.penup()

    def increase_size(self, multiplier):
        """Icrease the size of the player by a specific multiplier"""

        self.size = self.size * multiplier
        self.circle.shapesize(self.size)
    
    def move(self, move_amount):
        """Move the Player forwards"""

        self.circle.forward(move_amount)

    def up(self):
        """Set the heading of the player to UP"""

        if self.circle.heading() != UP:
            self.circle.setheading(UP)

    def down(self):
        """Set the heading of the player to DOWN"""

        if self.circle.heading() != DOWN:
            self.circle.setheading(DOWN)
    
    def left(self):
        """Set the heading of the player to LEFT"""

        if self.circle.heading() != LEFT:
            self.circle.setheading(LEFT)
    
    def right(self):
        """Set the heading of the player to RIGHT"""

        if self.circle.heading() != RIGHT:
            self.circle.setheading(RIGHT)

    def is_colliding_with_enemy(self, enemy):
        """Detect whether or not the player is colliding with an enemy, must provide enemy object. Returns True or False"""

        if self.circle.distance(enemy) < self.size + 15:
            return True
        else:
            return False

    def is_colliding_with_wall(self, screenSize):
        """Detects whether or not a player is colliding with the wall of the game window, returns True or False"""

        if self.circle.xcor() > 249 or self.circle.xcor() < -249 or self.circle.ycor() > 249 or self.circle.ycor() < -249:
            return True
        else:
            return False