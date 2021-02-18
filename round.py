from model import playerRoster
from grid import Connect4
import arcade

def gameplayRound(self)
    win = False 
    while win = False:


def on_mouse_press(self, _x, _y, _button, _modifiers):
    errorMsg=""
    tokenPlaced = False
    grid = []
    currentCoords = [0,0]
    column1=[0,0,0,0,0,0]
    column2=[0,0,0,0,0,0]
    column3=[0,0,0,0,0,0]
    column4=[0,0,0,0,0,0]
    column5=[0,0,0,0,0,0]
    column6=[0,0,0,0,0,0]
    column7=[0,0,0,0,0,0]
    grid.append(column1)
    grid.append(column2)
    grid.append(column3)
    grid.append(column4)
    grid.append(column5)
    grid.append(column6)
    grid.append(column7)
    if _x>0 and _x<7.14: #EDIT THIS FOR MARGIN/COLUMN LINE ALLOWANCE
        column=column1
    elif _x>7.14 and _x<14.28:
        column=column2
    elif _x>14.28 and _x<21.42:
        column=column3
    elif _x>21.42 and _x<28.56:
        column=column4
    elif _x>28.56 and _x<35.7:
        column=column5
    elif _x>35.7 and _x<42.84:
        column=column6
    elif _x>42.84 and _x<50:
        column=column7
    if column[5]==0:
        column[5]=1
    elif column[5]==1:
        if column[4]==0:
            column[4]=1
            tokenPlaced = True
        elif column[4]==1:
            if column[3]==0:
                column[3]=1
                tokenPlaced = True
            elif column[3]==1:
                if column[2]==0:
                    column[2]=1
                    tokenPlaced=True
                elif column[2]==1:
                    if column[1]==0:
                        column[1]=1
                        tokenPlaced=True
                    elif column[1]==1:
                        if column[0]==0:
                            column[0]=1
                            tokenPlaced = True
                        elif column[0]==1:
                            errorMsg="Error: column does not have any free spaces"
    print(errorMsg)




def vertWin(self,grid):
    win=False
    p1win=False
    p2win=False
    p1tokens=0
    p2tokens=0
    for column in grid:
        for i in column:
            if column[i]==1:
                p1tokens+=1
            elif column[i]==2:
                p1tokens=0
                p2tokens+=1
            elif column[i]==0:
                p1tokens=0
                p2tokens=0
    if p1tokens>=4:
        win=True
        p1win=True
    elif p2tokens>=4:
        win=True
        p2win=True
        

def horizWin(self,grid):
    win=False
    p1win=False
    p2win=False
    p1tokens=0
    p2tokens=0
    i=0
    for column in grid:
        if column[i]==1:
            p1tokens+=1
        elif column[i]==2:
            p1token=0
            p2tokens+=1
        elif column[i]==0:
            p1tokens=0
            p2tokens=0
        i+=1
        
    if p1tokens>=4:
        win=True
        p1win=True
    elif p2tokens>=4:
        win=True
        p2win=True

def diagWin1(self,grid):
    win=False
    p1win=False
    p2win=False
    p1tokens=0
    p2tokens=0
    i=0
    column=0
    for column in grid:
        if column[i]==1:
            p1tokens+=1
        elif column[i]==2:
            p1token=0
            p2tokens+=1
        elif column[i]==0:
            p1tokens=0
            p2tokens=0
        column+=1
        i+=1
        
    if p1tokens>=4:
        win=True
        p1win=True
    elif p2tokens>=4:
        win=True
        p2win=True 

def diagWin2(self,grid):
   win=False
    p1win=False
    p2win=False
    p1tokens=0
    p2tokens=0
    i=0
    for column in reversed(grid):
        if column[i]==1:
            p1tokens+=1
        elif column[i]==2:
            p1token=0
            p2tokens+=1
        elif column[i]==0:
            p1tokens=0
            p2tokens=0
        i+=1

    if p1tokens>=4:
        win=True
        p1win=True
    elif p2tokens>=4:
        win=True
        p2win=True 
    
    






    




    
    

    

        



       