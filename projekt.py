import tkinter as tk
import tkinter.font as tkFont
from PIL import Image,ImageTk
from menu_projekt import Menu

from menu_1_cpu import CPU_menu
from tkinter import ttk
import math as math
 

class App:
    def __init__(self, root):
        root.title("Afterburn-remix")
        root.iconbitmap('icon_afterburn.ico')
        root.configure(background='#4d4d4d')
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        
        self.menu=Menu(root)
        self.cpu = CPU_menu(root)
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
