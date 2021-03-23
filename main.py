from bot import Pianotiles
import tkinter as tk
from tkinter import ttk

class App():
    def __init__(self):
        self.windowSetup()
    
    def windowSetup(self):
        self.root = tk.Tk()
        self.root.title("Bot controler")
        #Header text
        self.header = tk.Label(self.root,text = "Hello World")
        self.header.grid(column = 0, row = 0)
        #Start button
        self.startBtn = ttk.Button(self.root, text = "Start!", command=self.startBot)
        self.startBtn.grid(column = 0, row = 1)
        #self.root.resizable(0,0)
        self.root.mainloop()
    def startBot(self):
        Pianotiles()

App()