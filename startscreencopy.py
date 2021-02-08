import arcade

#import token
#player1 = Token()
#player2 = Token()


WIDTH = 800
HEIGHT = 600


class MenuView(arcade.View):
    """ Class that manages the 'menu' view. """

    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        arcade.draw_text("Player 1 - choose your color", WIDTH/2,500,
                         arcade.color.BLACK, font_size=30, anchor_x="center")
        
        x = 200
        y = HEIGHT/2
        width = 75
        height = 75
        global colors
        colors = [arcade.color.RED, arcade.color.BLACK, arcade.color.YELLOW, arcade.color.GREEN]
        for color in colors:
            arcade.draw_rectangle_filled(x, y, width, height, color)
            x += width + 55

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ Use a mouse press to advance to the 'game' view. """
        menuView2 = MenuView2()
        menuView2.setup()
        if _x >= 162.5 and _x <= 237.5 and _y >= 262.5 and _y <= 337.5:
            player1color = colors[0]  #player.color = arcade.color.RED
            del colors[0]
            self.window.show_view(menuView2)
        elif _x >= 292.5 and _x <= 367.5 and _y >= 262.5 and _y <= 337.5:
            player1color = colors[1]
            del colors[1]
            self.window.show_view(menuView2)
        elif _x >= 422.5 and _x <= 497.5 and _y >= 262.5 and _y <= 337.5:
            player1color = colors[2]
            del colors[2]
            self.window.show_view(menuView2)
        elif _x >= 552.5 and _x <= 627.5 and _y >= 262.5 and _y <= 337.5:
            player1color = colors[3]
            del colors[3]
            self.window.show_view(menuView2)
        print (player1color)
        


class MenuView2(arcade.View):
    """ Manage the 'game' view for our program. """
    def __init__(self):
        super().__init__()
        # Create variables here

    def setup(self):
        """ This should set up your game and get it ready to play """
        # Replace 'pass' with the code to set up your game
        pass

    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        arcade.draw_text("Player 2 - choose your color", WIDTH/2,500,
                         arcade.color.BLACK, font_size=30, anchor_x="center")
        
        x = 200
        y = HEIGHT/2
        width = 75
        height = 75

        for color in colors:
            arcade.draw_rectangle_filled(x, y, width, height, color)
            x += width + 55

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ Use a mouse press to advance to the 'game' view. """
        connect4 = Connect4()

        if _x >= 162.5 and _x <= 237.5 and _y >= 262.5 and _y <= 337.5:
            player2color = colors[0]  #player.color = arcade.color.RED
            self.window.show_view(connect4)
        elif _x >= 292.5 and _x <= 367.5 and _y >= 262.5 and _y <= 337.5:
            player2color = colors[1]
            self.window.show_view(connect4)
        elif _x >= 422.5 and _x <= 497.5 and _y >= 262.5 and _y <= 337.5:
            player2color = colors[2]
            self.window.show_view(connect4)
        print (player2color)

rowCount = 6
columnCount = 7
width = 85
height = 85
margins = 5
screenWidth = (width + margins) * columnCount + margins
screenHeight = (height + margins) * rowCount + margins
title = "Connect 4"

class Connect4(arcade.View):
    def __init__(self):
        super().__init__()

        self.grid = []
        for row in range(rowCount):
            self.grid.append([])
            for column in range(columnCount):
                self.grid[row].append(0)

        arcade.set_background_color(arcade.color.BLUE)

    def setup(self):
        pass

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
                arcade.draw_rectangle_filled(x+80, y, width, height, color)


class GameOverView(arcade.View):
    """ Class to manage the game over view """
    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """ Draw the game over view """
        arcade.start_render()
        arcade.draw_text("Game Over - press ESCAPE to advance", WIDTH/2, HEIGHT/2,
                         arcade.color.WHITE, 30, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        """ If user hits escape, go back to the main menu view """
        if key == arcade.key.ESCAPE:
            menu_view = MenuView()
            self.window.show_view(menu_view)


def main():
    """ Startup """
    window = arcade.Window(WIDTH, HEIGHT, "Choose Colors")
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()