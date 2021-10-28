import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class Ball:
    def __init__(self, position_x, position_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)


def draw_sunset(x, y):
    """ Draw the sunset """

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 10)

    # Draw four different colored arcs that arch across the whole window to look like a sunset.
    arcade.draw_arc_filled(x, y, 530, 450, arcade.csscolor.RED, 0, 180)
    arcade.draw_arc_filled(x, y, 500, 420, arcade.csscolor.ORANGE_RED, 0, 180)
    arcade.draw_arc_filled(x, y, 450, 400, arcade.csscolor.GOLD, 0, 180)
    arcade.draw_arc_filled(x, y, 350, 350, arcade.color.LEMON, 0, 180)


def draw_birds(x, y):
    """ Draw black birds """

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 2)

    # Draw black birds flying past sunset
    arcade.draw_triangle_filled(x, y, x + 5, y + 5, x - 5, y - 5, arcade.color.BLACK)


def draw_field_and_river(x, y):
    """ Draw field with river running through it. """

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 10)

    # Draw a grassy field with a river running through it.
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 2, 0, arcade.csscolor.LIME_GREEN)
    arcade.draw_polygon_filled(((x, y),
                                (x + 200, y),
                                (x + 98, y + 300),
                                (x + 102, y + 300),
                                ),
                                arcade.csscolor.TURQUOISE)

def draw_fence(x, y):

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # Draw two fences with a collection of blanched almond lines on both sides of the river
    arcade.draw_line(x, y, x + 230, y, arcade.csscolor.BLANCHED_ALMOND, 10)
    arcade.draw_line(x, y - 50, x + 230, y - 50, arcade.csscolor.BLANCHED_ALMOND, 10)
    arcade.draw_line(x + 30, y + 25, x + 30, y - 100, arcade.csscolor.BLANCHED_ALMOND, 10)
    arcade.draw_line(x + 200, y + 25, x + 200, y - 100, arcade.csscolor.BLANCHED_ALMOND, 10)


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.csscolor.TURQUOISE)

        # Create our ball
        self.ball = Ball(50, 50, 15, arcade.color.BLACK)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()
        # Draw sunset
        draw_sunset(300, 300)

        # Draw a field with a river going through it
        draw_field_and_river(200, 0)

        # Draw black birds at three different places
        draw_birds(390, 400)
        draw_birds(395, 405)

        # Draw a fence at two different places.
        draw_fence(20, 250)
        draw_fence(350, 250)

        arcade.finish_render()

    def on_mouse_motion(self, x, y, dx, dy):
         """ Updates the ball's position """
         self.ball.position_x = x
         self.ball.position_y = y

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 07 - Fitzpatrick")
    arcade.run()


main()