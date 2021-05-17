import tkinter as tk
import tkinter.font as tkFont
from PIL import Image,ImageTk
from tkinter import ttk
import math as math
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.animation as animation


from projekt_chose_profile import Profile_picker
from projekt_nastaveni import Nastaveni

class GPU_menu:
    def __init__(self, root):
        Profile_picker(root)
        root.title("Afterburn-remix")
        root.configure(background='#4d4d4d')
        self.root=root
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        


############################################Výběr grafu#########################################

        promenna = tk.StringVar()
        promenna.set(u"Vyber graf") # standardní hodnota
        w = ttk.OptionMenu(root, promenna, u"GPU Usage",u"GPU Usage", u"GPU temperature", u"GPU clocks")
        w.place(relx=0.016,rely=0.75,relwidth=0.216,relheight=0.05)

##########################################Setting button#########################################
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
        fig2 = plt.Figure()
        fig.patch.set_facecolor('#4d4d4d')
        fig2.patch.set_facecolor('#4d4d4d')

        x = np.arange(0, 2*np.pi, 0.01)        # x-array

        def animate(i):
            line.set_ydata(np.sin(x+i/10.0))  # update the data
            return line,
        def animate2(i):
            line2.set_ydata(np.sin(x+i/10.0))  # update the data
            return line2,


        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.get_tk_widget().place(relx=0, rely=0.82,relwidth=0.9333,relheight=0.14)

        ax = fig.add_subplot(111)
        ax.set_facecolor('#007ad9')
        line, = ax.plot(x, np.sin(x),color='White')
        ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), interval=25, blit=False)

        canvas2 = FigureCanvasTkAgg(fig2, master=root)
        canvas2.get_tk_widget().place(relx=0, rely=0.424,relwidth=0.9333,relheight=0.14)
        ax2 = fig2.add_subplot(111)
        ax2.set_facecolor('#007ad9')
        line2, = ax2.plot(x, np.sin(x),color='White')
        ani2= animation.FuncAnimation(fig2, animate2, np.arange(1, 200), interval=25, blit=False)
        
        
        
################################################################################################

#################################slidery##########################################
        def funkce(abc):
            self.new_gpu_core_clock.config(text="New :"+str(self.gpu_clock.get()))
        def get_power_limit(abc):
            self.new_power_limit.config(text="New :"+str(self.power_limit_input.get()))
        def get_mem_frequency(abc):
            self.new_mem_limit.config(text="New :"+str(self.mem_frequency_limit.get()))

        self.gpu_clock=tk.IntVar()
        self.gpu_clock.set(2600)
        self.power_limit_input=tk.IntVar(0)
        self.power_limit_input.set(0)
        self.mem_frequency_limit=tk.IntVar()
        self.mem_frequency_limit.set(1000)


        self.gpu_clock_old=tk.IntVar()
        self.gpu_clock_old.set(2600)
        self.power_limit_old=tk.IntVar(0)
        self.power_limit_old.set(0)
        self.mem_frequency_limit_old=tk.IntVar()
        self.mem_frequency_limit_old.set(1000)

        gpu_core_clock = ttk.Scale(root, from_=1000, to=3100,orient="horizontal",variable=self.gpu_clock,value=1,command=funkce)
        gpu_core_clock.place(relx=0.01666,rely=0.22,relwidth=0.6666)

        power_limit = ttk.Scale(root, from_=-20, to=20,orient="horizontal",variable=self.power_limit_input,value=1,command=get_power_limit)
        power_limit.place(relx=0.01666,rely=0.32,relwidth=0.6666)
        
        usage_limit= ttk.Scale(root, from_=500, to=1100,orient="horizontal",variable=self.mem_frequency_limit,value=1,command=get_mem_frequency)
        usage_limit.place(relx=0.01666,rely=0.64,relwidth=0.6666)

        

