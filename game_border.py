import game_details
from turtle import Turtle


class GameBorder:

    def __init__(self, turtle: Turtle) -> None:
        border = turtle.Turtle()
        border.speed(0)
        border.shape(game_details.SHAPE)
        border.color(game_details.BLACK)
        self.border = border

    def draw(self) -> None:
        self.border.penup()
        self.border.hideturtle()
        self.border.goto(game_details.BOUNDARIES+20,game_details.BOUNDARIES+20)
        self.border.pendown()
        self.border.goto(-(game_details.BOUNDARIES+20),game_details.BOUNDARIES+20)
        self.border.goto(-(game_details.BOUNDARIES+20),-(game_details.BOUNDARIES+20))
        self.border.goto(game_details.BOUNDARIES+20,-(game_details.BOUNDARIES+20))
        self.border.goto(game_details.BOUNDARIES+20,game_details.BOUNDARIES+20)
        self.border.penup()
