# ---------------------------- IMPORTS ---------------------------- #
from turtle import Turtle
import random
from playsound import playsound
# ---------------------------- CONSTANTS ---------------------------- #
ALIENS_LOCATION = [(-210, 240), (-140, 240), (-70, 240), (0, 240), (70, 240), (140, 240), (210, 240),
                   (-210, 210), (-140, 210), (-70, 210), (0, 210), (70, 210), (140, 210), (210, 210)]
INVADER_KILLED_SOUND = 'sounds/invaderkilled.wav'

# ---------------------------- CODE ---------------------------- #
class Aliens(Turtle):
    def __init__(self):
        self.all_aliens = []
        self.score = 0

        # Bullets
        self.all_bullets = []
        self.bullet_speed = 15

    def create_aliens(self):
        '''This function creates all aliens for the start of a new level'''
        for location in ALIENS_LOCATION:
            new_alien = Turtle("turtle")
            new_alien.right(90)
            new_alien.penup()
            new_alien.color("blue")
            new_alien.goto(location)
            self.all_aliens.append(new_alien)

    def create_bullet(self):
        '''This function is used for aliens to fire bullets at random'''
        new_bullet = Turtle("circle")
        new_bullet.shapesize(stretch_wid=0.4, stretch_len=0.4)
        new_bullet.penup()
        new_bullet.color("white")
        random_alien = random.choice(self.all_aliens)
        new_bullet.goto(random_alien.xcor(), random_alien.ycor())
        self.all_bullets.append(new_bullet)

    def move_bullet(self):
        '''This function moves the alien's bullets in a downward trajectory towards the player'''
        for bullet in self.all_bullets:
            bullet_x = bullet.xcor()
            bullet_y = bullet.ycor()
            bullet.goto(bullet_x, bullet_y - self.bullet_speed)

    def get_bullet_position(self):
        '''This function returns the alien's bullet position'''
        for bullet in self.all_bullets:
            return [bullet.xcor, bullet.ycor]

    def remove_alien(self, alien):
        '''Takes in an alien, as "alien", and removes the alien'''
        self.all_aliens.remove(alien)
        alien.goto(-5000, 5000)
        self.score = self.score

    def remove_alien_bullet(self, alien_bullet):
        '''Takes in  an alien's bullet, as "alien_bullet" and removes the alien's bullet'''
        self.all_bullets.remove(alien_bullet)
        alien_bullet.goto(-5000, 10000)

    def remove_all_alien_bullets(self):
        '''This function removes all alien bullets on screen'''
        for alien_bullet in self.all_bullets:
            alien_bullet.goto(-5000, 10000)
            self.all_bullets = []

    def remove_alien_and_bullet(self, alien, bullet):
        '''This function takes in an alien and bullet as, "alien" and "bullet", and removes both of them'''
        self.remove_alien(alien)
        bullet.goto(5000, 5000)
        self.score = self.score + 5
        playsound(INVADER_KILLED_SOUND, block=False)

    def detect_hit(self, bullet):
        '''This function takes in a player's bullet, as "bullet", and detects, if it hit an alien'''
        # Each coordinate must be checked because of the (-) negative and
        # (+) positive coordinates of the bullet and alien
        for alien in self.all_aliens:
            # Quadrant - Left:
            if bullet.xcor() < 0 and alien.xcor() < 0 and bullet.ycor() > 0:
                if abs(abs(bullet.xcor()) - abs(alien.xcor())) < 15 and \
                    abs(abs(bullet.ycor()) - abs(alien.ycor())) < 15:
                        self.remove_alien_and_bullet(alien, bullet)
            # Center - Vertical:
            elif bullet.xcor() == 0 and alien.xcor() == 0 and bullet.ycor() > 0 and \
                    abs(abs(bullet.ycor()) - abs(alien.ycor())) < 15:
                        self.remove_alien_and_bullet(alien, bullet)
            # Quadrant - Right:
            elif bullet.xcor() > 0 and alien.xcor() > 0 and bullet.ycor() > 0:
                if abs(abs(bullet.xcor()) - abs(alien.xcor())) < 15 and \
                        abs(abs(bullet.ycor()) - abs(alien.ycor())) < 15:
                        self.remove_alien_and_bullet(alien, bullet)

    def move_right(self):
        '''This moves all aliens to the right'''
        for alien in self.all_aliens:
            alien.goto(alien.xcor() + 35, alien.ycor())

    def move_left(self):
        '''This moves all aliens to the left'''
        for alien in self.all_aliens:
            alien.goto(alien.xcor() - 35, alien.ycor())

    def restart(self):
        '''This restarts the game for all aliens'''
        self.score = 0
        self.remove_all_alien_bullets()
        for alien in self.all_aliens:
            alien.goto(-5000, 5000)
        self.all_aliens = []