###########


        self.width_kontrol=40
        def _resize_text(event):
            
            new_width = event.width

            basic=round((new_width/self.width_kontrol)*8)

           

            self.ft = tkFont.Font(family='Arial',size=basic)
            self.gpu_clock_label.config(font=self.ft)
            self.new_gpu_core_clock.config(font=self.ft)
            self.old_gpu_core_clock.config(font=self.ft)
            self.power_limit_label.config(font=self.ft)
            self.graph_label.config(font=self.ft)
            self.new_power_limit.config(font=self.ft)
            self.old_power_limitt.config(font=self.ft)
            self.usage_limit_label.config(font=self.ft)
            self.new_mem_limit.config(font=self.ft)
            self.old_usage_limit.config(font=self.ft)
        self.gpu_clock_label=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=8)
        self.gpu_clock_label["font"] = ft
        
        
        self.gpu_clock_label["justify"] = "center"
        self.gpu_clock_label["bg"] = "#4d4d4d"
        self.gpu_clock_label["fg"] = "White"
        self.gpu_clock_label["text"] = "GPU clock (Mhz):"
        self.gpu_clock_label.place(relx=0.015,rely=0.18,relwidth=0.1583,relheight=0.05)

        
        self.new_gpu_core_clock=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=8)
        self.new_gpu_core_clock["font"] = ft
        self.new_gpu_core_clock["text"]="New: "+str(self.gpu_clock.get())
        self.new_gpu_core_clock["bg"] = "#4d4d4d"
        self.new_gpu_core_clock["fg"] = "White"
        self.new_gpu_core_clock.place(relx=0.6833,rely=0.22,relwidth=0.15,relheight=0.05)

        self.old_gpu_core_clock=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=8)
        self.old_gpu_core_clock["font"] = ft
        self.old_gpu_core_clock["text"]="0ld: "+str(self.gpu_clock_old.get())
        self.old_gpu_core_clock["bg"] = "#4d4d4d"
        self.old_gpu_core_clock["fg"] = "White"
        self.old_gpu_core_clock.place(relx=0.8,rely=0.22,relwidth=0.15,relheight=0.05)
############
        self.power_limit_label=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=8)
        self.power_limit_label["font"] = ft
        self.power_limit_label["bg"] = "#4d4d4d"
        self.power_limit_label["fg"] = "White"
        self.power_limit_label["justify"] = "center"
        self.power_limit_label["text"] = "Power limit (%):"
        self.power_limit_label.place(relx=0.015,rely=0.28,relwidth=0.1366,relheight=0.05)

        self.graph_label=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=8)
        self.graph_label["font"] = ft
        self.graph_label["bg"] = "#4d4d4d"
        self.graph_label["fg"] = "White"
        self.graph_label["justify"] = "center"
        self.graph_label["text"] = "Core usage Graph:"
        self.graph_label.place(relx=0.02,rely=0.38,relwidth=0.15,relheight=0.05)

        self.new_power_limit=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=8)
        self.new_power_limit["font"] = ft
        self.new_power_limit["bg"] = "#4d4d4d"
        self.new_power_limit["fg"] = "White"
        self.new_power_limit["text"]="New: "+str(self.power_limit_input.get())
        self.new_power_limit.place(relx=0.68333,rely=0.3,relwidth=0.15,relheight=0.05)

        self.old_power_limitt=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=8)
        self.old_power_limitt["font"] = ft
        self.old_power_limitt["text"]="0ld: "+str(self.power_limit_old.get())
        self.old_power_limitt["bg"] = "#4d4d4d"
        self.old_power_limitt["fg"] = "White"
        self.old_power_limitt.place(relx=0.8,rely=0.3,relwidth=0.15,relheight=0.05)
#########

       
################
        self.usage_limit_label=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=8)
        self.usage_limit_label["font"] = ft
        self.usage_limit_label["bg"] = "#4d4d4d"
        self.usage_limit_label["fg"] = "White"
        self.usage_limit_label["justify"] = "center"
        self.usage_limit_label["text"] = "Memory frequency (Mhz):"
        self.usage_limit_label.place(relx=0,rely=0.6,relwidth=0.25,relheight=0.05)

        self.new_mem_limit=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=8)
        self.new_mem_limit["font"] = ft
        self.new_mem_limit["text"]="New: "+str(self.mem_frequency_limit.get())
        self.new_mem_limit["bg"] = "#4d4d4d"
        self.new_mem_limit["fg"] = "White"
        self.new_mem_limit.place(relx=0.68333,rely=0.64,relwidth=0.15,relheight=0.05)

        self.old_usage_limit=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=8)
        self.old_usage_limit["font"] = ft
        self.old_usage_limit["text"]="0ld: "+str(self.mem_frequency_limit_old.get())
        self.old_usage_limit["bg"] = "#4d4d4d"
        self.old_usage_limit["fg"] = "White"
        self.old_usage_limit.place(relx=0.8,rely=0.64,relwidth=0.15,relheight=0.05)



        


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
        self.smazani.place(relx=0.61666,rely=0.732,relwidth=0.0666,relheight=0.05)
        self.smazani["command"] = self.smazani_command
#####################################################################################


        root.mainloop()

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

    def potvrzeni_command(self):
        self.gpu_clock_old.set(self.gpu_clock.get())
        self.power_limit_old.set(self.power_limit_input.get())
        self.mem_frequency_limit_old.set(self.mem_frequency_limit.get())
        

        self.old_gpu_core_clock["text"]="Old: "+str(self.gpu_clock_old.get())
        self.old_power_limitt["text"]="Old: "+str(self.power_limit_old.get())
        self.old_usage_limit["text"]="Old: "+str(self.mem_frequency_limit_old.get())
       