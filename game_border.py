import game_details
from turtle import Turtle


class GameBorder:

    def __init__(self, turtle: Turtle) -> None:
        border = turtle.Turtle()
        border.speed(0)
        border.shape(game_details.SHAPE)
        border.color(game_details.BLACK)
        border.penup()
        border.hideturtle()
        border.goto(game_details.BOUNDARIES+20,game_details.BOUNDARIES+20)
        border.pendown()
        border.goto(-(game_details.BOUNDARIES+20),game_details.BOUNDARIES+20)
        border.goto(-(game_details.BOUNDARIES+20),-(game_details.BOUNDARIES+20))
        border.goto(game_details.BOUNDARIES+20,-(game_details.BOUNDARIES+20))
        border.goto(game_details.BOUNDARIES+20,game_details.BOUNDARIES+20)
        border.penup()
        self.border = border