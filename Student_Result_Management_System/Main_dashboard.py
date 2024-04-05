from tkinter import *
from PIL import Image,ImageTk
from Course import CourseClass
from student import StudentClass
from result import ResultClass
from report import ReportClass
from tkinter import messagebox,ttk
#Sfrom Login_staff import Login_window_staff
import os
from PIL import Image,ImageTk,ImageDraw
from datetime import *
import time
from math import *
import sqlite3
class RMS_main:
    def __init__(self,root):
        self.root = root
        self.root.title('Student Result Management System')
        self.root.geometry('1450x750+0+0')
        self.root.config(bg='white')
        #-------Icons---------
        self.logo_dash = ImageTk.PhotoImage(file=r"Student_Result_Management_System\images\universal_logo.jpg")

        #-----Title-------
        title = Label(self.root, text="Universal college\nResult management system",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#191970", fg="white").place(x=0, y=0, relwidth=1, height=60)
        #-----Menu--------
        M_Frame = LabelFrame(self.root, text="Menus", font=("times new roman",15),bg="white")
        M_Frame.place(x=10, y=70, width=1340, height=80)

        btn_Staff_login = Button(M_Frame, text="Staff Login", font=("goudy old style",15,"bold"),bg="#1E90FF",fg="white",cursor="hand2",command=self.Staff).place(x=20,y=5,width=420,height=40)
        btn_Student_login = Button(M_Frame, text="Student Login", font=("goudy old style",15,"bold"),bg="#1E90FF",fg="white",cursor="hand2",command=self.Student).place(x=460,y=5,width=420,height=40)
        btn_Exit = Button(M_Frame, text="Exit", font=("goudy old style",15,"bold"),bg="#1E90FF",fg="white",cursor="hand2",command=self.Exit).place(x=900,y=5,width=420,height=40)
        #-----Content-window------
        self.bg_image = Image.open(r"Student_Result_Management_System\images\universal_college_bg.png")
        self.bg_image = self.bg_image.resize((920,350),Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(self.bg_image)

        self.lbl_bg = Label(self.root, image=self.bg_image).place(x=400, y=180, width=920, height=350)

        #----------------Clock----------------------
        self.lbl = Label(self.root,text="\nAnalog Clock",font=("Book Antiqua",25,"bold"),fg="white",compound=BOTTOM,bg="#081923",bd=0)
        self.lbl.place(x=10,y=180,width=350,height=450)

        self.working()

        #-----Footer-------
        Footer = Label(self.root, text="SRMS-Student Result Management System\nUsing Python",padx=10,font=("goudy old style",13,"bold"),bg="#262626", fg="white").pack(side=BOTTOM, fill=X)
        #self.update_details()
#----------------------------------------------------------------------------------------------
    def working(self):
        hours = datetime.now().time().hour
        minutes = datetime.now().time().minute
        seconds = datetime.now().time().second
        hr = (hours/12)*360
        min_ = (minutes/60)*360
        sec_ = (seconds/60)*360
        self.clock_image(hr,min_,sec_)
        self.img = ImageTk.PhotoImage(file="clock_new_2.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)

    def clock_image(self,hr,min_,sec_):
        clock = Image.new("RGB",(400,400),(8,25,35))   
        draw = ImageDraw.Draw(clock)
        #--------For Clock Image--------------------
        bg = Image.open(r"Student_Result_Management_System\images\c.png")
        bg = bg.resize((300,300),Image.LANCZOS)
        clock.paste(bg,(50,50))
        # ---------Hour Line Image-----------------------
        origen = 200,200
        draw.line((origen,200+55*sin(radians(hr)),200-55*cos(radians(hr))),fill="#df005e",width=4)
        # ---------Minute Line Image-----------------------
        draw.line((origen,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="white",width=3)
        # ---------Second Line Image-----------------------
        draw.line((origen,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="yellow",width=2)
        draw.ellipse((195,195,210,210),fill="#1ad5d5")
        clock.save("clock_new_2.png") 
    
    
    def Staff(self):
        self.root.destroy()
        #from Login_staff import Login_window_staff
        os.system("python Student_Result_Management_System\Login_staff.py")

    def Student(self):
        self.root.destroy()
        #from Login_stud import Login_window_stud
        os.system("python Student_Result_Management_System\Login_stud.py")

    def Exit(self):
        op = messagebox.askyesno("Confirm","Do you really want to exit?",parent=self.root)
        if op == True:
            self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = RMS_main(root)
    root.mainloop()
        