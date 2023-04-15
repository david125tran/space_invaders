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
        '''This pulls up the starting screen'''
        self.clear()
        self.goto(0, 0)
        self.write("Space Invaders Mock Game\n"
                   "\n"
                   "Press 'Space' to fire weapon\n"
                   "Press 'Left' and 'Right' Arrow keys to move ship\n"
                   "Press 's' to start the game!\n"
                   "\n"
                   "Creator: david125tran@gmail.com\n"
                   "David Tran\n",
                   align="Center",
                   font=FONT)

    def update_display(self):
        '''This updates the scoreboard display'''
        self.clear()
        self.goto(0, 260)
        self.write(f"Level: {self.level}       Score:       {self.score}       Lives: {self.lives}",
                   align="Center",
                   font=FONT)

    def lose_life(self):
        '''This removes a life'''
        self.lives = self.lives - 1

    def level_up(self):
        '''This increase a level in the game'''
        self.lives = 3
        self.level = self.level + 1

    def update_score(self, new_score):
        '''This takes in the new score as, "new_scoore" and updates the score'''
        self.score = new_score

    def game_over(self):
        '''This function forces the game to be over'''
        self.clear()
        self.goto(0, 0)
        self.write(f"Level: {self.level}\nScore:{self.score}\n\n"
                   f"GAME OVER!!!\n"
                   f"Press 'r' to return to main menu\n"
                   f"Contact: david125tran@gmail.com",
                   align="Center",
                   font=FONT)

    def restart(self):
        '''This restarts the scoreboard'''
        self.level = 1
        self.lives = 3
        self.score = 0
        self.start_screen()
