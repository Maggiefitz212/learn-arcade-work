import arcade
import random

# Create and set the constants for screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.1
SPRITE_SCALING_DOG = 0.007
SPRITE_SCALING_HIDING_SPOT = .325

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ Main game class """

    def __init__(self, width, height, title):
        """ Initializer """
        super().__init__(width, height, title)
        # Sprite lists
        self.dog_list = None
        self.player_list = None
        self.hiding_spot_list = None

        # Set up the player info.
        self.dog_sprite = None
        self.player_sprite = None
        self.hiding_spot = None
        self.lives = None
        self.score = 0
        self.hiding_spot_clicked = None
        self.dog_placement = None

        # Since the user hasn't clicked a hiding spot, button_clicked = False
        self.button_clicked = False

        # Load good and bad sounds when the game starts.
        self.good_sound = arcade.load_sound("Picked Coin Echo 2.wav")
        self.bad_sound = arcade.load_sound("ALERT_Error.wav")

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Set the background color
        arcade.set_background_color(arcade.color.BOTTLE_GREEN)

    def setup(self):
        """ Set up the game and initialize variables """

        # Sprite lists
        self.dog_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.hiding_spot_list = arcade.SpriteList()

        # Set up the score.
        self.score = 0
        self.lives = 3

        # Set up the player, dog, and hiding spot.
        # Dog sprite from kenney.nl
        self.dog_sprite = arcade.Sprite("Daco_3805650.png", SPRITE_SCALING_DOG)

        # Player sprite from opengameart.org
        self.player_sprite = arcade.Sprite("Idle (1).png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 200
        self.player_list.append(self.player_sprite)

        # Create the five different hiding spots
        # All hiding spots from flaticon.com created by Freepik
        self.hiding_spot = arcade.Sprite("playground.png", SPRITE_SCALING_HIDING_SPOT)
        self.hiding_spot.center_x = 150
        self.hiding_spot.center_y = 250
        self.hiding_spot_list.append(self.hiding_spot)
        self.hiding_spot = arcade.Sprite("fountain.png", SPRITE_SCALING_HIDING_SPOT)
        self.hiding_spot.center_x = 300
        self.hiding_spot.center_y = 350
        self.hiding_spot_list.append(self.hiding_spot)
        self.hiding_spot = arcade.Sprite("slide.png", SPRITE_SCALING_HIDING_SPOT)
        self.hiding_spot.center_x = 450
        self.hiding_spot.center_y = 450
        self.hiding_spot_list.append(self.hiding_spot)
        self.hiding_spot = arcade.Sprite("seesaw.png", SPRITE_SCALING_HIDING_SPOT)
        self.hiding_spot.center_x = 600
        self.hiding_spot.center_y = 350
        self.hiding_spot_list.append(self.hiding_spot)
        self.hiding_spot = arcade.Sprite("bridge.png", SPRITE_SCALING_HIDING_SPOT)
        self.hiding_spot.center_x = 700
        self.hiding_spot.center_y = 250
        self.hiding_spot_list.append(self.hiding_spot)

        # Roll a random number that will decide where to place the dog
        dog_placement_number = random.randrange(5)
        if dog_placement_number == 0:
            self.dog_sprite.center_x = 150
            self.dog_sprite.center_y = 250
            self.dog_list.append(self.dog_sprite)
            self.dog_placement = "Playground"
        elif dog_placement_number == 1:
            self.dog_sprite.center_x = 300
            self.dog_sprite.center_y = 350
            self.dog_list.append(self.dog_sprite)
            self.dog_placement = "Fountain"
        elif dog_placement_number == 2:
            self.dog_sprite.center_x = 450
            self.dog_sprite.center_y = 450
            self.dog_list.append(self.dog_sprite)
            self.dog_placement = "Slide"
        elif dog_placement_number == 3:
            self.dog_sprite.center_x = 600
            self.dog_sprite.center_y = 350
            self.dog_list.append(self.dog_sprite)
            self.dog_placement = "Seesaw"
        else:
            self.dog_sprite.center_x = 700
            self.dog_sprite.center_y = 250
            self.dog_list.append(self.dog_sprite)
            self.dog_placement = "Bridge"

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()

        # Draw the sprites
        self.dog_list.draw()
        self.player_list.draw()
        self.hiding_spot_list.draw()

        # Show the lives on the screen
        lives_output = f"Lives Left: {self.lives}"
        score_output = f"Score: {self.score}"
        arcade.draw_text(lives_output, 10, 60, arcade.color.WHITE, 28)
        arcade.draw_text(score_output, 10, 20, arcade.color.WHITE, 28)

        if self.lives == 0:
            game_over_output = f"You lose! Your score was {self.score}"
            arcade.draw_text(game_over_output, 100, 300, arcade.color.BLACK, 36)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle mouse motion """
        if self.lives > 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """
        if button == arcade.MOUSE_BUTTON_LEFT:
            print("Left mouse button pressed at", x, y)
            if self.hiding_spot_list[0].left <= x <= self.hiding_spot_list[0].right:
                if self.hiding_spot_list[0].bottom <= y <= self.hiding_spot_list[0].top:
                    self.hiding_spot_clicked = "Playground"
            elif self.hiding_spot_list[1].left <= x <= self.hiding_spot_list[1].right:
                if self.hiding_spot_list[1].bottom <= y <= self.hiding_spot_list[1].top:
                    self.hiding_spot_clicked = "Fountain"
            elif self.hiding_spot_list[2].left <= x <= self.hiding_spot_list[2].right:
                if self.hiding_spot_list[2].bottom <= y <= self.hiding_spot_list[2].top:
                    self.hiding_spot_clicked = "Slide"
            elif self.hiding_spot_list[3].left <= x <= self.hiding_spot_list[3].right:
                if self.hiding_spot_list[3].bottom <= y <= self.hiding_spot_list[3].top:
                    self.hiding_spot_clicked = "Seesaw"
            else:
                if self.hiding_spot_list[3].bottom <= y <= self.hiding_spot_list[3].top:
                    self.hiding_spot_clicked = "Bridge"

            print(self.hiding_spot_clicked)

            if self.hiding_spot_clicked == self.dog_placement:
                self.score += 10
            else:
                self.lives -= 1

        elif button == arcade.MOUSE_BUTTON_RIGHT:
            print("Right mouse button pressed at", x, y)


def main():
    """ Open window and call other functions """
    # Open a 600 x 600 window called Lab 12 - Fitzpatrick.
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, " Lab 12 - Fitzpatrick ")
    window.setup()
    arcade.run()


# Check if import name is equal to main.
# If it is, run main.
if __name__ == "__main__":
    main()
