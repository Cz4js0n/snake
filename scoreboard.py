from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=250)
        self.speed("fastest")

    def score_show(self):
        self.clear()
        self.write(arg=f"Score {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)
