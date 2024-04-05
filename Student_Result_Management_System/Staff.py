from tkinter import *
from PIL import Image,ImageTk
from Course import CourseClass
from student import StudentClass
from result import ResultClass
from report import ReportClass
from tkinter import messagebox,ttk
import os
from PIL import Image,ImageTk,ImageDraw
from datetime import *
import time
from math import *
import sqlite3
import matplotlib.pyplot as plt
class RMS:
    def __init__(self,root):
        self.root = root
        self.root.title('Student Result Management System')
        self.root.geometry('1920x1080+0+0')
        self.root.config(bg='white')
        self.root.focus_force()
        #-------Icons---------
        self.logo_dash = ImageTk.PhotoImage(file=r"Student_Result_Management_System\images\universal_logo.jpg")

        #-----Title-------
        title = Label(self.root, text="Student Result Management System (Staff Dashboard)",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#191970", fg="white").place(x=0, y=0, relwidth=1, height=50)
        #-----Menu--------
        M_Frame = LabelFrame(self.root, text="Menus", font=("times new roman",15),bg="white")
        M_Frame.place(x=10, y=70, width=1540, height=80)
        
        ################# buttons-------------------------------------
        
        btn_PieChart = Button(M_Frame, text="Pie Chart", font=("goudy old style",15,"bold"),bg="#1E90FF",fg="white",cursor="hand2",command=self.display_course_pie_chart).place(x=1340,y=5,width=200,height=40)

    
        ###################################################

        btn_Course = Button(M_Frame, text="Course", font=("goudy old style",15,"bold"),bg="#1E90FF",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
        btn_Student = Button(M_Frame, text="Student", font=("goudy old style",15,"bold"),bg="#1E90FF",fg="white",cursor="hand2",command=self.add_student).place(x=240,y=5,width=200,height=40)
        btn_Result = Button(M_Frame, text="Result", font=("goudy old style",15,"bold"),bg="#1E90FF",fg="white",cursor="hand2",command=self.add_result).place(x=460,y=5,width=200,height=40)
        btn_View = Button(M_Frame, text="View Student Result", font=("goudy old style",15,"bold"),bg="#1E90FF",fg="white",cursor="hand2",command=self.add_report).place(x=680,y=5,width=200,height=40)
        btn_Logout = Button(M_Frame, text="Logout", font=("goudy old style",15,"bold"),bg="#1E90FF",fg="white",cursor="hand2",command=self.logout).place(x=900,y=5,width=200,height=40)
        btn_Exit = Button(M_Frame, text="Exit", font=("goudy old style",15,"bold"),bg="#1E90FF",fg="white",cursor="hand2",command=self.Exit).place(x=1120,y=5,width=200,height=40)
        #-----Content-window------
        self.bg_image = Image.open(r"Student_Result_Management_System\images\universal_college_bg.png")
        self.bg_image = self.bg_image.resize((920,350),Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(self.bg_image)

        self.lbl_bg = Label(self.root, image=self.bg_image).place(x=400, y=180, width=920, height=350)

        #-----Update_details------
        self.lbl_course = Label(self.root, text="Total Courses\n[ 0 ]", font=("goudy old style", 20), bd=10,relief=RIDGE,bg="#e43b06", fg="white")
        self.lbl_course.place(x=400, y=530, width=300, height=100)

        self.lbl_student = Label(self.root, text="Total Students\n[ 0 ]", font=("goudy old style", 20), bd=10,relief=RIDGE,bg="#0676ad", fg="white")
        self.lbl_student.place(x=710, y=530, width=300, height=100)

        self.lbl_result = Label(self.root, text="Total Results\n[ 0 ]", font=("goudy old style", 20), bd=10,relief=RIDGE,bg="#038074", fg="white")
        self.lbl_result.place(x=1020, y=530, width=300, height=100)

        #----------------Clock----------------------
        self.lbl = Label(self.root,text="\nAnalog Clock",font=("Book Antiqua",25,"bold"),fg="white",compound=BOTTOM,bg="#081923",bd=0)
        self.lbl.place(x=10,y=180,width=350,height=450)

        self.working()

        #-----Footer-------
        Footer = Label(self.root, text="SRMS-Student Result Management System\nUsing Python",padx=10,font=("goudy old style",13,"bold"),bg="#262626", fg="white").pack(side=BOTTOM, fill=X)
        self.update_details()
#----------------------------------------------------------------------------------------------
    def update_details(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from course")
            cr = cur.fetchall()
            self.lbl_course.config(text=f"Total Courses \n[{str(len(cr))}]")

            cur.execute("select * from student")
            cr = cur.fetchall()
            self.lbl_student.config(text=f"Total Students \n[{str(len(cr))}]")

            cur.execute("select * from result")
            cr = cur.fetchall()
            self.lbl_result.config(text=f"Total Results \n[{str(len(cr))}]")

            self.lbl_course.after(200,self.update_details)
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    
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
    
    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = StudentClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ResultClass(self.new_win)

    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ReportClass(self.new_win)

    def logout(self):
        op = messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
        if op == True:
            self.root.destroy()
            os.system("python Student_Result_Management_System\Main_dashboard.py")

    def Exit(self):
        op = messagebox.askyesno("Confirm","Do you really want to exit?",parent=self.root)
        if op == True:
            self.root.destroy()
            
            
      # Add the function to display the pie chart
    
    def display_course_pie_chart(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            # Fetch data from the database
            cur.execute("SELECT course, COUNT(*) AS num_students FROM student GROUP BY course")
            data = cur.fetchall()
            con.close()

            # Separate data into course names and number of students
            courses = [row[0] for row in data]
            num_students = [row[1] for row in data]

            # Plot the pie chart
            plt.figure(figsize=(6,6))
            plt.pie(num_students, labels=courses, autopct='%1.0f%%', startangle=140)
            plt.axis('equal') 
            plt.title('Course Distribution Pie Chart')

            # Show the plot
            plt.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
        