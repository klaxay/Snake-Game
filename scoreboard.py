from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(0, 280)
        self.color("white")
        self.update()

    def update(self):
        self.write(f"Score : {self.score}", align="center", font=("Arial", 10, "normal"))
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()
    def game_over(self):
        self.clear()
        self.write(f"Game Over! Final Score : {self.score}",align="center", font=("Arial", 10, "normal"))
