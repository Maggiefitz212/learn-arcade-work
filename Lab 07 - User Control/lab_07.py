import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3


def draw_sunset(x, y):
    """ Draw the sunset """
    # Draw four different colored arcs that arch across the whole window to look like a sunset.
    arcade.draw_arc_filled(x, y, 530, 450, arcade.csscolor.RED, 0, 180)
    arcade.draw_arc_filled(x, y, 500, 420, arcade.csscolor.ORANGE_RED, 0, 180)
    arcade.draw_arc_filled(x, y, 450, 400, arcade.csscolor.GOLD, 0, 180)
    arcade.draw_arc_filled(x, y, 350, 350, arcade.color.LEMON, 0, 180)


def draw_birds(x, y):
    """ Draw black birds """
    # Draw black birds flying past sunset
    arcade.draw_triangle_filled(x, y, x + 5, y + 5, x - 5, y - 5, arcade.color.BLACK)


def draw_field_and_river(x, y):
    """ Draw field with river running through it. """
    # Draw a grassy field with a river running through it.
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 2, 0, arcade.csscolor.LIME_GREEN)
    arcade.draw_polygon_filled(((x, y),
                                (x + 200, y),
                                (x + 98, y + 300),
                                (x + 102, y + 300),
                                ),
                               arcade.csscolor.TURQUOISE)


def draw_fence(x, y):
    # Draw two fences with a collection of blanched almond lines on both sides of the river
    arcade.draw_line(x, y, x + 230, y, arcade.csscolor.BLANCHED_ALMOND, 10)
    arcade.draw_line(x, y - 50, x + 230, y - 50, arcade.csscolor.BLANCHED_ALMOND, 10)
    arcade.draw_line(x + 30, y + 25, x + 30, y - 100, arcade.csscolor.BLANCHED_ALMOND, 10)
    arcade.draw_line(x + 200, y + 25, x + 200, y - 100, arcade.csscolor.BLANCHED_ALMOND, 10)


class MyGame(arcade.Window):

    def __init__(self):

        # Call the parent class's init function
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        # Load the ouch and nature sounds when the application starts
        self.nature_sound = arcade.load_sound("Outdoor_Ambiance.mp3")
        self.ouch_sound = arcade.load_sound("ouch1 (1).mp3")
        self.ouch_sound_player = None

        # Make the mouse disappear when it is over the window
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.csscolor.TURQUOISE)

        # Create our ball
        self.hot_air_balloon = HotAirBalloon(50, 50, 15, 20, 10, arcade.color.PURPLE)
        self.penguin = Penguin(50, 50, 0, 0, 15, arcade.color.ARMY_GREEN)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        draw_sunset(300, 300)
        draw_field_and_river(200, 0)
        draw_birds(390, 400)
        draw_fence(20, 250)
        draw_fence(350, 250)
        self.hot_air_balloon.draw()
        self.penguin.draw()

    def update(self, delta_time):
        self.penguin.update()
        if self.penguin.position_x <= self.penguin.radius + 8 or self.penguin.position_x >= \
                SCREEN_WIDTH - (self.penguin.radius + 10):
            if not self.ouch_sound_player or not self.ouch_sound_player.playing:
                self.ouch_sound_player = arcade.play_sound(self.ouch_sound)

        if self.penguin.position_y <= self.penguin.radius + 12 or self.penguin.position_y >= \
                SCREEN_HEIGHT - (self.penguin.radius + 45):
            if not self.ouch_sound_player or not self.ouch_sound_player.playing:
                self.ouch_sound_player = arcade.play_sound(self.ouch_sound)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Updates the ball's position """
        self.hot_air_balloon.position_x = x
        self.hot_air_balloon.position_y = y

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.penguin.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.penguin.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.penguin.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.penguin.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.SPACE:
            arcade.play_sound(self.nature_sound)

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.penguin.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.penguin.change_y = 0


class HotAirBalloon:
    def __init__(self, position_x, position_y, radius, width, height, color):
        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_line(self.position_x - 10, self.position_y - 17, self.position_x - 10, self.position_y - 37,
                         arcade.color.BLANCHED_ALMOND, 5)
        arcade.draw_line(self.position_x + 10, self.position_y - 17, self.position_x + 10, self.position_y - 37,
                         arcade.color.BLANCHED_ALMOND, 5)
        arcade.draw_ellipse_filled(self.position_x, self.position_y, 45, 60, self.color, 0, -1)
        arcade.draw_arc_filled(self.position_x, self.position_y - 37, 40, 80, arcade.color.BROWN, 180, 360)


class Penguin:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the penguin with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)
        arcade.draw_ellipse_filled(self.position_x, self.position_y, 50, 60, arcade.color.BLACK, 0, -1)
        arcade.draw_ellipse_filled(self.position_x, self.position_y, 30, 40, arcade.color.WHITE, 0, -1)
        arcade.draw_circle_filled(self.position_x, self.position_y + 40, self.radius + 5, arcade.color.BLACK, 0, -1)
        arcade.draw_circle_filled(self.position_x, self.position_y + 40, self.radius - 2, arcade.color.WHITE)
        arcade.draw_circle_filled(self.position_x - 5, self.position_y + 45, self.radius - 12, arcade.color.BLACK)
        arcade.draw_circle_filled(self.position_x + 5, self.position_y + 45, self.radius - 12, arcade.color.BLACK)
        arcade.draw_triangle_filled(self.position_x, self.position_y + 40, self.position_x, self.position_y + 30,
                                    self.position_x + 10, self.position_y + 32, arcade.color.YELLOW_ORANGE)

    def update(self):
        self.position_x += self.change_x
        self.position_y += self.change_y

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius + 8:
            self.position_x = self.radius + 8

        if self.position_x > SCREEN_WIDTH - (self.radius + 10):
            self.position_x = SCREEN_WIDTH - (self.radius + 10)

        if self.position_y < self.radius + 12:
            self.position_y = self.radius + 12

        if self.position_y > SCREEN_HEIGHT - (self.radius + 45):
            self.position_y = SCREEN_HEIGHT - (self.radius + 45)


def main():
    window = MyGame()
    arcade.run()


main()
