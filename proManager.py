#!/usr/bin/python3.5
#chmod +x procManager.py
#run with './procManager'
import subprocess
import tkinter as tk
import time
BUTTON_WIDTH = 50
BUTTON_HEIGHT = 5
TEXT_WIDTH = 55
TEXT_HEIGHT = 15

class procManager:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.T = tk.Text(self.frame, 
        height=TEXT_HEIGHT, 
        width=TEXT_WIDTH)
        self.T.pack()
        self.T.insert("end","Ready")

        self.button1 = tk.Button(self.frame,
            text = 'D', 
            width = BUTTON_WIDTH, 
            height = BUTTON_HEIGHT,
            command = self.science)
        self.button1.pack()

        self.button2 = tk.Button(self.frame, 
            text = 'A', 
            width = BUTTON_WIDTH, 
            height = BUTTON_HEIGHT, 
            command = self.extreme)
        self.button2.pack()

        self.button3 = tk.Button(self.frame, 
            text = 'B', 
            width = BUTTON_WIDTH, 
            height = BUTTON_HEIGHT, 
            command = self.servicing)
        self.button3.pack()

        self.button4 = tk.Button(self.frame, 
            text = 'C', 
            width = BUTTON_WIDTH, 
            height = BUTTON_HEIGHT, 
            command = self.auto)
        self.button4.pack()

        self.button5 = tk.Button(self.frame, 
        text = 'Pause All', 
        width = BUTTON_WIDTH, 
        height = BUTTON_HEIGHT, 
        command = self.pauseAll)
        self.button5.pack()

        self.quitButton = tk.Button(self.frame, 
            text = 'Exit', 
            width = BUTTON_WIDTH, 
            height = BUTTON_HEIGHT, 
            command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

    def extreme(self):
        self.T.delete('1.0', "end")
        self.T.insert("end","Starting A...")

    def servicing(self):
        self.T.delete('1.0', "end")
        self.T.insert("end","Starting B...")

    def auto(self):
        self.T.delete('1.0', "end")
        self.T.insert("end","Starting C...")

    def science(self):
        self.T.delete('1.0', "end")
        self.T.insert("end","Starting D...")
    
    def pauseAll(self):
        self.T.delete('1.0', "end")
        self.T.insert("end","Pausing all processes...")
        
    def close_windows(self):
        self.T.delete('1.0', "end")
        self.master.destroy()

def main(): 
    root = tk.Tk()
    root.title("-Process Manager-")
    #root.geometry('1000x1000')
    app = procManager(root)
    root.mainloop()

if __name__ == '__main__':
    main()
