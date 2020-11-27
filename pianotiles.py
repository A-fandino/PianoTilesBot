import numpy as np
from PIL import ImageGrab
import matplotlib.pyplot as plt
from pynput.mouse import Button, Controller, Listener


class Pianotiles():
    
    def __init__(self):

        self.INIT_COLOR = "[ 54 159 198]" #The colour of the initial TILE
        self.TILE_COLOR = "[0 0 0]" #The colour of the game TILES

        #minX, minY, maxX, maxY = (640,0,1280,820)
        self.minX, self.minY, self.maxX, self.maxY = (640,800,1280,801)

        self.width = self.maxX - self.minX #Width of the game
        self.height = self.maxY - self.minY #Height of the game

        self.columns = 4 #Number of columns in the game
        self.column_width = self.width/self.columns #Width of a single column

        self.game_coords = (self.minX,self.minY,self.maxX,self.maxY) # Coords of the screen where the game is displayed

        self.mouse = Controller()

        self.cutWidth = 1 # Decides the width of each column
        self.stillInGame();
        #self.StartGame(self.INIT_COLOR, -20) #Clicks the START tile
        #while(True):
        #    self.StartGame(self.TILE_COLOR, 100) 

    def newImage(self): #Makes a screenshot to analyze the colours
        image = np.array(ImageGrab.grab(self.game_coords))
        newImg = []

        for x in range(self.columns):
            initX = int(self.column_width * x + self.column_width / 2 - self.cutWidth / 2)
            endX = int(self.column_width * x + self.column_width / 2 + self.cutWidth / 2)
            #print(initX, endX)
            newImg.append(image[:, initX:endX])
        return newImg


    #Image to array
    #image = np.array(ImageGrab.grab(game_coords))

    #Automatize column cutting


    def StartGame(self, tile_color, y_adjust):
        newImg = self.newImage()

        #SEARCH FOR INIT TILE
        for i in range(len(newImg)):
            desired = False #Defines if the desired TILE it's been found

            for y in range(len(newImg[i])): #DETECTS TILES AND CLICKS THEM

                for x in range(len(newImg[i][y])):
                    print(newImg[i][y][x])
                    
                    if(str(newImg[i][y][x]) == tile_color):
                        x_ = self.minX + self.column_width/2 + (i * self.column_width) #It's the center of the tile
                        self.mouse.position = (x_,self.minY+y_adjust) #Moves the mouse to the tile
                        self.mouse.click(Button.left, 1) #Click the tile, duh
                        #print("TILE found on ({},{})".format(x_ ,y))
                        desired = True
                        break;

                if desired:
                    break;
    def stillInGame(self): # Lateral colour #0282C5
        newImg = self.newImage()
        """print(newImg[2])
        if (str(newImg[2]) == "[[[ 39 146 187]]]" ):
            print("AY LMAO")
            return True;
        else:
            print("AYMAN")
            return False;"""
        canvas=plt.figure(figsize=(8, 8))
        #NECESITAS COGER EL COLOR DE LOS LATERALES!!!
        plt.grid(True)
        plt.gray()
        plt.axis('off')
        for x in range(1,self.columns+1):
            canvas.add_subplot(1, self.columns, x)
            plt.imshow(newImg[x-1])

        plt.show()
Pianotiles();

#Display Image (JUST FOR TESTING)

"""
canvas=plt.figure(figsize=(8, 8))

plt.grid(True)
plt.gray()
plt.axis('off')
for x in range(1,columns+1):
    canvas.add_subplot(1, columns, x)
    plt.imshow(newImg[x-1])

plt.show()

def mouseClick(i,y):
    pass"""