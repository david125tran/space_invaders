# ---------------------------- IMPORTS ---------------------------- #
import time
from turtle import Screen
from player import Player
from game_manager import GameManager
from playsound import playsound

# ---------------------------- CONSTANTS ---------------------------- #
BACKGROUND_MUSIC = 'sounds/music.mpeg'
EXPLOSION_SOUND = 'sounds/explosion.wav'
# ---------------------------- CODE ---------------------------- #

# Generate the screen
screen = Screen()
screen.title("David Tran's Space Invaders (Built w/Python)")
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.tracer(0)
playsound(BACKGROUND_MUSIC, block=False)

player = Player()
game_manager = GameManager()

screen.listen()

def disable_key_press():
    # This function will make key presses do nothing
    pass

def lose_life(a_bullet):
    game_manager.scoreboard.lose_life()
    game_manager.aliens.remove_alien_bullet(a_bullet)
    game_manager.aliens.remove_all_alien_bullets()
    player.goto(0, -260)
    playsound(EXPLOSION_SOUND, block=False)

def restart_game():
    player.remove_all_bullets()
    game_manager.restart()
    screen.update()
    screen.onkeypress(start_game, "s")

# Create new game
def start_game():
    # Key actions:
    screen.onkeypress(disable_key_press, "s")
    screen.onkeypress(player.go_left, "Left")
    screen.onkeypress(player.go_right, "Right")
    screen.onkeypress(player.create_bullet, "space")

    game_manager.start_level()
    game_is_on = True

    while game_is_on:
        time.sleep(0.1)

        # Detect game over:
        if game_manager.scoreboard.lives < 1:
            game_is_on = False

        # Detect player goes out of bounds, if they do, reset their position:
        if player.xcor() < -255:
            player.goto(-220, -260)
        elif player.xcor() > 255:
            player.goto(220, -260)

        # Detect level up:
        if len(game_manager.aliens.all_aliens) == 0:
            player.remove_all_bullets()
            game_manager.aliens.remove_all_alien_bullets()
        game_manager.detect_level_up()

        # Detect life lost in different coordinates:
        for a_bullet in game_manager.aliens.all_bullets:
            # Left coordinate:
            if a_bullet.xcor() < 0 and player.xcor() < 0 and a_bullet.ycor() > -280 and a_bullet.ycor() < -240:
                if abs(abs(a_bullet.xcor()) - abs(player.xcor())) < 45:
                    lose_life(a_bullet)
                    player.remove_all_bullets()
            # Center:
            elif a_bullet.xcor() == 0 and player.xcor() == 0 and a_bullet.ycor() > -280 and a_bullet.ycor() < -240:
                if abs(abs(a_bullet.xcor()) - abs(player.xcor())) < 45:
                    lose_life(a_bullet)
                    player.remove_all_bullets()
            # Right coordinate:
            elif a_bullet.xcor() > 0 and player.xcor() > 0 and a_bullet.ycor() > -280 and a_bullet.ycor() < -240:
                if abs(abs(a_bullet.xcor()) - abs(player.xcor())) < 45:
                    lose_life(a_bullet)
                    player.remove_all_bullets()

        # Remove player bullets that go off-screen:
        for player_bullet in player.all_bullets:
            if player_bullet.ycor() > 300:
                player.remove_player_bullet(player_bullet)

        game_manager.detect_alien_hit(player.all_bullets)

        if player.all_bullets:
            game_manager.detect_bullets_collide(player.all_bullets)

        game_manager.update_game()
        player.move_bullet()

        # Update the screen
        screen.update()

    game_manager.scoreboard.game_over()
    screen.onkeypress(restart_game, "r")
    screen.onkeypress(disable_key_press, "Left")
    screen.onkeypress(disable_key_press, "Right")
    screen.onkeypress(disable_key_press, "space")

# Press 's' to start the game!
screen.onkeypress(start_game, "s")

# Leave the screen open
screen.exitonclick()