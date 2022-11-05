import time
import turtle
import game_details
from random import randint
from apple import Apple
from game_border import GameBorder
from snake import Snake


class Game:

    def __init__(self) -> None:
        wn = turtle.Screen()
        wn.title('Snake Game')
        wn.bgcolor(game_details.WHITE)
        wn.setup(width=game_details.WIDTH, height=game_details.HEIGHT)
        wn.tracer(0)
        self.wn = wn
        self.snake = Snake(turtle)
        self.apple = Apple(turtle).apple
        self.border = GameBorder(turtle).draw()

    def mainloop(self) -> turtle._Screen:
        self.wn.mainloop()    
    
    def key_listener(self) -> None:
        self.wn.listen()
        self.wn.onkeypress(self.snake.go_up, 'Up')
        self.wn.onkeypress(self.snake.go_down, 'Down')
        self.wn.onkeypress(self.snake.go_left, 'Left')
        self.wn.onkeypress(self.snake.go_right, 'Right')

    def game_loop(self) -> None:
        while True:
            self.wn.update()
            self.check_collision()
            if self.snake.head.distance(self.apple) < 20:
                self.apple.goto(randint(-game_details.BOUNDARIES,game_details.BOUNDARIES),randint(-game_details.BOUNDARIES,game_details.BOUNDARIES))
                self.snake.add_segment()
                game_details.DELAY -= 0.001
            self.snake.move()
            for segment in self.snake.segments:
                if segment.distance(self.snake.head) < 10:
                    self.snake.collision()
            time.sleep(game_details.DELAY)

    def check_collision(self) -> None:
        if self.snake.head.xcor()>game_details.BOUNDARIES or self.snake.head.xcor()<-game_details.BOUNDARIES or self.snake.head.ycor()>game_details.BOUNDARIES or self.snake.head.ycor()<-game_details.BOUNDARIES:
            self.snake.collision()