import arcade
import copy
import startscreen



WIDTH = 800
HEIGHT = 800

rowCount = 6
columnCount = 7
width = 85
height = 85
margins = 5
screenWidth = (width + margins) * columnCount + margins
screenHeight = (height + margins) * rowCount + margins
turn = 1
turnTxt = "Player 1's turn"

class Connect4(arcade.View):
    def __init__(self,p1color,p2color):
        super().__init__()

        self.grid = []
        for row in range(rowCount):
            self.grid.append([])
            for column in range(columnCount):
                self.grid[row].append(0)
        self.player1color = p1color
        self.player2color = p2color
        
        arcade.set_background_color(arcade.color.LIGHT_BLUE)
    
    def horizWin(self,grid):
        win=[0,False]

        p1tokens=0
        p2tokens=0
        for row in grid:
            for i in range(len(row)):
                if row[i]==1:
                    p1tokens+=1
                    p2tokens=0
                    if p1tokens>=4:
                        win=[1,True]
                elif row[i]==2:
                    p1tokens=0
                    p2tokens+=1
                    if p2tokens>=4:
                        win=[2,True]
                elif row[i]==0:
                    p1tokens=0
                    p2tokens=0
            p1tokens=0
            p2tokens=0
    
        return win
            

    def vertWin(self,grid):
        win=[0,False]

        p1tokens=0
        p2tokens=0

        for i in range(len(grid[0])):
            for row in grid:
                if row[i]==1:
                    p1tokens+=1
                    p2tokens=0
                    if p1tokens>=4:
                        win=[1,True]
                elif row[i]==2:
                    p1tokens=0
                    p2tokens+=1
                    if p2tokens>=4:
                        win=[2,True]
                elif row[i]==0:
                    p1tokens=0
                    p2tokens=0
            p1tokens=0
            p2tokens=0

        return win

    def diagWin1(self,grid):
        win=[0,False]

        p1tokens=0
        p2tokens=0
        i = 0
        for column in range (len(grid[0]) - 2):
            for row in grid:
                if i > 6:
                    continue
                elif row[i]==1:
                    p1tokens+=1
                    p2tokens=0
                    if p1tokens>=4:
                        win=[1,True]
                elif row[i]==2:
                    p1tokens=0
                    p2tokens+=1
                    if p2tokens>=4:
                        win=[2,True]
                elif row[i]==0:
                    p1tokens=0
                    p2tokens=0
                i += 1
            i = column
            p1tokens=0
            p2tokens=0



        i = 0
        for r in range(len(grid[1:4])):
            for row in grid[r:]:
                if row[i]==1:
                    p1tokens+=1
                    p2tokens=0
                    if p1tokens>=4:
                        win=[1,True]
                elif row[i]==2:
                    p1tokens=0
                    p2tokens+=1
                    if p2tokens>=4:
                        win=[2,True]
                elif row[i]==0:
                    p1tokens=0
                    p2tokens=0
                i += 1
            i = 0
            p1tokens=0
            p2tokens=0

        return win 

    def diagWin2(self,grid):
        win=[0,False]
        gridTemp = copy.deepcopy(grid)
        p1tokens=0
        p2tokens=0
        i=0

        for i in range (len(gridTemp)):
            gridTemp[i].reverse()

        for column in range (len(gridTemp[0]) - 2):
            for row in gridTemp:
                if i > 6:
                    continue
                elif row[i]==1:
                    p1tokens+=1
                    p2tokens=0
                    if p1tokens>=4:
                        win=[1,True]
                elif row[i]==2:
                    p1tokens=0
                    p2tokens+=1
                    if p2tokens>=4:
                        win=[2,True]
                elif row[i]==0:
                    p1tokens=0
                    p2tokens=0
                i += 1

            i = column
            p1tokens=0
            p2tokens=0



        i = 0
        for r in range(len(gridTemp[1:4])):
            for row in gridTemp[r:]:
                if row[i]==1:
                    p1tokens+=1
                    p2tokens=0
                    if p1tokens>=4:
                        win=[1,True]
                elif row[i]==2:
                    p1tokens=0
                    p2tokens+=1
                    if p2tokens>=4:
                        win=[2,True]
                elif row[i]==0:
                    p1tokens=0
                    p2tokens=0
                i += 1
            i = 0
            p1tokens=0
            p2tokens=0

        return win 
        
    def win(self, grid):
        hor = self.horizWin(grid)
        vert = self.vertWin(grid)
        dia1 = self.diagWin1(grid)
        dia2 = self.diagWin2(grid)
        for wins in (hor,vert,dia1,dia2):
            if wins[1] == True:
                return wins
        return [0,False]
        
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        global turn
        global turnTxt

        if not (self.win(self.grid)[1]):
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
        if self.win(self.grid)[1]:
            turnTxt = 'Player ' + str(self.win(self.grid)[0]) + ' won the game! Press Esc to play again.'

        if key == arcade.key.ESCAPE:
            turnTxt = "Player 1's turn"
            menu_view = startscreen.MenuView()
            self.window.show_view(menu_view)
            menu_view.setup()
                    

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
                    tokencolor = self.player1color
                elif self.grid[row][column] == 2:
                    tokencolor = self.player2color

                # Draw the box
                arcade.draw_rectangle_filled(x+80, y, width, height, color)
                arcade.draw_text(str(column),x+80,550,arcade.color.BLACK, font_size=20, anchor_x="center")
                arcade.draw_circle_filled(x+80,y,30,tokencolor)
        
        arcade.draw_rectangle_filled(WIDTH/2, 750, 700, 85, arcade.color.WHITE)
        arcade.draw_text("On your keyboard, press on the number corresponding to\nthe column you want to place your token in.\nPress Esc to reset.", WIDTH/2,715,
                         arcade.color.BLACK, font_size=20, anchor_x="center")


        arcade.draw_text(turnTxt, WIDTH/2,625,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

        arcade.draw_text("NORMAL MODE", 100,675,
                         arcade.color.BLACK, font_size=20, anchor_x="center")