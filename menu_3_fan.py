import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from projekt_nastaveni import Nastaveni
from PIL import Image,ImageTk

class Fan:
    def __init__(self, root):
        root.title("Afterburn-remix")
        root.configure(background='#4d4d4d')
        width=600
        height=500
        self.root=root
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
###################################Setting button######################################
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

        self.width_kontrol=40
        def _resize_text(event):
            
            new_width = event.width

            basic=round((new_width/self.width_kontrol)*8)

           

            self.ft = tkFont.Font(family='Arial',size=basic)
            self.chprofile_label.config(font=self.ft)
            self.fan_graph_label.config(font=self.ft)
            self.fan_speed_label.config(font=self.ft)
            self.new_fan_speed_label.config(font=self.ft)
            self.old_fan_speed_label.config(font=self.ft)


            
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
        self.potvrzeni.place(relx=0.55,rely=0.89,relwidth=0.0666,relheight=0.05)
        self.potvrzeni["command"] = self.potvrzeni_command
        self.potvrzeni.bind('<Configure>', _resize_text)

        self.smazani=tk.Button(root)
        self.smazani["bg"] = "#007ad9"
        self.smazani["bd"] = 1
        self.smazani["relief"] = "flat"
        ft = tkFont.Font(family='Arial',size=10)
        self.smazani["font"] = ft
        self.smazani["fg"] = "White"
        self.smazani["justify"] = "center"
        self.smazani["text"] = "X"
        self.smazani.place(relx=0.6166,rely=0.89,relwidth=0.0666,relheight=0.05)
        self.smazani["command"] = self.smazani_command
##############################################################################################


########################################profile_picker######################################
        
        self.jedna_profile=tk.Button()
        self.jedna_profile["bg"] = "#007ad9"
        ft = tkFont.Font(family='Arial',size=8)
        self.jedna_profile["font"] = ft
        self.jedna_profile["fg"] = "White"
        self.jedna_profile["justify"] = "center"
        self.jedna_profile["text"] = "1"
        self.jedna_profile["bd"] = 1
        self.jedna_profile["relief"] = "flat"
        self.jedna_profile.place(relx=0.7333,rely=0.9,relwidth=0.033,relheight=0.04)
        self.jedna_profile["command"] = self.jedna_profile_command

        self.dva_profile=tk.Button(root)
        self.dva_profile["bg"] = "#007ad9"
        ft = tkFont.Font(family='Arial',size=8)
        self.dva_profile["font"] = ft
        self.dva_profile["fg"] = "White"
        self.dva_profile["justify"] = "center"
        self.dva_profile["text"] = "2"
        self.dva_profile["bd"] = 1
        self.dva_profile["relief"] = "flat"
        self.dva_profile.place(relx=0.76666,rely=0.9,relwidth=0.033,relheight=0.04)
        self.dva_profile["command"] = self.dva_profile_command

        self.tri_profile=tk.Button(root)
        self.tri_profile["bg"] = "#007ad9"
        ft = tkFont.Font(family='Arial',size=8)
        self.tri_profile["font"] = ft
        self.tri_profile["fg"] = "White"
        self.tri_profile["justify"] = "center"
        self.tri_profile["text"] = "3"
        self.tri_profile["bd"] = 1
        self.tri_profile["relief"] = "flat"
        self.tri_profile.place(relx=0.8,rely=0.9,relwidth=0.033,relheight=0.04)
        self.tri_profile["command"] = self.tri_profile_command

        self.ctyri_profile=tk.Button(root)
        self.ctyri_profile["bg"] = "#007ad9"
        ft = tkFont.Font(family='Arial',size=8)
        self.ctyri_profile["font"] = ft
        self.ctyri_profile["fg"] = "White"
        self.ctyri_profile["justify"] = "center"
        self.ctyri_profile["text"] = "4"
        self.ctyri_profile["bd"] = 1
        self.ctyri_profile["relief"] = "flat"
        self.ctyri_profile.place(relx=0.833,rely=0.9,relwidth=0.033,relheight=0.04)
        self.ctyri_profile["command"] = self.ctyri_profile_command

        self.pet_profile=tk.Button(root)
        self.pet_profile["bg"] = "#007ad9"
        ft = tkFont.Font(family='Arial',size=8)
        self.pet_profile["font"] = ft
        self.pet_profile["fg"] = "White"
        self.pet_profile["justify"] = "center"
        self.pet_profile["text"] = "5"
        self.pet_profile["bd"] = 1
        self.pet_profile["relief"] = "flat"
        self.pet_profile.place(relx=0.866,rely=0.9,relwidth=0.033,relheight=0.04)
        self.pet_profile["command"] = self.pet_profile_command

        self.sest_profile=tk.Button(root)
        self.sest_profile["bg"] = "#007ad9"
        ft = tkFont.Font(family='Arial',size=8)
        self.sest_profile["font"] = ft
        self.sest_profile["fg"] = "White"
        self.sest_profile["justify"] = "center"
        self.sest_profile["text"] = "6"
        self.sest_profile["bd"] = 1
        self.sest_profile["relief"] = "flat"
        self.sest_profile.place(relx=0.899,rely=0.9,relwidth=0.033,relheight=0.04)
        self.sest_profile["command"] = self.sest_profile_command

        self.chprofile_label=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=8)
        self.chprofile_label["font"] = ft
        self.chprofile_label["bg"] = "#4d4d4d"
        self.chprofile_label["fg"] = "White"
        self.chprofile_label["text"] = "Choose profile:"
        self.chprofile_label.place(relx=0.73333,rely=0.85,relwidth=0.15,relheight=0.05)
