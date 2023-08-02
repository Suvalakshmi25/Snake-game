from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial,24,normal")
class   ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("score.txt") as sc:
            self.highscore= int(sc.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.highscore}", align="center",font=FONT)

    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("score.txt", mode="w") as sc:
                sc.write(f"{self.highscore}")
        self.score=0
        self.update_score()
    # def game_over(self):
    #     self.home()
    #     self.write("GAME OVER ", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score+=1
        self.update_score()
