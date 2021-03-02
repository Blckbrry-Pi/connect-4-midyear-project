import arcade
# from connect4 import Connect4
from startscreen import *


def main():
    """ Startup """
    window = arcade.Window(WIDTH, HEIGHT, "Connect Four")
    menu_view = MenuView()
    window.show_view(menu_view)
    menu_view.setup()
    arcade.run()

main()