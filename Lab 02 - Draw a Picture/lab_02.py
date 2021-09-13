# Import the Arcade library.

import arcade

# Open a 600 X 600 window called Lab 2 - Fitzpatrick.
arcade.open_window(600, 600, "Lab 2 - Fitzpatrick")

# Set the background color.
arcade.set_background_color(arcade.csscolor.PALE_TURQUOISE)

# Get ready to draw.
arcade.start_render()

# Draw four different colored arcs that arch across the whole window to look like a sunset.
arcade.draw_arc_filled(300, 300, 530, 450, arcade.csscolor.RED, 0, 180)
arcade.draw_arc_filled(300, 300, 500, 420, arcade.csscolor.ORANGE_RED, 0, 180)
arcade.draw_arc_filled(300, 300, 450, 400, arcade.csscolor.GOLD, 0, 180)
arcade.draw_arc_filled(300, 300, 350, 350, arcade.color.LEMON, 0, 180)

# Draw a grassy field with a river running through it.
arcade.draw_lrtb_rectangle_filled(0, 600, 300, 0, arcade.csscolor.LIME_GREEN)
arcade.draw_polygon_filled(((200, 0),
                            (400, 0),
                            (298, 300),
                            (302, 300),
                            ),
                           arcade.csscolor.TURQUOISE)

# Draw black birds flying past sunset
arcade.draw_triangle_filled(390, 400, 395, 400, 385, 395, arcade.csscolor.BLACK)
arcade.draw_triangle_filled(395, 405, 400, 405, 405, 410, arcade.csscolor.BLACK)

# Draw two fences with a collection of blanched almond lines on both sides of the river
arcade.draw_line(20, 250, 250, 250, arcade.csscolor.BLANCHED_ALMOND, 10)
arcade.draw_line(20, 200, 250, 200, arcade.csscolor.BLANCHED_ALMOND, 10)
arcade.draw_line(50, 275, 50, 150, arcade.csscolor.BLANCHED_ALMOND, 10)
arcade.draw_line(220, 275, 220, 150, arcade.csscolor.BLANCHED_ALMOND, 10)

arcade.draw_line(350, 250, 570, 250, arcade.csscolor.BLANCHED_ALMOND, 10)
arcade.draw_line(350, 200, 570, 200, arcade.csscolor.BLANCHED_ALMOND, 10)
arcade.draw_line(380, 275, 380, 150, arcade.csscolor.BLANCHED_ALMOND, 10)
arcade.draw_line(540, 275, 540, 150, arcade.csscolor.BLANCHED_ALMOND, 10)

# Draw little black arcs on ends of fences to make them look 3-D
arcade.draw_arc_outline(24, 250, 10, 10, arcade.csscolor.BLACK, 180, 270, 2)
arcade.draw_arc_outline(24, 200, 10, 10, arcade.csscolor.BLACK, 180, 270, 2)
arcade.draw_arc_outline(50, 271, 10, 10, arcade.csscolor.BLACK, 0, 90, 2)
arcade.draw_arc_outline(220, 271, 10, 10, arcade.csscolor.BLACK, 0, 90, 2)

arcade.draw_arc_outline(354, 250, 10, 10, arcade.csscolor.BLACK, 180, 270, 2)
arcade.draw_arc_outline(354, 200, 10, 10, arcade.csscolor.BLACK, 180, 270, 2)
arcade.draw_arc_outline(380, 271, 10, 10, arcade.csscolor.BLACK, 0, 90, 2)
arcade.draw_arc_outline(540, 271, 10, 10, arcade.csscolor.BLACK, 0, 90, 2)

# Finish the drawing.
arcade.finish_render()

# Keep the window open until someone closes it.
arcade.run()
