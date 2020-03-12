import turtle
from random import randit, shuffle
from time import sleep


grid = []
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

myPen = turtle.Turtle()
myPen.tracer(0)
myPen.speed(0)
myPen.color("#00000")
myPen.hideturtle()
topLeft_x=-150
topLeft_y=150

def text(message,x,y,size):
    FONT = ('Arial', size, 'normal')
    myPen.penup()
    myPen.goto(x,y)
    myPen.write(message,align="left",font=FONT)

def drawGrid(grid):
    intDim=35
    for row in range(0,10):
        if (row%3)==0:
            myPen.pensize(3)
        else:
            myPen.pensize(1)
        myPen.penup()
        myPen.goto(topLeft_x,topLeft_y-row*intDim)
        myPen.pendown()
        myPen.goto(topLeft_x+9*intDim,topLeft_y-row*intDim)
    for col in range(0,10):
        if (col%3)==0:
            myPen.pensize(3)
        else:
            myPen.pensize(1)
        myPen.penup()
        myPen.goto(topLeft_x+col*intDim,topLeft_y)
        myPen.pendown()
        myPen.goto(topLeft_x+col*intDim,topLeft_y-9*intDim)

    for row in range (0,9):
        for col in range (0,9):
            if grid[row][col]!=0:
                text(grid[row][col],topLeft_x+col*intDim+9,topLeft_y-row*intDim-intDim+8+18)


def checkGrid(grid):
    for row in range(0,9):
        for col in range(0,9):
            if grid[row][col]==0:
                return False

return True

def solveGrid(grid):
    global counter
    for i in range(0,81):
        row=i//9
        col=i%9
        if grid [row][col]==0:
            if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
                square=[]
                if row<3:
                    if col<3:
                        square=[grid[i][0:3] for i in range(0,3)]
                    elif col<6:
                        square=[grid[i][3:6] for i in range(0,3)]
                    else:
                        square=[grid[i][6:9] for i in range(0,3)]
                elif row<6:
                    if col<3:
                        square=[grid[i][0:3] for i in range(3,6)]
                    elif col<6:
                        square=[grid[i][3:6] for i in range(3,6)]
                    else:
                        square=[grid[i][6:9] for i in range(3,6)]
                else: