import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

class Nastaveni:
    def __init__(self, root):
        #setting title
        w = tk.Toplevel()
        w.title("Settings")
        w.configure(background='#4d4d4d')
        w.iconbitmap('icon_afterburn.ico')
        #setting window size
        width=300
        height=430
        screenwidth = w.winfo_screenwidth()
        screenheight = w.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        w.geometry(alignstr)
        w.resizable(width=False, height=False)

        self.seting_label=tk.Label(w)
        ft = tkFont.Font(family='Arial',size=15)
        self.seting_label["font"] = ft
        self.seting_label["fg"] = "White"
        self.seting_label["bg"] = "#4d4d4d"
        self.seting_label["justify"] = "center"
        self.seting_label["text"] = "Settings:"
        
        self.seting_label.place(x=10,y=10,width=80,height=30)

        self.temperature_label=tk.Label(w)
        ft = tkFont.Font(family='Arial',size=8)
        self.temperature_label["font"] = ft
        self.temperature_label["fg"] = "White"
        self.temperature_label["bg"] = "#4d4d4d"
        self.temperature_label["justify"] = "center"
        self.temperature_label["text"] = "Temperature units:"
        self.temperature_label.place(x=20,y=40,width=90,height=30)

        v = tk.IntVar()
        self.stupne_radio=tk.Radiobutton(w,variable=v ,value=1,bd=0)
        ft = tkFont.Font(family='Arial',size=8)
        self.stupne_radio["font"] = ft
        self.stupne_radio["activebackground"] = "#4d4d4d"
        self.stupne_radio["activeforeground"] = "#007ad9"
        self.stupne_radio["fg"] = "White"
        self.stupne_radio["relief"] = "flat"
        self.stupne_radio["bg"] = "#4d4d4d"
        self.stupne_radio["justify"] = "center"
        self.stupne_radio["text"] = " °C"
        self.stupne_radio["selectcolor"] = "#4d4d4d"
        self.stupne_radio["offrelief"]="flat"
        self.stupne_radio.place(x=25,y=60,width=42,height=30)
        self.stupne_radio.select()
        

        self.far_radio=tk.Radiobutton(w,variable=v,value=2)
        ft = tkFont.Font(family='Arial',size=8)
        self.far_radio["font"] = ft
        self.far_radio["activebackground"] = "#4d4d4d"
        self.far_radio["activeforeground"] = "#007ad9"
        self.far_radio["fg"] = "White"
        self.far_radio["relief"] = "flat"
        self.far_radio["bg"] = "#4d4d4d"
        self.far_radio["justify"] = "center"
        self.far_radio["text"] = " F"
        self.far_radio["selectcolor"] = "#4d4d4d"
        self.far_radio.place(x=75,y=60,width=39,height=30)

        exp = tk.BooleanVar() 
        exp.set(True)
        self.hardware_control_check=tk.Checkbutton(w,variable=exp, onvalue = 1, offvalue = 0)
        ft = tkFont.Font(family='Arial',size=8)
        self.hardware_control_check["font"] = ft
        self.hardware_control_check["fg"] = "White"
        self.hardware_control_check["bg"] = "#4d4d4d"
        self.hardware_control_check["activebackground"] = "#4d4d4d"
        self.hardware_control_check["activeforeground"] = "#007ad9"
        self.hardware_control_check["justify"] = "center"
        self.hardware_control_check["relief"] = "flat"
        self.hardware_control_check["text"] = "Enable hardware control and monitoring"
        self.hardware_control_check.place(x=15,y=90,width=220,height=30)
        self.hardware_control_check["selectcolor"] = "#4d4d4d"
        self.hardware_control_check.select()
        

        self.reched_limit_text=tk.Checkbutton(w)
        ft = tkFont.Font(family='Arial',size=8)
        self.reched_limit_text["font"] = ft 
        self.reched_limit_text["fg"] = "White"
        self.reched_limit_text["bg"] = "#4d4d4d"
        self.reched_limit_text["relief"] = "flat"
        self.reched_limit_text["activebackground"] = "#4d4d4d"
        self.reched_limit_text["justify"] = "center"
        self.reched_limit_text["text"] = "Restore setting when some of limit is reached"
        self.reched_limit_text.place(x=9,y=115,width=260,height=30)
        self.reched_limit_text["offvalue"] = "0"
        self.reched_limit_text["onvalue"] = "1"
        self.reched_limit_text["selectcolor"] = "#4d4d4d"
        self.reched_limit_text["activeforeground"] = "#007ad9"

        self.IO_driver_check=tk.Checkbutton(w)
        ft = tkFont.Font(family='Arial',size=8)
        self.IO_driver_check["font"] = ft
        self.IO_driver_check["fg"] = "White"
        self.IO_driver_check["bg"] = "#4d4d4d"
        self.IO_driver_check["activebackground"] = "#4d4d4d"
        self.IO_driver_check["justify"] = "center"
        self.IO_driver_check["text"] = "Enable low-level IO Driver"
        self.IO_driver_check.place(x=16,y=140,width=150,height=30)
        self.IO_driver_check["offvalue"] = "0"
        self.IO_driver_check["onvalue"] = "1"
        self.IO_driver_check["selectcolor"] = "#4d4d4d"
        self.IO_driver_check["activeforeground"] = "#007ad9"


        self.force_voltage_check=tk.Checkbutton(w)
        ft = tkFont.Font(family='Arial',size=8)
        self.force_voltage_check["font"] = ft
        self.force_voltage_check["fg"] = "White"
        self.force_voltage_check["bg"] = "#4d4d4d"
        self.force_voltage_check["activebackground"] = "#4d4d4d"
        self.force_voltage_check["justify"] = "center"
        self.force_voltage_check["text"] = "Force constant voltage"
        self.force_voltage_check.place(x=17,y=165,width=135,height=30)
        self.force_voltage_check["offvalue"] = "0"
        self.force_voltage_check["onvalue"] = "1"
        self.force_voltage_check["selectcolor"] = "#4d4d4d"
        self.force_voltage_check["activeforeground"] = "#007ad9"
        self.force_voltage_check.select()


        self.system_time_check=tk.Checkbutton(w)
        ft = tkFont.Font(family='Arial',size=8)
        self.system_time_check["font"] = ft
        self.system_time_check["fg"] = "White"
        self.system_time_check["bg"] = "#4d4d4d"
        self.system_time_check["activebackground"] = "#4d4d4d"
        self.system_time_check["activeforeground"] = "#007ad9"
        self.system_time_check["justify"] = "center"
        self.system_time_check["text"] = "Show System time"
        self.system_time_check["selectcolor"] = "#4d4d4d"
        self.system_time_check.place(x=20,y=220,width=110,height=30)
        self.system_time_check.select()

        self.twelhe_h_check=tk.Checkbutton(w)
        ft = tkFont.Font(family='Arial',size=8)
        self.twelhe_h_check["font"] = ft
        self.twelhe_h_check["fg"] = "White"
        self.twelhe_h_check["bg"] = "#4d4d4d"
        self.twelhe_h_check["activeforeground"] = "#007ad9"
        self.twelhe_h_check["activebackground"] = "#4d4d4d"
        self.twelhe_h_check["justify"] = "center"
        self.twelhe_h_check["text"] = "12 hours time format"
        self.twelhe_h_check["selectcolor"] = "#4d4d4d"
        self.twelhe_h_check.place(x=12,y=245,width=135,height=30)

        self.language_label=tk.Label(w)
        ft = tkFont.Font(family='Arial',size=8)
        self.language_label["font"] = ft
        self.language_label["fg"] = "White"
        self.language_label["bg"] = "#4d4d4d"
        self.language_label["justify"] = "center"
        self.language_label["text"] = "Language:"
        self.language_label.place(x=20,y=270,width=50,height=30)

        
        self.beta_check=tk.Checkbutton(w)
        ft = tkFont.Font(family='Arial',size=8)
        self.beta_check["font"] = ft
        self.beta_check["fg"] = "White"
        self.beta_check["bg"] = "#4d4d4d"
        self.beta_check["activebackground"] = "#4d4d4d"
        self.beta_check["activeforeground"] = "#007ad9"
        self.beta_check["justify"] = "center"
        self.beta_check["text"] = "Check for available betas"
        self.beta_check.place(x=16,y=320,width=150,height=30)
        self.beta_check["offvalue"] = "0"
        self.beta_check["onvalue"] = "1"
        self.beta_check["selectcolor"] = "#4d4d4d"


        self.start_windows_check=tk.Checkbutton(w)
        ft = tkFont.Font(family='Arial',size=8)
        self.start_windows_check["font"] = ft
        self.start_windows_check["bg"] = "#4d4d4d"
        self.start_windows_check["activebackground"] = "#4d4d4d"
        self.start_windows_check["activeforeground"] = "#007ad9"
        self.start_windows_check["fg"] = "White"
        self.start_windows_check["justify"] = "center"
        self.start_windows_check["text"] = " Start with Windows"
        self.start_windows_check["selectcolor"] = "#4d4d4d"
        self.start_windows_check.place(x=19,y=345,width=120,height=39)
        

        
