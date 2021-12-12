import arcade
import random

# Create and set the constants for screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.1
SPRITE_SCALING_DOG_1 = 0.007
SPRITE_SCALING_DOG_2 = .115
SPRITE_SCALING_HIDING_SPOT = .325

MOVEMENT_SPEED = 5


# Function allows player to choose between a brown and gray dog to find
def choose_player(x, y):
    dog_sprite_1 = arcade.Sprite("Daco_3805650.png", SPRITE_SCALING_DOG_1)
    dog_sprite_1.center_x = 100
    dog_sprite_1.center_y = 190
    dog_sprite_2 = arcade.Sprite("Idle (2).png", SPRITE_SCALING_DOG_2)
    dog_sprite_2.center_x = 690
    dog_sprite_2.center_y = 190
    if dog_sprite_1.left <= x <= dog_sprite_1.right:
        if dog_sprite_1.bottom <= y <= dog_sprite_1.top:
            dog_choice = "Brown Dog"
            return dog_choice
    elif dog_sprite_2.left <= x <= dog_sprite_2.right:
        if dog_sprite_2.bottom <= y <= dog_sprite_2.top:
            dog_choice = "Grey Dog"
            return dog_choice
    else:
        arcade.draw_text("That is not a possible character. CLick on a dog.", 200, 150,
                         arcade.color.RED, font_size=20, anchor_x="center")


# Function hides dog in random spot
def hide_dog(dog_sprite, hiding_spot_list):
    dog_sprite.center_x = random.randrange(10, 795)
    dog_sprite.center_y = random.randrange(10, 595)
    dog_sprite.angle = random.randrange(360)
    for hiding_spot in hiding_spot_list:
        if not arcade.check_for_collision(dog_sprite, hiding_spot):
            dog_placement_number = random.randrange(8)
            if dog_placement_number == 0:
                dog_sprite.center_x = 110
                dog_sprite.center_y = 270
            elif dog_placement_number == 1:
                dog_sprite.center_x = 300
                dog_sprite.center_y = 200
            elif dog_placement_number == 2:
                dog_sprite.center_x = 430
                dog_sprite.center_y = 450
            elif dog_placement_number == 3:
                dog_sprite.center_x = 575
                dog_sprite.center_y = 310
            elif dog_placement_number == 4:
                dog_sprite.center_x = 700
                dog_sprite.center_y = 160
            elif dog_placement_number == 5:
                dog_sprite.center_x = 480
                dog_sprite.center_y = 125
            elif dog_placement_number == 6:
                dog_sprite.center_x = 200
                dog_sprite.center_y = 480
            elif dog_placement_number == 7:
                dog_sprite.center_x = 630
                dog_sprite.center_y = 470


