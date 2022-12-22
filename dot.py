from turtle import Turtle
import random
colors = ["black", "blue", "green", "pink", "yellow"]

class Dot:
    """The Enemy of the game"""

    def __init__(self):
        super().__init__()
        
        self.shape = Turtle()
        self.shape.penup()
        self.shape.shape("circle")
        self.shape.shapesize(0.5)
        self.shape.speed("fastest")
        #self.shape.goto(50, 20)
        self.move()

    def move(self):
        """Moves the Enemy to a random location and changes the color"""

        for color in colors:
            random_color = random.choice(colors)

        new_position = (random.randrange(-251, 251), random.randrange(-251, 251))
        self.shape.color(random_color)
        self.shape.goto(new_position)
        self.shape.color(random_color)

    def get_position(self):
        return self.shape.position()
