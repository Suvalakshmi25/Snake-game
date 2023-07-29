from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial,24,normal")
class   ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()
    def update_score(self):
        self.write(f"Score:{self.score}", align="center",font=FONT)
    def game_over(self):
        self.home()
        self.write("GAME OVER ", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()
