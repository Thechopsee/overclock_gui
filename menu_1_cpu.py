import tkinter as tk
import tkinter.font as tkFont
from PIL import Image,ImageTk
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tkinter import ttk
import math as math

from projekt_nastaveni import Nastaveni
from projekt_chose_profile import Profile_picker


class CPU_menu:
    def __init__(self, root):
        Profile_picker(root)
        self.root=root
############################################Výběr grafu#########################################
        def change_graph(abc):
            
            for item in self.canvas.get_tk_widget().find_all():
                    self.canvas.get_tk_widget().delete(item) 
            if (abc=="CPU temperature"):
                fig = plt.Figure()
                fig.patch.set_facecolor('#4d4d4d')
                fig.set_edgecolor("White")

                self.x = np.arange(0, 2*np.pi, 0.01)        # x-array

                
                def animate(i):
                    line.set_ydata(np.sin(self.x*i/30.0))  # update the data
                    return line,

                

                self.canvas = FigureCanvasTkAgg(fig, master=root)
                self.canvas.get_tk_widget().place(relx=0, rely=0.82,relwidth=0.9333 ,relheight=0.14)

                ax = fig.add_subplot(111)
                ax.set_facecolor('#007ad9')
                line, = ax.plot(self.x, np.sin(self.x),color="white")
                ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), interval=25, blit=False)
                tk.mainloop()
            if (abc=="CPU Usage"):
                fig = plt.Figure()
                fig.patch.set_facecolor('#4d4d4d')
                fig.set_edgecolor("White")
                y=[0,15,9,6,8,7,5,7,8,2]
                def animate2(i):
                    line.set_ydata(np.sin(i/30.0))  # update the data
                    return line,

                

                self.canvas = FigureCanvasTkAgg(fig, master=root)
                self.canvas.get_tk_widget().place(relx=0, rely=0.82,relwidth=0.9333 ,relheight=0.14)

                ax = fig.add_subplot(111)
                ax.set_facecolor("#007ad9")
                line, = ax.plot(y, np.sin(y),color="white")
                ani = animation.FuncAnimation(fig, animate2, np.arange(1, 200), interval=25, blit=False)
                tk.mainloop()   

            
        promenna = tk.StringVar()
        style = ttk.Style()
        style.configure('TMenubutton', background="#007ad9",foreground="White")
        promenna.set(u"Vyber graf") # standardní hodnota
        w = ttk.OptionMenu(root, promenna, u"CPU Usage",u"CPU Usage", u"CPU temperature", u"CPU clocks",command=change_graph)
        
        w.place(relx=0.016,rely=0.75,relwidth=0.216,relheight=0.05)

################################################################################################
        def _resize_image(event):

            new_width = event.width
            new_height = event.height

            self.image = self.img_copy.resize((new_width, new_height))

            self.render = ImageTk.PhotoImage(self.image)
            self.img.configure(image = self.render)

        self.image = Image.open("settings_button.png")
        self.img_copy= self.image.copy()
        self.render = ImageTk.PhotoImage(self.image)
        self.img = tk.Button(image=self.render,bd=0,relief="flat",background="#4d4d4d",command=self.go_to_settings)
        self.img.image = self.render
        self.img.place(relx=0.9, rely=0.88,relwidth=0.1 ,relheight=0.12)
        self.img.bind('<Configure>', _resize_image)
        

        

#########################################Graph##################################################
        
        fig = plt.Figure()
        fig.patch.set_facecolor('#4d4d4d')
        fig.patch.set_edgecolor("White")

       # x = np.arange(0, 2*np.pi, 0.01)        # x-array

        self.x=[0,15,9,6,8,7,5,7,8,2]
        def animate(i):
            line.set_ydata(np.sin(i/30.0))  # update the data
            return line,

        

        self.canvas = FigureCanvasTkAgg(fig, master=root)
        self.canvas.get_tk_widget().place(relx=0, rely=0.82,relwidth=0.9333 ,relheight=0.14)

        ax = fig.add_subplot(111)
        ax.set_facecolor('#007ad9')
        line, = ax.plot(self.x, np.sin(self.x),color="white")
        ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), interval=25, blit=False)
