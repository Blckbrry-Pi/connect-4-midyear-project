import arcade

#import token
#player1 = Token()
#player2 = Token()


WIDTH = 800
HEIGHT = 800



class MenuView(arcade.View):
    """ Class that manages the 'menu' view. """

    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        arcade.draw_text("Player 1 - choose your color", WIDTH/2,500,
                         arcade.color.BLACK, font_size=40, anchor_x="center")
        
        x = 200
        y = 300
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
        global player1color

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
                         arcade.color.BLACK, font_size=40, anchor_x="center")
        
        x = 200
        y = 300
        width = 75
        height = 75

        for color in colors:
            arcade.draw_rectangle_filled(x, y, width, height, color)
            x += width + 55

    

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ Use a mouse press to advance to the 'game' view. """
        connect4 = Connect4()
        global player2color
        player2color = None

        if _x >= 162.5 and _x <= 237.5 and _y >= 262.5 and _y <= 337.5:
            player2color = colors[0]  #player.color = arcade.color.RED
            self.window.show_view(connect4)
        elif _x >= 292.5 and _x <= 367.5 and _y >= 262.5 and _y <= 337.5:
            player2color = colors[1]
            self.window.show_view(connect4)
        elif _x >= 422.5 and _x <= 497.5 and _y >= 262.5 and _y <= 337.5:
            player2color = colors[2]
            self.window.show_view(connect4)
        else:
            arcade.set_background_color(arcade.color.WHITE)
        print (player2color)

rowCount = 6
columnCount = 7
width = 85
height = 85
margins = 5
screenWidth = (width + margins) * columnCount + margins
screenHeight = (height + margins) * rowCount + margins
title = "Connect 4"
turn = 1
turnTxt = "Player 1's turn"

class Connect4(arcade.View):
    def __init__(self):
        super().__init__()

        self.grid = []
        for row in range(rowCount):
            self.grid.append([])
            for column in range(columnCount):
                self.grid[row].append(0)
        
        arcade.set_background_color(arcade.color.LIGHT_BLUE)

    def setup(self):
        pass

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        global turn
        global turnTxt
        for keys in ([arcade.key.KEY_0,0],[arcade.key.KEY_1,1],[arcade.key.KEY_2,2],[arcade.key.KEY_3,3],[arcade.key.KEY_4,4],[arcade.key.KEY_5,5],[arcade.key.KEY_6,6]):
            if key == keys[0]:
                for rowIndex in range(len(self.grid)):
                    if self.grid[rowIndex][keys[1]] == 0:
                        if turn % 2 == 1:
                            self.grid[rowIndex][keys[1]] = 1
                            turnTxt = "Player 2's turn"
                        else:
                            self.grid[rowIndex][keys[1]] = 2
                            turnTxt = "Player 1's turn"
                        turn += 1
                        break
                    

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the grid
        for row in range(rowCount):
            for column in range(columnCount):
                color = arcade.color.WHITE 
                tokencolor = color
                x = (margins + width) * column + margins + width // 2
                y = (margins + height) * row + margins + height // 2

                if self.grid[row][column] == 1:
                    tokencolor = player1color
                elif self.grid[row][column] == 2:
                    tokencolor = player2color

                # Draw the box
                arcade.draw_rectangle_filled(x+80, y, width, height, color)
                arcade.draw_text(str(column),x+80,550,arcade.color.BLACK, font_size=20, anchor_x="center")
                arcade.draw_circle_filled(x+80,y,30,tokencolor)
        
        arcade.draw_rectangle_filled(WIDTH/2, 750, 700, 100, arcade.color.WHITE)
        arcade.draw_text("On your keyboard, press on the number corresponding to\nthe column you want to place your token in.", WIDTH/2,725,
                         arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text(turnTxt, WIDTH/2,625,
                         arcade.color.BLACK, font_size=20, anchor_x="center")
    
    

        


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