#####################################################################dolni buttony
        self.settings_save_btn=tk.Button(w)
        self.settings_save_btn["bg"] = "#007ad9"
        self.settings_save_btn["activebackground"] = "White"
        self.settings_save_btn["activeforeground"] = "#007ad9"
        self.settings_save_btn["bd"] = 1
        self.settings_save_btn["relief"] = "flat"
        ft = tkFont.Font(family='Arial',size=8)
        self.settings_save_btn["font"] = ft
        self.settings_save_btn["fg"] = "White"
        self.settings_save_btn["justify"] = "center"
        self.settings_save_btn["text"] = "Ok"
        self.settings_save_btn.place(x=130,y=390,width=70,height=25)
        self.settings_save_btn["command"] = w.destroy

        self.settings_cancel_btn=tk.Button(w)
        self.settings_cancel_btn["bg"] = "#007ad9"
        self.settings_cancel_btn["activebackground"] = "White"
        self.settings_cancel_btn["activeforeground"] = "#007ad9"
        ft = tkFont.Font(family='Arial',size=8)
        self.settings_cancel_btn["font"] = ft
        self.settings_cancel_btn["bd"] = 1
        self.settings_cancel_btn["relief"] = "flat"
        self.settings_cancel_btn["fg"] = "White"
        self.settings_cancel_btn["justify"] = "center"
        self.settings_cancel_btn["text"] = "Cancel"
        self.settings_cancel_btn.place(x=210,y=390,width=70,height=25)
        self.settings_cancel_btn["command"] = w.destroy



        promenna = tk.StringVar()
        style = ttk.Style()
        style.configure('TMenubutton', background="#007ad9",foreground="White")
        promenna.set(u"Vyber graf") # standardní hodnota
        w = ttk.OptionMenu(w, promenna, u"English",u"Czech", u"English", u"Polski")
        w.place(x=20,y=295,width=120,height=25)
        
        root.mainloop()