################################################################################################

#################################slidery##########################################
        def funkce(abc):
            self.new_core_clock.config(text="New :"+str(self.inputt.get()))
        def get_power_limit(abc):
            self.new_power_limit.config(text="New :"+str(self.input_power_limit.get()))
        def get_temp_limit(abc):
            self.new_temp_limit.config(text="New :"+str(self.input_temp_limit.get()))
        def get_usage_limit(abc):
            self.new_usage_limit.config(text="New :"+str(self.input_usage_limit.get()))

        self.inputt=tk.IntVar()
        self.inputt.set(3200)
        self.input_power_limit=tk.IntVar(0)
        self.input_power_limit.set(0)
        self.input_temp_limit=tk.IntVar()
        self.input_temp_limit.set(72)
        self.input_usage_limit=tk.IntVar()
        self.input_usage_limit.set(100)

        self.inputt_old=tk.IntVar()
        self.inputt_old.set(3200)
        self.input_power_limit_old=tk.IntVar(0)
        self.input_power_limit_old.set(0)
        self.input_temp_limit_old=tk.IntVar()
        self.input_temp_limit_old.set(72)
        self.input_usage_limit_old=tk.IntVar()
        self.input_usage_limit_old.set(100)

        s = ttk.Style()
        s.configure('Horizontal.TScale', background='#4d4d4d')

        core_clock = ttk.Scale(root, from_=2000, to=4150,orient="horizontal",variable=self.inputt,value=1,command=funkce)
        core_clock.place(relx=0.0166,rely=0.22,relwidth=0.6666)
        power_limit = ttk.Scale(root, from_=-20, to=20,orient="horizontal",variable=self.input_power_limit,value=1,command=get_power_limit)
        power_limit.place(relx=0.0166,rely=0.34,relwidth=0.6666)
        temp_limit = ttk.Scale(root, from_=40, to=110,orient="horizontal",variable=self.input_temp_limit,value=1,command=get_temp_limit)
        temp_limit.place(relx=0.0166,rely=0.46,relwidth=0.6666)
        usage_limit = ttk.Scale(root, from_=0, to=100,orient="horizontal",variable=self.input_usage_limit,value=1,command=get_usage_limit)
        usage_limit.place(relx=0.0166,rely=0.58,relwidth=0.6666)

        

###########
        self.width_kontrol=40
        def _resize_image(event):
            
            new_width = event.width

            basic=round((new_width/self.width_kontrol)*8)

           

            self.ft = tkFont.Font(family='Arial',size=basic)
            self.core_clock_label.config(font=self.ft)
            self.new_core_clock.config(font=self.ft)
            self.old_core_clock.config(font=self.ft)
            self.power_limit_label.config(font=self.ft)
            self.new_power_limit.config(font=self.ft)
            self.old_power_limit.config(font=self.ft)
            self.temp_limit_label.config(font=self.ft)
            self.new_temp_limit.config(font=self.ft)
            self.old_temp_limit.config(font=self.ft)
            self.usage_limit_label.config(font=self.ft)
            self.new_usage_limit.config(font=self.ft)
            self.old_usage_limit.config(font=self.ft)


        self.core_clock_label=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=8)
        self.core_clock_label["font"] = ft
        
        self.core_clock_label["bg"] = "#4d4d4d"
        self.core_clock_label["fg"] = "White"
        self.core_clock_label["justify"] = "center"
        self.core_clock_label["text"] = "Core clock (MHz):"
        self.core_clock_label.place(relx=0.015,rely=0.17,relwidth=0.1583,relheight=0.05)

        
        self.new_core_clock=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=8)
        self.new_core_clock["font"] = ft
        self.new_core_clock["bg"] = "#4d4d4d"
        self.new_core_clock["fg"] = "White"
        self.new_core_clock["justify"] = "left"
        self.new_core_clock["text"]="New: "+str(self.inputt.get())+"\n"
        self.new_core_clock.place(relx=0.69,rely=0.22,relwidth=0.1166,relheight=0.05)

        self.old_core_clock=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=8)
        self.old_core_clock["font"] = ft
        self.old_core_clock["bg"] = "#4d4d4d"
        self.old_core_clock["fg"] = "White"
        self.old_core_clock["justify"] = "left"
        self.old_core_clock["text"]="0ld: "+str(self.inputt_old.get())+"\n"
        self.old_core_clock.place(relx=0.816,rely=0.22,relwidth=0.0833,relheight=0.05)
