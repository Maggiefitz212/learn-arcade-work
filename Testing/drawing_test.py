import arcade

WIDTH = 60
HEIGHT = 60
MARGIN = 8
ROW_COUNT = 10
COLUMN_COUNT = 10
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLUEBERRY)

        self.grid = []
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)

        # Row first, then column (y, x)
        self.grid[2][5] = 1
        print(self.grid)

    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                x = WIDTH / 2 + column * (WIDTH + MARGIN) + MARGIN
                y = HEIGHT / 2 + row * (WIDTH + MARGIN) + MARGIN
                if self.grid[row][column] == 1:
                    color = arcade.color.AFRICAN_VIOLET
                else:
                    color = arcade.color.GRANNY_SMITH_APPLE

                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        row = y // (HEIGHT + MARGIN)
        column = x // (WIDTH + MARGIN)
        print("Clicked at:", column + 1, row + 1)
        if self.grid[row][column] == 0:
            self.grid[row][column] = 1
        else:
            self.grid[row][column] = 0


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
