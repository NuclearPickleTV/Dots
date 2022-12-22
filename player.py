from turtle import Turtle
from dot import Dot

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Player:
    def __init__(self):
        super().__init__()
        self.size = 0.5

        self.circle = Turtle()
        self.circle.shape("circle")
        self.circle.color("red")
        self.circle.shapesize(self.size)
        self.circle.penup()

    def increase_size(self, multiplier):
        self.size = self.size * multiplier
        self.circle.shapesize(self.size)
    
    def move(self, move_amount):
        self.circle.forward(move_amount)

    def up(self):
        if self.circle.heading() != UP:
            self.circle.setheading(UP)

    def down(self):
        if self.circle.heading() != DOWN:
            self.circle.setheading(DOWN)
    
    def left(self):
        if self.circle.heading() != LEFT:
            self.circle.setheading(LEFT)
    
    def right(self):
        if self.circle.heading() != RIGHT:
            self.circle.setheading(RIGHT)

    def is_colliding_with_enemy(self, enemy):
        if self.circle.distance(enemy) < self.size + 15:
            return True
        else:
            return False

    def is_colliding_with_wall(self, screenSize):
        if self.circle.xcor() > 249 or self.circle.xcor() < -249 or self.circle.ycor() > 249 or self.circle.ycor() < -249:
            return True
        else:
            return False