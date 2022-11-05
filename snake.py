import time
import game_details
from turtle import Turtle


class Snake:

    def __init__(self, turtle: Turtle) -> None:
        self.turtle = turtle
        head = self.turtle.Turtle()
        head.speed(0)
        head.shape(game_details.SHAPE)
        head.color(game_details.BLACK)
        head.penup()
        head.goto(0,0)
        head.direction = 'stop'       
        self.head = head
        self.segments = []

    def go_up(self):
        if self.head.direction != 'down':
            self.head.direction = 'up'

    def go_down(self):
        if self.head.direction != 'up':
            self.head.direction = 'down'

    def go_left(self):
        if self.head.direction != 'right':
            self.head.direction = 'left'

    def go_right(self):
        if self.head.direction != 'left':
            self.head.direction = 'right'

    def move(self):
        # Move the end segments first in reverse order
        for index in range(len(self.segments)-1, 0, -1):
            x = self.segments[index-1].xcor()
            y = self.segments[index-1].ycor()
            self.segments[index].goto(x,y)
        # Move segment 0 to the head
        if len(self.segments) > 0:
            x = self.head.xcor()
            y = self.head.ycor()
            self.segments[0].goto(x,y)
        self.keep_moving_to()

    def keep_moving_to(self) -> None:    
        if self.head.direction == 'up':
            self.head.sety(self.head.ycor() + 10)
        if self.head.direction == 'down':
            self.head.sety(self.head.ycor() - 10)
        if self.head.direction == 'left':
            self.head.setx(self.head.xcor() - 10)
        if self.head.direction == 'right':
            self.head.setx(self.head.xcor() + 10)

    def collision(self):
        time.sleep(0.5)
        self.head.goto(0,0)
        self.head.direction = 'stop'
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()

    def add_segment(self) -> None:
        new_segment = self.turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape(game_details.SHAPE)
        new_segment.color(game_details.GRAY)
        new_segment.penup()
        self.segments.append(new_segment)             