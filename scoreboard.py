from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.hideturtle()
        self.score = 0
        self.penup()
        self.goto(0, 250)
        self.write(f"Score : {self.score}", font=FONT, align="center")

    def score_increase(self):
        self.clear()
        self.score += 1
        self.write(f"Score : {self.score}", font=FONT, align="center")

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",font=FONT,align="center")