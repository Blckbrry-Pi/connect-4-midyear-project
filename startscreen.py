import arcade
import copy
import connect4

WIDTH = 800
HEIGHT = 800



class MenuView(arcade.View):
    """ Class that manages the 'menu' view. """
    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__()
        self.background = None
        self.token = None


    def setup(self):
        self.background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")
        token = arcade.Sprite(":resources:images/items/gold_1.png",1.5)
        token.center_x = WIDTH/2
        token.center_y = 650
        self.token = token

    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            WIDTH, HEIGHT,
                                            self.background)
        arcade.draw_rectangle_filled(WIDTH/2, 525, 700, 100, arcade.color.WHITE)
        arcade.draw_text("Player 1 - choose your color", WIDTH/2,500,
                         arcade.color.BLACK, font_size=40, anchor_x="center")

        self.token.draw()
        arcade.draw_rectangle_filled(WIDTH/2, 300, 600, 125, arcade.color.WHITE)

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
        
        



class MenuView2(arcade.View):
    """ Manage the 'game' view for our program. """
    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__()
        self.background = None
        self.token = None


    def setup(self):
        self.background = arcade.load_texture(":resources:images/backgrounds/abstract_2.jpg")
        token = arcade.Sprite(":resources:images/items/coinSilver_test.png",1.5)
        token.center_x = WIDTH/2
        token.center_y = 650
        self.token = token

    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            WIDTH, HEIGHT,
                                            self.background)
        arcade.draw_rectangle_filled(WIDTH/2, 525, 700, 100, arcade.color.WHITE)
        arcade.draw_text("Player 2 - choose your color", WIDTH/2,500,
                         arcade.color.BLACK, font_size=40, anchor_x="center")
        
        self.token.draw()
        arcade.draw_rectangle_filled(WIDTH/2, 300, 600, 125, arcade.color.WHITE)
        
        x = 200
        y = 300
        width = 75
        height = 75

        for color in colors:
            arcade.draw_rectangle_filled(x, y, width, height, color)
            x += width + 55
    

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ Use a mouse press to advance to the 'game' view. """
        global player2color
        global player1color

        if _x >= 162.5 and _x <= 237.5 and _y >= 262.5 and _y <= 337.5:
            player2color = colors[0]  #player.color = arcade.color.RED
            c4 = connect4.Connect4(player1color,player2color)
            self.window.show_view(c4)
        elif _x >= 292.5 and _x <= 367.5 and _y >= 262.5 and _y <= 337.5:
            player2color = colors[1]
            c4 = connect4.Connect4(player1color,player2color)
            self.window.show_view(c4)
        elif _x >= 422.5 and _x <= 497.5 and _y >= 262.5 and _y <= 337.5:
            player2color = colors[2]
            c4 = connect4.Connect4(player1color,player2color)
            self.window.show_view(c4)
        else:
            arcade.set_background_color(arcade.color.WHITE)