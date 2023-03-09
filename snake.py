from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_list = []
        for i in range(3):
            self.new_snake = Turtle()
            self.new_snake.color("white")
            self.new_snake.shape("square")
            self.new_snake.penup()
            self.new_snake.goto(POSITIONS[i])
            self.snake_list.append(self.new_snake)

    def snake_increment(self):

        self.new_snake = Turtle()
        self.new_snake.goto(self.snake_list[-1].xcor(),self.snake_list[-1].ycor())
        self.new_snake.speed("fastest")
        self.new_snake.color("white")
        self.new_snake.shape("square")
        self.new_snake.penup()

        self.snake_list.append(self.new_snake)


    def move_snake(self):
        for snakes_seg in range(len(self.snake_list) -1, 0, -1):
            new_x = self.snake_list[snakes_seg - 1].xcor()
            new_y = self.snake_list[snakes_seg - 1].ycor()
            self.snake_list[snakes_seg].goto(new_x, new_y)
        self.snake_list[0].forward(20)



    def move_up(self):
        if self.snake_list[0].heading() != DOWN:
            self.snake_list[0].setheading(UP)

    def move_down(self):
        if self.snake_list[0].heading() != UP:
            self.snake_list[0].setheading(DOWN)

    def move_forward(self):
        if self.snake_list[0].heading() != LEFT:
            self.snake_list[0].setheading(RIGHT)

    def move_backward(self):
        if self.snake_list[0].heading() != RIGHT:
            self.snake_list[0].setheading(LEFT)
