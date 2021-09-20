# Import the arcade

import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


def draw_sunset(x, y):
    """ Draw the sunset """

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

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


def draw_fence(x1, y1, x2, y2):
    # Draw two fences with a collection of blanched almond lines on both sides of the river
    arcade.draw_line(x1, y1, x2, y2, arcade.csscolor.BLANCHED_ALMOND, 10)
    arcade.draw_line(x1, y1 - 50, x2, y2 - 50, arcade.csscolor.BLANCHED_ALMOND, 10)
    arcade.draw_line(x1 + 30, y1 + 25, x2 - 200, y2 - 100, arcade.csscolor.BLANCHED_ALMOND, 10)
    arcade.draw_line(x1 + 200, y1 + 25, x2 - 30, y2 - 100, arcade.csscolor.BLANCHED_ALMOND, 10)

    arcade.draw_line(x1 + 330, y1, x2 + 320, 250, arcade.csscolor.BLANCHED_ALMOND, 10)
    arcade.draw_line(x1 + 330, y1 - 50, x2 + 320, 200, arcade.csscolor.BLANCHED_ALMOND, 10)
    arcade.draw_line(x1 + 360, y1 + 25, x2 + 130, 150, arcade.csscolor.BLANCHED_ALMOND, 10)
    arcade.draw_line(x1 + 520, y1 + 25, x2 + 290, 150, arcade.csscolor.BLANCHED_ALMOND, 10)

    # Draw little black arcs on ends of fences to make them look 3-D
    arcade.draw_arc_outline(x1 + 4, 250, 10, 10, arcade.csscolor.BLACK, 180, 270, 2)
    arcade.draw_arc_outline(x1 + 4, 200, 10, 10, arcade.csscolor.BLACK, 180, 270, 2)
    arcade.draw_arc_outline(x1 + 30, 271, 10, 10, arcade.csscolor.BLACK, 0, 90, 2)
    arcade.draw_arc_outline(x1 + 200, 271, 10, 10, arcade.csscolor.BLACK, 0, 90, 2)

    arcade.draw_arc_outline(x1 + 334, 250, 10, 10, arcade.csscolor.BLACK, 180, 270, 2)
    arcade.draw_arc_outline(x1 + 334, 200, 10, 10, arcade.csscolor.BLACK, 180, 270, 2)
    arcade.draw_arc_outline(x1 + 360, 271, 10, 10, arcade.csscolor.BLACK, 0, 90, 2)
    arcade.draw_arc_outline(x1 + 520, 271, 10, 10, arcade.csscolor.BLACK, 0, 90, 2)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 3 - Fitzpatrick")
    arcade.set_background_color(arcade.color.PALE_TURQUOISE)
    arcade.start_render()

    # Draw sunsets at three different places
    draw_sunset(40, 400)
    draw_sunset(120, 300)
    draw_sunset(70, 350)

    # Draw a grassy field with a river running through it.
    arcade.draw_lrtb_rectangle_filled(0, 600, 300, 0, arcade.csscolor.LIME_GREEN)
    arcade.draw_polygon_filled(((200, 0),
                                (400, 0),
                                (298, 300),
                                (302, 300),
                                ),
                               arcade.csscolor.TURQUOISE)

    # Draw black birds at three different spots
    draw_birds(390, 350)
    draw_birds(450, 400)
    draw_birds(360, 430)

    # Finish and run the drawing
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()