##################################################################################################



        



#########################################Graph##################################################
        fig = plt.Figure()
        fig.patch.set_facecolor('#4d4d4d')
        fig.patch.set_edgecolor("White")

        self.x = np.arange(0, 2*np.pi, 0.01)        # x-array

        def animate(i):
            line.set_ydata(np.sin(self.x+i/30.0))  # update the data
            return line,

        
        
        self.canvas_g = FigureCanvasTkAgg(fig, master=root)
        self.canvas_g.get_tk_widget().place(relx=0.4583333, rely=0.226,relwidth=0.5 ,relheight=0.6)

        ax = fig.add_subplot(111)
        ax.set_facecolor('#007ad9')
        line, = ax.plot(self.x, np.sin(self.x),color="white")
        ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), interval=25, blit=False)
        

################################################################################################
        self.fan_graph_label=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=8)
        self.fan_graph_label["font"] = ft
        self.fan_graph_label["bg"] = "#4d4d4d"
        self.fan_graph_label["fg"] = "White"
        self.fan_graph_label["justify"] = "center"
        self.fan_graph_label["text"] = "Fan speed Graph:"
        self.fan_graph_label.place(relx=0.45,rely=0.234,relwidth=0.1666,relheight=0.05)
#################################slidery##########################################
        def get_fan_speed(abc):
            self.new_fan_speed_label.config(text="New :"+str(self.input_fan_speed.get()))


        self.input_fan_speed=tk.IntVar()
        self.input_fan_speed.set(80)
        self.input_fan_speed_old=tk.IntVar()
        self.input_fan_speed_old.set(80)

        
        s = ttk.Style()
        s.configure('Horizontal.TScale', background='#4d4d4d')
        
        fan_speed = ttk.Scale(root, from_=0, to=100,orient="horizontal",variable=self.input_fan_speed,value=1,command=get_fan_speed)
        fan_speed.place(relx=0.01666,rely=0.76,relwidth=0.38333)

        



       