############
        self.power_limit_label=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=8)
        self.power_limit_label["font"] = ft
        self.power_limit_label["bg"] = "#4d4d4d"
        self.power_limit_label["fg"] = "White"
        self.power_limit_label["justify"] = "center"
        self.power_limit_label["text"] = "Power limit (%):"
        self.power_limit_label.place(relx=0.015,rely=0.29,relwidth=0.1366,relheight=0.05)

        self.new_power_limit=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=8)
        self.new_power_limit["font"] = ft
        self.new_power_limit["bg"] = "#4d4d4d"
        self.new_power_limit["fg"] = "White"
        self.new_power_limit["justify"] = "left"
        self.new_power_limit["text"]="New: "+str(self.input_power_limit.get())+"\n"
        self.new_power_limit.place(relx=0.6833,rely=0.34,relwidth=0.1083,relheight=0.05)

        self.old_power_limit=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=8)
        self.old_power_limit["font"] = ft
        self.old_power_limit["bg"] = "#4d4d4d"
        self.old_power_limit["fg"] = "White"
        self.old_power_limit["justify"] = "left"
        self.old_power_limit["text"]="0ld: "+str(self.input_power_limit_old.get())+"\n"
        self.old_power_limit.place(relx=0.8,rely=0.34,relwidth=0.1166,relheight=0.05)
#########

        self.temp_limit_label=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=8)
        self.temp_limit_label["font"] = ft
        self.temp_limit_label["bg"] = "#4d4d4d"
        self.temp_limit_label["fg"] = "White"
        self.temp_limit_label["justify"] = "center"
        self.temp_limit_label["text"] = "Temp limit (°C):"
        self.temp_limit_label.place(relx=0.0133,rely=0.41,relwidth=0.1333,relheight=0.05)

        self.new_temp_limit=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=8)
        self.new_temp_limit["font"] = ft
        self.new_temp_limit["bg"] = "#4d4d4d"
        self.new_temp_limit["fg"] = "White"
        self.new_temp_limit["justify"] = "left"
        self.new_temp_limit["text"]="New: "+str(self.input_temp_limit.get())+"\n"
        self.new_temp_limit.place(relx=0.6833,rely=0.46,relwidth=0.1083,relheight=0.05)

        self.old_temp_limit=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=8)
        self.old_temp_limit["font"] = ft
        self.old_temp_limit["bg"] = "#4d4d4d"
        self.old_temp_limit["fg"] = "White"
        self.old_temp_limit["justify"] = "left"
        self.old_temp_limit["text"]="0ld: "+str(self.input_temp_limit_old.get())+"\n"
        self.old_temp_limit.place(relx=0.8,rely=0.46,relwidth=0.1083,relheight=0.05)
