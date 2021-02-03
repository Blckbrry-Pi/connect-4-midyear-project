import arcade

rowCount = 6
columnCount = 7
width = 50
height = 50
margins = 5
screenWidth = (width + margins) * columnCount + margins
screenHeight = (height + margins) * rowCount + margins
title = "Connect 4"

class Connect4(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.grid = []
        for row in range(rowCount):
            self.grid.append([])
            for column in range(columnCount):
                self.grid[row].append(0)

        arcade.set_background_color(arcade.color.BLUE)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the grid
        for row in range(rowCount):
            for column in range(columnCount):
                # Figure out what color to draw the box
                if self.grid[row][column] == 1:
                    color = arcade.color.RED
                elif self.grid[row][column] == 2:
                    color = arcade.color.YELLOW
                else:
                    color = arcade.color.WHITE

                # Do the math to figure out where the box is
                x = (margins + width) * column + margins + width // 2
                y = (margins + height) * row + margins + height // 2

                # Draw the box
                arcade.draw_rectangle_filled(x, y, width, height, color)



def main():
    Connect4(screenWidth, screenHeight, title)
    arcade.run()

main()