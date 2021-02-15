import arcade
from connect4copy import *

def main():
    """ Startup """
    window = arcade.Window(WIDTH, HEIGHT, "Connect Four")
    menu_view = MenuView()
    window.show_view(menu_view)
    menu_view.setup()
    arcade.run()


if __name__ == "__main__":
    main()