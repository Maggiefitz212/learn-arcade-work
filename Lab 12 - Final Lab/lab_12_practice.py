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


def hide_dog(dog_sprite):
    # Roll a random number that will decide where to place the dog
    dog_placement_number = random.randrange(8)
    if dog_placement_number == 0:
        # If dog_placement_number is 0, place the dog under the playground
        dog_sprite.center_x = 110
        dog_sprite.center_y = 270
        dog_sprite.angle = 80
    elif dog_placement_number == 1:
        # If dog_placement_number is 1, place the dog under the fountain
        dog_sprite.center_x = 300
        dog_sprite.center_y = 350
        dog_sprite.angle = 0
    elif dog_placement_number == 2:
        # If dog_placement_number is 2, place the dog under the slide
        dog_sprite.center_x = 450
        dog_sprite.center_y = 450
        dog_sprite.angle = 0
    elif dog_placement_number == 3:
        # If dog_placement_number is 3, place the dog under the seesaw
        dog_sprite.center_x = 600
        dog_sprite.center_y = 350
        dog_sprite.angle = 0
    elif dog_placement_number == 4:
        # If dog_placement_number is 4, place the dog under the bridge
        dog_sprite.center_x = 700
        dog_sprite.center_y = 250
        dog_sprite.angle = 0
    elif dog_placement_number == 5:
        # If dog_placement_number is 5, place the dog under the carousel
        dog_sprite.center_x = 550
        dog_sprite.center_y = 120


class InstructionView(arcade.View):
    def on_show(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        arcade.draw_text("Instructions Screen", self.window.width / 2, self.window.height / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", self.window.width / 2, self.window.height / 2-75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_mouse_press(self, x, y, button, modifiers):
        """ If the user presses the mouse button, start the game. """
        game_view = GameView()
        game_view.setup()
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
        self.window.set_mouse_visible(False)

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
        self.player_sprite.center_y = 250
        self.player_list.append(self.player_sprite)

        # Create different hiding spots
        # All hiding spots from flaticon.com created by Freepik
        self.hiding_spot = arcade.Sprite("playground.png", SPRITE_SCALING_HIDING_SPOT)
        self.hiding_spot.center_x = 135
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
        self.hiding_spot.center_x = 575
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
        self.hiding_spot.center_x = 650
        self.hiding_spot.center_y = 500
        self.hiding_spot_list.append(self.hiding_spot)

        self.dog_list.append(self.dog_sprite)
        hide_dog(self.dog_sprite)

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

            if arcade.check_for_collision(self.player_sprite, self.dog_sprite):
                hide_dog(self.dog_sprite)
                arcade.play_sound(self.good_sound)
                self.score += 10
            else:
                self.lives -= 1
                arcade.play_sound(self.bad_sound)

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