################
        self.fan_speed_label=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=8)
        self.fan_speed_label["font"] = ft
        self.fan_speed_label["bg"] = "#4d4d4d"
        self.fan_speed_label["fg"] = "White"
        self.fan_speed_label["justify"] = "center"
        self.fan_speed_label["text"] = "Max speed (%):"
        self.fan_speed_label.place(relx=0.011,rely=0.71,relwidth=0.13333,relheight=0.05)

        

        self.new_fan_speed_label=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=8)
        self.new_fan_speed_label["font"] = ft
        self.new_fan_speed_label["bg"] = "#4d4d4d"
        self.new_fan_speed_label["fg"] = "White"
        self.new_fan_speed_label["justify"] = "center"
        self.new_fan_speed_label["text"] = "New: "+str(self.input_fan_speed.get())
        self.new_fan_speed_label.place(relx=0,rely=0.82,relwidth=0.13333,relheight=0.05)

        self.old_fan_speed_label=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=8)
        self.old_fan_speed_label["font"] = ft
        self.old_fan_speed_label["bg"] = "#4d4d4d"
        self.old_fan_speed_label["fg"] = "White"
        self.old_fan_speed_label["justify"] = "center"
        self.old_fan_speed_label["text"] = "Old: "+str(self.input_fan_speed_old.get())
        self.old_fan_speed_label.place(relx=0.13333,rely=0.82,relwidth=0.13333,relheight=0.05)




###############################################################################################

#################################################self.canvas#########################################


        self.new_dot=tk.Button(root)
        self.new_dot["bg"] = "#007ad9"
        self.new_dot["bd"] = 1
        self.new_dot["relief"] = "flat"
        ft = tkFont.Font(family='Arial',size=10)
        self.new_dot["font"] = ft
        self.new_dot["fg"] = "White"
        self.new_dot["justify"] = "center"
        self.new_dot["text"] = "New dot"
        self.new_dot.place(relx=0.0666,rely=0.22,relwidth=0.1333,relheight=0.05)


        self.delete_latest=tk.Button(root)
        self.delete_latest["bg"] = "#007ad9"
        self.delete_latest["bd"] = 1
        self.delete_latest["relief"] = "flat"
        ft = tkFont.Font(family='Arial',size=10)
        self.delete_latest["font"] = ft
        self.delete_latest["fg"] = "White"
        self.delete_latest["justify"] = "center"
        self.delete_latest["text"] = "Delete latest"
        self.delete_latest.place(relx=0.208,rely=0.22,relwidth=0.1333,relheight=0.05)


        self.width=230
        self.height=200
        def on_resize(event):
            # determine the ratio of old width/height to new width/height
            wscale = float(event.width)/self.width
            hscale = float(event.height)/self.height
            self.width = event.width
            self.height = event.height
            # resize the self.canvas 
            self.canvas.config(width=self.width, height=self.height)
            # rescale all the objects tagged with the "all" tag
            self.canvas.scale("all",0,0,wscale,hscale)

        self.canvas = tk.Canvas(root)
        self.canvas.bind("<Configure>", on_resize)
        self.canvas.create_rectangle(0,0, 230, 200,fill="#4d4d4d")
        self.canvas.create_line(0, 200, 50, 150,fill="White")
        self.canvas.create_line(50, 150, 80, 150,fill="White")
        self.canvas.create_line(80, 150,120,100,fill="White")
        self.canvas.create_line(120,100,230,100,fill="White")
        
        self.canvas.create_oval(46,146,54,154,fill="#007ad9")
        self.canvas.create_oval(76,146,84,154,fill="#007ad9")
        self.canvas.create_oval(116,96,124,104,fill="#007ad9")
        
        
       

        self.canvas.place(relx=0.01666,rely=0.3,relwidth=0.3833,relheight=0.4)



        root.mainloop()
 #########################################################################################
    def potvrzeni_command(self):
        self.input_fan_speed_old.set(self.input_fan_speed.get())
        self.old_fan_speed_label["text"]="Old: "+str(self.input_fan_speed.get())



    def smazani_command(self):
        print("command")


    def jedna_profile_command(self):
        print("command")


    def dva_profile_command(self):
        print("command")


    def tri_profile_command(self):
        print("command")


    def ctyri_profile_command(self):
        print("command")


    def pet_profile_command(self):
        print("command")


    def sest_profile_command(self):
        print("command")

    def go_to_settings(self):
        abc=Nastaveni(self.root)


