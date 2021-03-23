import numpy as np
from PIL import ImageGrab
import matplotlib.pyplot as plt
from pynput.mouse import Button, Controller, Listener


class Pianotiles():
    
    def __init__(self):

        self.INIT_COLOR = "[ 54 159 198]" #The colour of the initial TILE
        self.TILE_COLOR = "[0 0 0]" #The colour of the game TILES
        self.BORDER_COLOR = "[  2 130 197]" #Colour of the borders 

        #minX, minY, maxX, maxY = (640,0,1280,820)
        self.minX, self.minY, self.maxX, self.maxY = (640,800,1280,801)

        self.width = self.maxX - self.minX #Width of the game
        self.height = self.maxY - self.minY #Height of the game

        self.columns = 4 #Number of columns in the game
        self.column_width = self.width/self.columns #Width of a single column

        self.game_coords = (self.minX,self.minY,self.maxX,self.maxY) # Coords of the screen where the game is displayed

        self.mouse = Controller()

        self.cutWidth = 1 # Decides the width of each column
        if(self.stillInGame()):
            self.StartGame(self.INIT_COLOR, -20) #Clicks the START tile
            while(self.stillInGame()):
                self.StartGame(self.TILE_COLOR, 100) 

    def newImage(self): #Makes a screenshot to analyze the colours
        image = np.array(ImageGrab.grab(self.game_coords))
        newImg = []
        
        for x in range(self.columns):
            initX = int(self.column_width * x + self.column_width / 2 - self.cutWidth / 2)
            endX = int(self.column_width * x + self.column_width / 2 + self.cutWidth / 2)
            newImg.append(image[:, initX:endX])
        return newImg


    def StartGame(self, tile_color, y_adjust):
        newImg = self.newImage()

        #SEARCH FOR INIT TILE
        for i in range(len(newImg)):
            desired = False #Defines if the desired TILE has been found

            for y in range(len(newImg[i])): #DETECTS TILES AND CLICKS THEM

                for x in range(len(newImg[i][y])):
                    print(newImg[i][y][x])
                    
                    if(str(newImg[i][y][x]) == tile_color):
                        x_ = self.minX + self.column_width/2 + (i * self.column_width) #It's the center of the tile
                        self.mouse.position = (x_,self.minY+y_adjust) #Moves the mouse to the tile
                        self.mouse.click(Button.left, 1) #Clicks the tile
                        #print("TILE found on ({},{})".format(x_ ,y))
                        desired = True
                        break

                if desired:
                    break
    def stillInGame(self): 
        img = np.array(ImageGrab.grab((623,0,1300,1)))
        firstPixel = str(img[0][0])
        lastPixel = str(img[-1][-1])
        print(firstPixel)
        if (firstPixel == self.BORDER_COLOR and lastPixel == self.BORDER_COLOR ):
            return True
        else:
            return False


if __name__ == '__main__':
	Pianotiles()