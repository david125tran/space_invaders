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
        self.color("white")
        self.start_screen()

    def start_screen(self):
        self.clear()
        self.goto(0, 0)
        self.write("Space Invaders Mock Game\n"
                   "\n"
                   "Press 'Space' to fire weapon\n"
                   "Press 'Left' and 'Right' Arrow keys to move ship\n"
                   "Press 's' to start the game!\n"
                   "\n"
                   "Creator: david125tran@gmail.com\n"
                   "David Tran\n"
                   "(919) 631-3778",
                   align="Center",
                   font=FONT)

    def update_display(self):
        self.clear()
        self.goto(0, 260)
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
        self.write(f"Level: {self.level}\nScore:{self.score}\n\nGAME OVER!!!\nPress 'r' to return to main menu",
                   align="Center",
                   font=FONT)

    def restart(self):
        self.level = 1
        self.lives = 3
        self.score = 0
        self.start_screen()