from turtle import Turtle

class Dot:
    colors = {"red", "blue", "green", "pink", "yellow"}

    def __init__(self):
        super().__init__()
        
        self.shape = Turtle()
        self.shape.shape("circle")
