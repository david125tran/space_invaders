# ---------------------------- IMPORTS ---------------------------- #
from turtle import Turtle
import random
from aliens import Aliens
from scoreboard import Scoreboard
from playsound import playsound
# ---------------------------- CONSTANTS ---------------------------- #
COLLISION = 15
# ---------------------------- CODE ---------------------------- #
class GameManager(Turtle):
    def __init__(self):
        self.aliens = Aliens()
        self.scoreboard = Scoreboard()

    def start_level(self):
        self.aliens.create_aliens()

    def alien_fire_weapon(self):
        self.top_range = 200 + (10 * self.scoreboard.level)
        self.random_number = random.randrange(0, self.top_range)
        if self.random_number > 190:   # 20% Chance of firing weapon
            self.aliens.create_bullet()
        else:
            pass
        self.aliens.move_bullet()

    def detect_bullets_collide(self, player_bullets):
        for a_bullet in self.aliens.all_bullets:
            for p_bullet in player_bullets:

                # Quadrant - Bottom Left:
                if a_bullet.xcor() < 0 and a_bullet.ycor() < 0 and p_bullet.xcor() < 0 and p_bullet.ycor() < 0:
                    if abs(abs(a_bullet.xcor()) - abs(p_bullet.xcor())) < COLLISION:
                        if abs(abs(a_bullet.ycor()) - abs(p_bullet.ycor())) < 30:
                            self.aliens.remove_alien_bullet(a_bullet)
                            p_bullet.goto(10000, -10000)
                            playsound('sounds/explosion.wav', block=False)
                # Quadrant - Bottom Right:
                elif a_bullet.xcor() > 0 and a_bullet.ycor() < 0 and p_bullet.xcor() > 0 and p_bullet.ycor() < 0:
                    if abs(abs(a_bullet.xcor()) - abs(p_bullet.xcor())) < COLLISION:
                        if abs(abs(a_bullet.ycor()) - abs(p_bullet.ycor())) < 30:
                            self.aliens.remove_alien_bullet(a_bullet)
                            p_bullet.goto(10000, -10000)
                            playsound('sounds/explosion.wav', block=False)
                # Quadrant - Top Right:
                elif a_bullet.xcor() > 0 and a_bullet.ycor() > 0 and p_bullet.xcor() > 0 and p_bullet.ycor() > 0:
                    if abs(abs(a_bullet.xcor()) - abs(p_bullet.xcor())) < COLLISION:
                        if abs(abs(a_bullet.ycor()) - abs(p_bullet.ycor())) < 30:
                            self.aliens.remove_alien_bullet(a_bullet)
                            p_bullet.goto(10000, -10000)
                            playsound('sounds/explosion.wav', block=False)
                # Quadrant - Top Left:
                elif a_bullet.xcor() < 0 and a_bullet.ycor() > 0 and p_bullet.xcor() < 0 and p_bullet.ycor() > 0:
                    if abs(abs(a_bullet.xcor()) - abs(p_bullet.xcor())) < COLLISION:
                        if abs(abs(a_bullet.ycor()) - abs(p_bullet.ycor())) < 30:
                            self.aliens.remove_alien_bullet(a_bullet)
                            p_bullet.goto(10000, -10000)
                            playsound('sounds/explosion.wav', block=False)
                # Center - Vertical Top:
                elif a_bullet.xcor() == 0 and a_bullet.ycor() > 0 and p_bullet.xcor() == 0 and p_bullet.ycor() > 0:
                    if abs(abs(a_bullet.xcor()) - abs(p_bullet.xcor())) < COLLISION:
                        if abs(abs(a_bullet.ycor()) - abs(p_bullet.ycor())) < 30:
                            self.aliens.remove_alien_bullet(a_bullet)
                            p_bullet.goto(10000, -10000)
                            playsound('sounds/explosion.wav', block=False)
                # Center - Vertical Bottom:
                elif a_bullet.xcor() == 0 and a_bullet.ycor() < 0 and p_bullet.xcor() == 0 and p_bullet.ycor() < 0:
                    if abs(abs(a_bullet.xcor()) - abs(p_bullet.xcor())) < COLLISION:
                        if abs(abs(a_bullet.ycor()) - abs(p_bullet.ycor())) < 30:
                            self.aliens.remove_alien_bullet(a_bullet)
                            p_bullet.goto(10000, -10000)
                            playsound('sounds/explosion.wav', block=False)
                # Center:
                elif a_bullet.xcor() == 0 and a_bullet.ycor() == 0 and p_bullet.xcor() == 0 and p_bullet.ycor() == 0:
                    if abs(abs(a_bullet.xcor()) - abs(p_bullet.xcor())) < COLLISION:
                        if abs(abs(a_bullet.ycor()) - abs(p_bullet.ycor())) < 30:
                            self.aliens.remove_alien_bullet(a_bullet)
                            p_bullet.goto(10000, -10000)
                            playsound('sounds/explosion.wav', block=False)
                # Center - Horizontal Left:
                elif a_bullet.xcor() < 0 and a_bullet.ycor() == 0 and p_bullet.xcor() < 0 and p_bullet.ycor() == 0:
                    if abs(abs(a_bullet.xcor()) - abs(p_bullet.xcor())) < COLLISION:
                        if abs(abs(a_bullet.ycor()) - abs(p_bullet.ycor())) < 30:
                            self.aliens.remove_alien_bullet(a_bullet)
                            p_bullet.goto(10000, -10000)
                            playsound('sounds/explosion.wav', block=False)
                # Center - Horizontal Left:
                elif a_bullet.xcor() > 0 and a_bullet.ycor() == 0 and p_bullet.xcor() > 0 and p_bullet.ycor() == 0:
                    if abs(abs(a_bullet.xcor()) - abs(p_bullet.xcor())) < COLLISION:
                        if abs(abs(a_bullet.ycor()) - abs(p_bullet.ycor())) < 30:
                            self.aliens.remove_alien_bullet(a_bullet)
                            p_bullet.goto(10000, -10000)
                            playsound('sounds/explosion.wav', block=False)


    def detect_alien_hit(self, bullets):
        for bullet in bullets:
            self.aliens.detect_hit(bullet)

    def update_score(self):
        score = self.aliens.number_of_aliens_hit()
        self.scoreboard.update_score(score)

    def detect_level_up(self):
        if len(self.aliens.all_aliens) == 0:
            self.scoreboard.level_up()
            self.start_level()

    def move_aliens(self):
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
        if self.aliens.all_aliens:
            self.alien_fire_weapon()
            self.scoreboard.update_display()
            self.move_aliens()
            self.update_score()

        # Remove alien bullets that go off-screen
        for alien_bullet in self.aliens.all_bullets:
            if alien_bullet.ycor() < -300:
                self.aliens.remove_alien_bullet(alien_bullet)


