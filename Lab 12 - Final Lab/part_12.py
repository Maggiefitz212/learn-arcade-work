import arcade

# Create and set the constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.01
SPRITE_SCALING_DOG = 0.05
SPRITE_SCALING_HIDING_SPOT = 0.05
HIDING_SPOT_COUNT = 5


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

        # Set up the physics engine.
        self.physics_engine = None

        # Create two cameras: one for the sprite and one for the GUI.
        # The sprite camera scrolls, but the GUI one does not.
        self.camera_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

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

        # Set up the player, dog, and hiding spot.
        # Dog sprite from kenney.nl
        self.dog_sprite = arcade.Sprite("Daco_3805650.png", SPRITE_SCALING_DOG)
        # Player sprite from opengameart.org
        self.player_sprite = arcade.Sprite("Idle (1).png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)
        # Create the five different hiding spots
        # All hiding spots from flaticon.com created by Freepik
        self.hiding_spot = arcade.Sprite("playground.png", SPRITE_SCALING_HIDING_SPOT)
        self.hiding_spot_list.append(self.hiding_spot)
        self.hiding_spot = arcade.Sprite("fountain.png", SPRITE_SCALING_HIDING_SPOT)
        self.hiding_spot_list.append(self.hiding_spot)
        self.hiding_spot = arcade.Sprite("slide.png", SPRITE_SCALING_HIDING_SPOT)
        self.hiding_spot_list.append(self.hiding_spot)
        self.hiding_spot = arcade.Sprite("seesaw.png", SPRITE_SCALING_HIDING_SPOT)
        self.hiding_spot_list.append(self.hiding_spot)
        self.hiding_spot = arcade.Sprite("bridge.png", SPRITE_SCALING_HIDING_SPOT)
        self.hiding_spot_list.append(self.hiding_spot)


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
