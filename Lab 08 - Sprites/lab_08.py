import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.05
SPRITE_SCALING_TREAT = 0.05
SPRITE_SCALING_COOKIE = 0.03

TREAT_COUNT = 50
COOKIE_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 8 - Sprites")

        # Variables that will hold sprite lists
        self.player_list = None
        self.treat_list = None
        self.cookie_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

        # Load sound when the game is started
        self.good_sound = arcade.load_sound("Picked Coin Echo 2.wav")
        self.bad_sound = arcade.load_sound("mixkit-apartment-buzzer-bell-press-932.wav")

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.treat_list = arcade.SpriteList()
        self.cookie_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("toppng.com-cute-dog-clipart-clipart-panda-free"
                                           "-clipart-images-dog-clipart-cute-4766x5173.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(TREAT_COUNT):
            # Create the treat instance
            # Treat image from kenney.nl
            treat = Treat("kisspng-labrador-retriever-puppy-bone-drawing-clip-art-free-dog-bone-clipart-"
                          "5aaba1f1a3fb81.0608378215211975536717.png", SPRITE_SCALING_TREAT)

            # Position the coin
            treat.center_x = random.randrange(SCREEN_WIDTH)
            treat.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.treat_list.append(treat)

        # Create the cookies
        for i in range(COOKIE_COUNT):
            # Create the cookie instance
            # Cookie image from kenney.nl
            cookie = Cookie("NicePng_cookie-png_34513.png", SPRITE_SCALING_COOKIE)

            # Position the coin
            cookie.center_x = random.randrange(SCREEN_WIDTH)
            cookie.center_y = random.randrange(SCREEN_HEIGHT)
            cookie.change_x = random.randrange(-3, 4)
            if cookie.change_x == 0:
                cookie.change_x += 1
            cookie.change_y = random.randrange(-3, 4)
            if cookie.change_y == 0:
                cookie.change_y += 1

            # Add the coin to the lists
            self.cookie_list.append(cookie)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.treat_list.draw()
        self.player_list.draw()
        self.cookie_list.draw()

        # Put the score and game over on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        if len(self.treat_list) == 0:
            screen_text = f"Game Over!"
            arcade.draw_text(screen_text, 320, 220, arcade.color.WHITE, 36)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """
        if len(self.treat_list) > 0:
            # Move the center of the player sprite to match the mouse x, y
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """
        if len(self.treat_list) > 0:
            self.treat_list.update()
            self.cookie_list.update()

        # Generate a list of all sprites that collided with the player.
        treats_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                               self.treat_list)
        cookies_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                self.cookie_list)

        # Loop through each colliding treat, remove it, and add to the score.
        for treat in treats_hit_list:
            arcade.play_sound(self.good_sound)
            treat.remove_from_sprite_lists()
            self.score += 1

        # Loop through each colliding cookie, remove it, and decrease the score by 1
        for cookie in cookies_hit_list:
            arcade.play_sound(self.bad_sound)
            cookie.remove_from_sprite_lists()
            self.score -= 1


class Treat(arcade.Sprite):
    """ This class represents the treats on the screen. It is a child class of the arcade library's sprite class."""

    def reset_pos(self):
        # Resets treat to random spot above the top of the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        # Move the coin down screen vertically
        self.center_y -= 1

        # Reset treats to the top when they go off the screen
        if self.top < 0:
            self.reset_pos()


class Cookie(arcade.Sprite):
    """ This class represents the cookies on the screen. It is a child class of the arcade library's sprite class. """

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):
        # Move the cookies
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then bounce
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