################
        self.usage_limit_label=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=8)
        self.usage_limit_label["font"] = ft
        self.usage_limit_label["bg"] = "#4d4d4d"
        self.usage_limit_label["fg"] = "White"
        self.usage_limit_label["justify"] = "center"
        self.usage_limit_label["text"] = "Usage Limit (%):"
        self.usage_limit_label.place(relx=0.01666,rely=0.53,relwidth=0.1333,relheight=0.05)

        self.new_usage_limit=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=8)
        self.new_usage_limit["font"] = ft
        self.new_usage_limit["bg"] = "#4d4d4d"
        self.new_usage_limit["fg"] = "White"
        self.new_usage_limit["justify"] = "left"
        self.new_usage_limit["text"]="New: "+str(self.input_usage_limit.get())+"\n"
        self.new_usage_limit.place(relx=0.69,rely=0.58,relwidth=0.1,relheight=0.05)

        self.old_usage_limit=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=8)
        self.old_usage_limit["font"] = ft
        self.old_usage_limit["bg"] = "#4d4d4d"
        self.old_usage_limit["fg"] = "White"
        self.old_power_limit["justify"] = "left"
        self.old_usage_limit["text"]="0ld: "+str(self.input_usage_limit.get())+"\n"
        self.old_usage_limit.place(relx=0.7916,rely=0.58,relwidth=0.1166,relheight=0.05)
        


###############################################################################################
##########################################Potvrzení/smazaní profilu###########################
        self.potvrzeni=tk.Button(root)
        self.potvrzeni["bg"] = "#007ad9"
        self.potvrzeni["bd"] = 1
        self.potvrzeni["relief"] = "flat"
        ft = tkFont.Font(family='Arial',size=10)
        self.potvrzeni["font"] = ft
        self.potvrzeni["fg"] = "White"
        self.potvrzeni["justify"] = "center"
        self.potvrzeni["text"] = "✓"
        self.potvrzeni.place(relx=0.55,rely=0.732,relwidth=0.0666,relheight=0.05)
        self.potvrzeni["command"] = self.potvrzeni_command
        self.potvrzeni.bind('<Configure>', _resize_image)

        self.smazani=tk.Button(root)
        self.smazani["bg"] = "#007ad9"
        self.smazani["bd"] = 1
        self.smazani["relief"] = "flat"
        ft = tkFont.Font(family='Arial',size=10)
        self.smazani["font"] = ft
        self.smazani["fg"] = "White"
        self.smazani["justify"] = "center"
        self.smazani["text"] = "X"
        self.smazani.place(relx=0.61666,rely=0.732,relwidth=0.0666,relheight=0.05)
        self.smazani["command"] = self.smazani_command

        self.refresh_old_new()
        tk.mainloop()

##############################################################################################
    def potvrzeni_command(self):
        self.inputt_old.set(self.inputt.get())
        self.input_power_limit_old.set(self.input_power_limit.get())
        self.input_temp_limit_old.set(self.input_temp_limit.get())

        self.input_usage_limit_old.set(self.input_usage_limit.get())

        self.old_core_clock["text"]="Old: "+str(self.inputt_old.get())
        self.old_power_limit["text"]="Old: "+str(self.input_power_limit_old.get())
        self.old_temp_limit["text"]="Old: "+str(self.input_temp_limit_old.get())
        self.old_usage_limit["text"]="Old: "+str(self.input_usage_limit_old.get())
    def refresh_old_new(self):
        self.new_core_clock["text"]="New: "+str(self.inputt.get())
        self.new_power_limit["text"]="New: "+str(self.input_power_limit.get())
        self.new_temp_limit["text"]="New: "+str(self.input_temp_limit.get())
        self.new_usage_limit["text"]="New: "+str(self.input_usage_limit.get())

        self.old_core_clock["text"]="Old: "+str(self.inputt_old.get())
        self.old_power_limit["text"]="Old: "+str(self.input_power_limit_old.get())
        self.old_temp_limit["text"]="Old: "+str(self.input_temp_limit_old.get())
        self.old_usage_limit["text"]="Old: "+str(self.input_usage_limit_old.get())
    def smazani_command(self):
        print("command")

   
    def go_to_settings(self):
        abc=Nastaveni(self.root)

