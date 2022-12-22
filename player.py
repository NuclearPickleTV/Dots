from turtle import Turtle

class Player:
    def __init__(self):
        super().__init__()
        self.size = 0.5

        self.circle = Turtle()
        self.circle.shape("circle")
        self.circle.color("red")
        self.circle.shapesize(self.size)

    def increase_size(self, multiplier):
        self.size = 0.5 * multiplier
        self.circle.shapesize(self.size)
        print(self.size)