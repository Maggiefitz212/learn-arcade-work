# Import the arcade

import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


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


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 3 - Fitzpatrick")
    arcade.set_background_color(arcade.color.PALE_TURQUOISE)
    arcade.start_render()

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

    # Finish and run the drawing
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()
