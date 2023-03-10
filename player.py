# ---------------------------- IMPORTS ---------------------------- #
from turtle import Turtle
from playsound import playsound

# ---------------------------- CONSTANTS ---------------------------- #
STARTING_POSITION = (0, -260)
MOVE_DISTANCE = 10
SHOOTING_SOUND = 'sounds/shoot.wav'

# ---------------------------- CODE ---------------------------- #

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("red")
        self.right(-90)
        self.width(width=20)
        self.shapesize(stretch_wid=5, stretch_len=2)
        self.goto(STARTING_POSITION)

        # Bullets
        self.all_bullets = []
        self.bullet_speed = 15

    def go_left(self):
        '''This moves the player left'''
        self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())

    def go_right(self):
        '''This moves the player right'''
        self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())

    def get_player_position(self):
        '''This returns the player's x and y coordinate position as [x coordinate, y coordinate]'''
        return [self.xcor(), self.ycor()]

    def create_bullet(self):
        '''This creates a player bullet'''
        new_bullet = Turtle("circle")
        new_bullet.shapesize(stretch_wid=0.3, stretch_len=0.3)
        new_bullet.color("red")
        new_bullet.penup()
        new_bullet.goto(self.xcor(), self.ycor())
        self.all_bullets.append(new_bullet)
        playsound(SHOOTING_SOUND, block=False)

    def move_bullet(self):
        '''This moves all player bullets in an upward trajectory'''
        for bullet in self.all_bullets:
            bullet_x = bullet.xcor()
            bullet_y = bullet.ycor()
            bullet.goto(bullet_x, bullet_y + self.bullet_speed)

    def remove_player_bullet(self, player_bullet):
        '''This takes a player's bullet as, "player_bullet" and removes it'''
        self.all_bullets.remove(player_bullet)

    def remove_all_bullets(self):
        '''This takes all player's bullet as, "player_bullets" and removes all of them'''
        for bullet in self.all_bullets:
            bullet.goto(-10000, 10000)
        self.all_bullets = []



