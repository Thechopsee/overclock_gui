import tkinter as tk
import tkinter.font as tkFont
from menu_2_gpu import GPU_menu
from menu_1_cpu import CPU_menu
from menu_3_fan import Fan

class Menu:
    def __init__(self, root):
        


        self.root=root
        
        self.cpu_menu=tk.Button(root)
        self.cpu_menu["bg"] = "#007ad9"
        self.cpu_menu["activebackground"] = "White"
        self.cpu_menu["activeforeground"] = "#007ad9"
        #self.cpu_menu["image"] = CPU_button
        ft = tkFont.Font(family='Arial',size=15,weight="bold")
        self.cpu_menu["font"] = ft
        self.cpu_menu["bd"] = 1
        self.cpu_menu["relief"] = "flat"
        self.cpu_menu["fg"] = "White"
        self.cpu_menu["justify"] = "center"
        self.cpu_menu["text"] = "CPU"
        self.cpu_menu.place(relx=0.143,rely=0.02,relwidth=0.1416,relheight=0.14)
        self.cpu_menu["command"] = self.cpu_menu_command

        self.gpu_menu=tk.Button(root)
        self.gpu_menu["bg"] = "#007ad9"
        self.gpu_menu["activebackground"] = "White"
        self.gpu_menu["activeforeground"] = "#007ad9"
        self.gpu_menu["bd"] = 1
        ft = tkFont.Font(family='Arial',size=15,weight="bold")
        self.gpu_menu["font"] = ft
        self.gpu_menu["relief"] = "flat"
        self.gpu_menu["fg"] = "White"
        self.gpu_menu["justify"] = "center"
        self.gpu_menu["text"] = "GPU"
        self.gpu_menu.place(relx=0.4283,rely=0.02,relwidth=0.1416,relheight=0.14)
        self.gpu_menu["command"] = self.gpu_menu_command

        self.fans_menu=tk.Button(root)
        self.fans_menu["bg"] = "#007ad9"
        self.fans_menu["activebackground"] = "White"
        self.fans_menu["activeforeground"] = "#007ad9"
        self.fans_menu["bd"] = 1
        self.fans_menu["relief"] = "flat"
        ft = tkFont.Font(family='Arial',size=15,weight="bold")
        self.fans_menu["font"] = ft
        self.fans_menu["fg"] = "White"
        self.fans_menu["justify"] = "center"
        self.fans_menu["text"] = "FAN"
        self.fans_menu.place(relx=0.713,rely=0.02,relwidth=0.1416,relheight=0.14)
        self.fans_menu["command"] = self.fans_menu_command

    def cpu_menu_command(self):
        self.destroy()
        self.__init__(self.root)
        abc=CPU_menu(self.root)

    def gpu_menu_command(self):
        self.destroy()
        self.__init__(self.root)
        abc=GPU_menu(self.root)

    def fans_menu_command(self):
        self.destroy()
        self.__init__(self.root)
        abc=Fan(self.root)

    def destroy(self):
        for ele in self.root.winfo_children():
            ele.destroy()
        
        