# Class that shows instruction screen and displays options for dogs
class InstructionView(arcade.View):
    def on_show(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.color.BOTTLE_GREEN)

        self.window.set_mouse_visible(True)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        arcade.draw_text("Instructions Screen", self.window.width / 2, self.window.height / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Click on dog you want to advance", self.window.width / 2, self.window.height / 2-125,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text("Game Instructions: Find dog and click on it.", self.window.width / 2,
                         self.window.height / 2-75, arcade.color.WHITE, font_size=30, anchor_x="center")
        dog_sprite_1 = arcade.Sprite("Daco_3805650.png", SPRITE_SCALING_DOG_1)
        dog_sprite_1.center_x = 100
        dog_sprite_1.center_y = 190
        dog_sprite_1.draw()
        dog_sprite_2 = arcade.Sprite("Idle (2).png", SPRITE_SCALING_DOG_2)
        dog_sprite_2.center_x = 690
        dog_sprite_2.center_y = 190
        dog_sprite_2.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handles mouse motion """
        # Player sprite from opengameart.org
        player_sprite = arcade.Sprite("Idle (1).png", SPRITE_SCALING_PLAYER)
        player_sprite.center_x = 50
        player_sprite.center_y = 250
        player_sprite.center_x = x
        player_sprite.center_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        """ If the user presses the mouse button on a dog, start the game and choose player. """
        dog_choice = choose_player(x, y)
        if dog_choice:
            game_view = GameView()
            game_view.setup(dog_choice)
            self.window.show_view(game_view)


class GameView(arcade.View):
    """ Main game class """

    def __init__(self):
        """ Initializer """
        super().__init__()
        # Sprite lists
        self.dog_list = None
        self.player_list = None
        self.hiding_spot_list = None

        # Set up the player info.
        self.dog_sprite = None
        self.user_player = None
        self.player_sprite = None
        self.hiding_spot = None
        self.lives = None
        self.score = 0
        self.dog_placement = None

        # Load good and bad sounds when the game starts.
        self.good_sound = arcade.load_sound("Picked Coin Echo 2.wav")
        self.bad_sound = arcade.load_sound("ALERT_Error.wav")

        # Don't show the mouse cursor
        self.window.set_mouse_visible(False)

        # Set the background color
        arcade.set_background_color(arcade.color.BOTTLE_GREEN)

    def setup(self, dog_choice):
        """ Set up the game and initialize variables """

        # Sprite lists
        self.dog_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.hiding_spot_list = arcade.SpriteList()

        # Set up the score.
        self.score = 0
        self.lives = 3

        # Set up the player, dog, and hiding spots.
        # Brown dog sprite from kenney.nl
        # Grey dog sprite from opengameart.org
        if dog_choice == "Brown Dog":
            self.dog_sprite = arcade.Sprite("Daco_3805650.png", SPRITE_SCALING_DOG_1)
            self.dog_sprite.center_x = 100
            self.dog_sprite.center_y = 190
            self.dog_list.append(self.dog_sprite)
        elif dog_choice == "Grey Dog":
            self.dog_sprite = arcade.Sprite("Idle (2).png", SPRITE_SCALING_DOG_2)
            self.dog_sprite.center_x = 690
            self.dog_sprite.center_y = 190
            self.dog_list.append(self.dog_sprite)

        # Player sprite from opengameart.org
        self.player_sprite = arcade.Sprite("Idle (1).png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 250
        self.player_list.append(self.player_sprite)

        # All hiding spots from flaticon.com created by Freepik
        self.hiding_spot = arcade.Sprite("playground.png", SPRITE_SCALING_HIDING_SPOT)
        self.hiding_spot.center_x = 125
        self.hiding_spot.center_y = 300
        self.hiding_spot_list.append(self.hiding_spot)
        self.hiding_spot = arcade.Sprite("fountain.png", SPRITE_SCALING_HIDING_SPOT)
        self.hiding_spot.center_x = 325
        self.hiding_spot.center_y = 230
        self.hiding_spot_list.append(self.hiding_spot)
        self.hiding_spot = arcade.Sprite("slide.png", SPRITE_SCALING_HIDING_SPOT)
        self.hiding_spot.center_x = 430
        self.hiding_spot.center_y = 450
        self.hiding_spot_list.append(self.hiding_spot)
        self.hiding_spot = arcade.Sprite("seesaw.png", SPRITE_SCALING_HIDING_SPOT)
        self.hiding_spot.center_x = 565
        self.hiding_spot.center_y = 300
        self.hiding_spot_list.append(self.hiding_spot)
        self.hiding_spot = arcade.Sprite("bridge.png", SPRITE_SCALING_HIDING_SPOT)
        self.hiding_spot.center_x = 700
        self.hiding_spot.center_y = 150
        self.hiding_spot_list.append(self.hiding_spot)
        self.hiding_spot = arcade.Sprite("carousel.png", SPRITE_SCALING_HIDING_SPOT)
        self.hiding_spot.center_x = 500
        self.hiding_spot.center_y = 125
        self.hiding_spot_list.append(self.hiding_spot)
        self.hiding_spot = arcade.Sprite("childhood.png", SPRITE_SCALING_HIDING_SPOT)
        self.hiding_spot.center_x = 200
        self.hiding_spot.center_y = 475
        self.hiding_spot_list.append(self.hiding_spot)
        self.hiding_spot = arcade.Sprite("sailing-boat.png", SPRITE_SCALING_HIDING_SPOT)
        self.hiding_spot.center_x = 630
        self.hiding_spot.center_y = 470
        self.hiding_spot_list.append(self.hiding_spot)

        # Calls function to hide dog in random spot
        hide_dog(self.dog_sprite, self.hiding_spot_list)

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

        # Checks if there are any lives left
        # If there aren't, it displays game over output
        if self.lives <= 0:
            game_over_output = f"You lose! Your score was {self.score}"
            arcade.draw_text(game_over_output, 100, 300, arcade.color.BLACK, 36)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handles mouse motion """
        if self.lives > 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """
        if button == arcade.MOUSE_BUTTON_LEFT:
            print("Left mouse button pressed at", x, y)

            if arcade.check_for_collision(self.player_sprite, self.dog_sprite):
                hide_dog(self.dog_sprite, self.hiding_spot_list)
                arcade.play_sound(self.good_sound)
                self.score += 10
            else:
                if self.lives > 0:
                    self.lives -= 1
                    arcade.play_sound(self.bad_sound)

        elif button == arcade.MOUSE_BUTTON_RIGHT:
            print("Right mouse button pressed at", x, y)


def main():
    """ Open window and call other functions """
    # Open a 600 x 600 window called Lab 12 - Fitzpatrick.
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, " Lab 12 - Fitzpatrick ")
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()


# Check if import name is equal to main.
# If it is, run main.
if __name__ == "__main__":
    main()
