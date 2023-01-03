# ---------------------------- IMPORTS ---------------------------- #
from turtle import Turtle

# ---------------------------- CONSTANTS ---------------------------- #
FONT = ("Verdana", 18, "normal")

# ---------------------------- CODE ---------------------------- #

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.lives = 3
        self.score= 0
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.update_display()
        self.color("white")

    def update_display(self):
        self.clear()
        self.write(f"Level: {self.level}       Score:       {self.score}       Lives: {self.lives}",
                   align="Center",
                   font=FONT)

    def lose_life(self):
        self.lives = self.lives - 1

    def level_up(self):
        self.lives = 3
        self.level = self.level + 1

    def update_score(self, new_score):
        self.score = new_score

    def lose_life(self):
        self.lives = self.lives - 1

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Level: {self.level}\nScore:{self.score}\n\nGAME OVER!!!",
                   align="Center",
                   font=FONT)