from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)  # Move to top of screen
        self.update_score()

    def update_score(self):
        self.clear()  # Clear previous score
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!", align = ALIGNMENT, font = FONT)

    