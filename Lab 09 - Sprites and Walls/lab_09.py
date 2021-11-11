"""
Scroll around a large screen.

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_scrolling
"""

import arcade
import random

SPRITE_SCALING = 1

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Lab 09 - Sprites and Walls"

NUMBER_OF_CAKES = 20

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 7


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.cake_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

        # Load sound when the game starts
        self.cake_sound = arcade.load_sound("Picked Coin Echo 2.wav")

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.cake_list = arcade.SpriteList()

        # Set up the score
        self.score = 0

        # Set up the player
        # Player from kenney.nl
        self.player_sprite = arcade.Sprite("player_walk2.png",
                                           scale=0.8)
        self.player_sprite.center_x = 256
        self.player_sprite.center_y = 512
        self.player_list.append(self.player_sprite)

        # Wall sprites from kenney.nl
        for x in range(0, 1024, 64):
            wall = arcade.Sprite("wallHalf_top.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 1024
            self.wall_list.append(wall)

        for y in range(0, 1024, 64):
            wall = arcade.Sprite("wallHalf_right.png", SPRITE_SCALING)
            wall.center_x = 960
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(0, 1024, 64):
            wall = arcade.Sprite("wallHalf_bottom.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 0
            self.wall_list.append(wall)

        for y in range(0, 1024, 64):
            wall = arcade.Sprite("wallHalf_left.png", SPRITE_SCALING)
            wall.center_x = 0
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(192, 512, 64):
            wall = arcade.Sprite("towerSquare.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 256
            self.wall_list.append(wall)

        for y in range(192, 510, 64):
            wall = arcade.Sprite("towerSquare.png", SPRITE_SCALING)
            wall.center_x = 128
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(256, 896, 64):
            wall = arcade.Sprite("towerSquare.png", SPRITE_SCALING)
            wall.center_x = 510
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(510, 936, 64):
            wall = arcade.Sprite("towerSquare.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 384
            self.wall_list.append(wall)

        for x in range(620, 832, 64):
            wall = arcade.Sprite("towerSquare.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 210
            self.wall_list.append(wall)

        for y in range(264, 330, 64):
            wall = arcade.Sprite("towerSquare.png", SPRITE_SCALING)
            wall.center_x = 812
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(146, 210, 64):
            wall = arcade.Sprite("towerSquare.png", SPRITE_SCALING)
            wall.center_x = 620
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(574, 832, 64):
            wall = arcade.Sprite("towerSquare.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 832
            self.wall_list.append(wall)

        for x in range(638, 896, 64):
            wall = arcade.Sprite("towerSquare.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 685
            self.wall_list.append(wall)

        for y in range(560, 685, 64):
            wall = arcade.Sprite("towerSquare.png", SPRITE_SCALING)
            wall.center_x = 638
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(702, 832, 64):
            wall = arcade.Sprite("towerSquare.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 538
            self.wall_list.append(wall)

        for y in range(640, 1024, 64):
            wall = arcade.Sprite("towerSquare.png", SPRITE_SCALING)
            wall.center_x = 256
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(128, 448, 64):
            wall = arcade.Sprite("towerSquare.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 448
            self.wall_list.append(wall)

        for x in range(128, 256, 64):
            wall = arcade.Sprite("towerSquare.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 640
            self.wall_list.append(wall)

        for i in range(NUMBER_OF_CAKES):
            # Set up the cake
            # Cake from kenney.nl
            cake = arcade.Sprite("cakeBirthday_SE.png",
                                 scale=0.25)

            # Boolean variable if we successfully placed the cake
            cake_placed_successfully = False

            # Keep trying until success
            while not cake_placed_successfully:
                # Position the cake
                cake.center_x = random.randrange(DEFAULT_SCREEN_WIDTH)
                cake.center_y = random.randrange(DEFAULT_SCREEN_HEIGHT)

                # See if the cake is hitting a wall
                wall_hit_list = arcade.check_for_collision_with_list(cake, self.wall_list)

                # See if the cake is hitting another cake
                cake_hit_list = arcade.check_for_collision_with_list(cake, self.cake_list)

                if len(wall_hit_list) == 0 and len(cake_hit_list) == 0:
                    cake_placed_successfully = True

            # Add the cake to the lists
            self.cake_list.append(cake)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Select the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.cake_list.draw()

        # Select the camera that isn't scrolling for our GUI
        self.camera_gui.use()

        # Draw the score
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 50, arcade.color.BROWN, 36)
        if len(self.cake_list) == 0:
            game_over_text = f"You Win!"
            arcade.draw_text(game_over_text, 280, 300, arcade.color.BROWN, 36)

        # Draw the GUI
        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     40,
                                     arcade.color.ALMOND)
        text = f"Scroll value: ({self.camera_sprites.position[0]:5.1f}, " \
               f"{self.camera_sprites.position[1]:5.1f})"
        arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        if len(self.cake_list) != 0:
            self.physics_engine.update()
            self.cake_list.update()

        # Generate a list of when the player hit a cake
        cake_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.cake_list)

        # Remove each colliding sprite from hit_list and add points to score
        for self.cake in cake_hit_list:
            arcade.play_sound(self.cake_sound)
            self.cake.remove_from_sprite_lists()
            self.score += 1
        # Scroll the screen to the player
        self.scroll_to_player()

    def scroll_to_player(self):
        """
        Scroll the window to the player.

        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        Anything between 0 and 1 will have the camera move to the location with a smoother
        pan.
        """

        position = self.player_sprite.center_x - self.width / 2, \
            self.player_sprite.center_y - self.height / 2
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        """
        Resize window
        Handle the user grabbing the edge and resizing the window.
        """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
