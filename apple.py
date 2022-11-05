import game_details
from turtle import Turtle

class Apple:

    def __init__(self, turtle: Turtle) -> None:
        apple = turtle.Turtle()
        apple.speed(0)
        apple.shape(game_details.SHAPE)
        apple.color(game_details.RED)
        apple.penup()
        apple.goto(0,100)
        self.apple = apple