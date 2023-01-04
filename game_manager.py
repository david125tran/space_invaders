# ---------------------------- IMPORTS ---------------------------- #
from turtle import Turtle
import random
from aliens import Aliens
from scoreboard import Scoreboard
from playsound import playsound

# ---------------------------- CONSTANTS ---------------------------- #
COLLISION = 15
EXPLOSION_SOUND = 'sounds/explosion.wav'

# ---------------------------- CODE ---------------------------- #
class GameManager(Turtle):
    def __init__(self):
        self.aliens = Aliens()
        self.scoreboard = Scoreboard()

    def start_level(self):
        '''Starts a new level'''
        self.aliens.create_aliens()
        self.scoreboard.update_display()


    def alien_fire_weapon(self):
        '''Makes the aliens fire weapons at random.  As the level increases, the firing speeds up'''
        self.top_range = 200 + (10 * self.scoreboard.level)
        self.random_number = random.randrange(0, self.top_range)
        if self.random_number > 190:   # 20% Chance of firing weapon
            self.aliens.create_bullet()
        else:
            pass
        self.aliens.move_bullet()

    def remove_alien_and_player_bullets(self, a_bullet, p_bullet):
        '''This takes in an alien and player bullet as, "a_bullet" and "p_bullet" and removes both bullets'''
        self.aliens.remove_alien_bullet(a_bullet)
        p_bullet.goto(10000, -10000)
        self.aliens.score = self.aliens.score + 1
        playsound(EXPLOSION_SOUND, block=False)

    def detect_bullets_collide(self, player_bullets):
        '''This takes in all player's bullets as, "player_bullets" to check if it hit an alien's bullet'''
        # Detect alien and player bullet colliding in each quadrant
        for a_bullet in self.aliens.all_bullets:
            for p_bullet in player_bullets:

                # Quadrant - Bottom Left:
                if a_bullet.xcor() < 0 and a_bullet.ycor() < 0 and p_bullet.xcor() < 0 and p_bullet.ycor() < 0:
                    if abs(abs(a_bullet.xcor()) - abs(p_bullet.xcor())) < COLLISION and \
                        abs(abs(a_bullet.ycor()) - abs(p_bullet.ycor())) < 30:
                        self.remove_alien_and_player_bullets(a_bullet, p_bullet)
                # Quadrant - Bottom Right:
                elif a_bullet.xcor() > 0 and a_bullet.ycor() < 0 and p_bullet.xcor() > 0 and p_bullet.ycor() < 0:
                    if abs(abs(a_bullet.xcor()) - abs(p_bullet.xcor())) < COLLISION and \
                        abs(abs(a_bullet.ycor()) - abs(p_bullet.ycor())) < 30:
                        self.remove_alien_and_player_bullets(a_bullet, p_bullet)
                # Quadrant - Top Right:
                elif a_bullet.xcor() > 0 and a_bullet.ycor() > 0 and p_bullet.xcor() > 0 and p_bullet.ycor() > 0:
                    if abs(abs(a_bullet.xcor()) - abs(p_bullet.xcor())) < COLLISION and \
                        abs(abs(a_bullet.ycor()) - abs(p_bullet.ycor())) < 30:
                        self.remove_alien_and_player_bullets(a_bullet, p_bullet)
                # Quadrant - Top Left:
                elif a_bullet.xcor() < 0 and a_bullet.ycor() > 0 and p_bullet.xcor() < 0 and p_bullet.ycor() > 0:
                    if abs(abs(a_bullet.xcor()) - abs(p_bullet.xcor())) < COLLISION and \
                        abs(abs(a_bullet.ycor()) - abs(p_bullet.ycor())) < 30:
                        self.remove_alien_and_player_bullets(a_bullet, p_bullet)
                # Center - Vertical Top:
                elif a_bullet.xcor() == 0 and a_bullet.ycor() > 0 and p_bullet.xcor() == 0 and p_bullet.ycor() > 0:
                    if abs(abs(a_bullet.xcor()) - abs(p_bullet.xcor())) < COLLISION and \
                        abs(abs(a_bullet.ycor()) - abs(p_bullet.ycor())) < 30:
                        self.remove_alien_and_player_bullets(a_bullet, p_bullet)
                # Center - Vertical Bottom:
                elif a_bullet.xcor() == 0 and a_bullet.ycor() < 0 and p_bullet.xcor() == 0 and p_bullet.ycor() < 0:
                    if abs(abs(a_bullet.xcor()) - abs(p_bullet.xcor())) < COLLISION and \
                        abs(abs(a_bullet.ycor()) - abs(p_bullet.ycor())) < 30:
                        self.remove_alien_and_player_bullets(a_bullet, p_bullet)
                # Center:
                elif a_bullet.xcor() == 0 and a_bullet.ycor() == 0 and p_bullet.xcor() == 0 and p_bullet.ycor() == 0:
                    if abs(abs(a_bullet.xcor()) - abs(p_bullet.xcor())) < COLLISION and \
                        abs(abs(a_bullet.ycor()) - abs(p_bullet.ycor())) < 30:
                        self.remove_alien_and_player_bullets(a_bullet, p_bullet)
                # Center - Horizontal Left:
                elif a_bullet.xcor() < 0 and a_bullet.ycor() == 0 and p_bullet.xcor() < 0 and p_bullet.ycor() == 0:
                    if abs(abs(a_bullet.xcor()) - abs(p_bullet.xcor())) < COLLISION and \
                        abs(abs(a_bullet.ycor()) - abs(p_bullet.ycor())) < 30:
                        self.remove_alien_and_player_bullets(a_bullet, p_bullet)
                # Center - Horizontal Left:
                elif a_bullet.xcor() > 0 and a_bullet.ycor() == 0 and p_bullet.xcor() > 0 and p_bullet.ycor() == 0:
                    if abs(abs(a_bullet.xcor()) - abs(p_bullet.xcor())) < COLLISION and \
                        abs(abs(a_bullet.ycor()) - abs(p_bullet.ycor())) < 30:
                        self.remove_alien_and_player_bullets(a_bullet, p_bullet)


    def detect_alien_hit(self, bullets):
        '''This takes in all player's bullets as, "bullets", and checks if an alien was hit'''
        for bullet in bullets:
            self.aliens.detect_hit(bullet)

    def update_score(self):
        '''This function updates the scoreboard'''
        score =  self.aliens.score
        self.scoreboard.update_score(score)

    def level_up(self):
        '''This function level's up the game'''
        self.scoreboard.level_up()
        self.start_level()

    def move_aliens(self):
        '''This function moves aliens at random either left or right'''
        # Aliens moving left and right at random speed
        move_aliens = random.randrange(0, 101 + (self.scoreboard.level * 4))
        if move_aliens > 90:
            choice = random.randrange(1, 3)
            if choice == 1:
                self.aliens.move_right()
            else:
                self.aliens.move_left()
            for alien in self.aliens.all_aliens:
                if alien.xcor() < 0 and alien.xcor() < -256:
                    self.aliens.move_right()
                elif alien.xcor() > 0 and alien.xcor() > 256:
                    self.aliens.move_left()

    def update_game(self):
        '''This function is called every loop to update the game'''
        if self.aliens.all_aliens:
            self.alien_fire_weapon()
            self.scoreboard.update_display()
            self.move_aliens()
            self.update_score()

        # Remove alien bullets that go off-screen
        for alien_bullet in self.aliens.all_bullets:
            if alien_bullet.ycor() < -300:
                self.aliens.remove_alien_bullet(alien_bullet)

    def restart (self):
        '''This function restarts the game'''
        self.aliens.restart()
        self.scoreboard.restart()



