import tkinter as tk
import tkinter.font as tkFont
class Profile_picker:
    def __init__(self,root):



########################################profile_picker######################################
        self.width_kontrol=20
        def _resize_image(event):
            
            new_width = event.width

            basic=round((new_width/self.width_kontrol)*8)

           

            self.ft = tkFont.Font(family='Arial',size=basic)
            self.chprofile_label.config(font=self.ft)

        self.ft = tkFont.Font(family='Arial',size=8)
        self.jedna_profile=tk.Button(root)
        self.jedna_profile["bg"] = "#007ad9"
        self.jedna_profile["bd"] = 1
        self.jedna_profile["relief"] = "flat"
        self.jedna_profile.bind('<Configure>', _resize_image)

        self.jedna_profile["font"] = self.ft
        self.jedna_profile["fg"] = "White"
        self.jedna_profile["justify"] = "center"
        self.jedna_profile["text"] = "1"
        self.jedna_profile.place(relx=0.73333,rely=0.74,relwidth=0.033333,relheight=0.04)
        self.jedna_profile["command"] = self.jedna_profile_command

        self.dva_profile=tk.Button(root)
        self.dva_profile["bg"] = "#007ad9"
        self.dva_profile["bd"] = 1
        self.dva_profile["relief"] = "flat"
        
        self.dva_profile["font"] = self.ft
        self.dva_profile["fg"] = "White"
        self.dva_profile["justify"] = "center"
        self.dva_profile["text"] = "2"
        self.dva_profile.place(relx=0.76666,rely=0.74,relwidth=0.033333,relheight=0.04)
        self.dva_profile["command"] = self.dva_profile_command

        self.tri_profile=tk.Button(root)
        self.tri_profile["bg"] = "#007ad9"
        self.tri_profile["bd"] = 1
        self.tri_profile["relief"] = "flat"
        
        self.tri_profile["font"] = self.ft
        self.tri_profile["fg"] = "White"
        self.tri_profile["justify"] = "center"
        self.tri_profile["text"] = "3"
        self.tri_profile.place(relx=0.8,rely=0.74,relwidth=0.033333,relheight=0.04)
        self.tri_profile["command"] = self.tri_profile_command

        self.ctyri_profile=tk.Button(root)
        self.ctyri_profile["bg"] = "#007ad9"
        self.ctyri_profile["bd"] = 1
        self.ctyri_profile["relief"] = "flat"
        
        self.ctyri_profile["font"] = self.ft
        self.ctyri_profile["fg"] = "White"
        self.ctyri_profile["justify"] = "center"
        self.ctyri_profile["text"] = "4"
        self.ctyri_profile.place(relx=0.83333,rely=0.74,relwidth=0.033333,relheight=0.04)
        self.ctyri_profile["command"] = self.ctyri_profile_command

        self.pet_profile=tk.Button(root)
        self.pet_profile["bg"] = "#007ad9"
        self.pet_profile["bd"] = 1
        self.pet_profile["relief"] = "flat"
        
        self.pet_profile["font"] = self.ft
        self.pet_profile["fg"] = "White"
        self.pet_profile["justify"] = "center"
        self.pet_profile["text"] = "5"
        self.pet_profile.place(relx=0.86666,rely=0.74,relwidth=0.033333,relheight=0.04)
        self.pet_profile["command"] = self.pet_profile_command

        self.sest_profile=tk.Button(root)
        self.sest_profile["bd"] = 1
        self.sest_profile["relief"] = "flat"
        self.sest_profile["bg"] = "#007ad9"
        
        self.sest_profile["font"] = self.ft
        self.sest_profile["fg"] = "White"
        self.sest_profile["justify"] = "center"
        self.sest_profile["text"] = "6"
        self.sest_profile.place(relx=0.9,rely=0.74,relwidth=0.033333,relheight=0.04)
        self.sest_profile["command"] = self.sest_profile_command

        self.chprofile_label=tk.Label(root)
        
        self.chprofile_label["font"] = self.ft
        self.chprofile_label["bg"] = "#4d4d4d"
        self.chprofile_label["fg"] = "White"
        self.chprofile_label["justify"] = "center"
        self.chprofile_label["text"] = "Choose profile:"
        self.chprofile_label.place(relx=0.7183,rely=0.69,relwidth=0.15,relheight=0.05)
    

    


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