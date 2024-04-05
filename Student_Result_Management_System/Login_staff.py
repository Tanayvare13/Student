from tkinter import *
from PIL import Image,ImageTk,ImageDraw
from datetime import *
import time
from math import *
import sqlite3
from tkinter import messagebox,ttk
import os
class Login_window_staff:
    def __init__(self,root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")

        #--------------Background Colors----------------
        left_lbl = Label(self.root,bg="#08a3d2",bd=0)
        left_lbl.place(x=0,y=0,width=600,relheight=1)
        
        right_lbl = Label(self.root,bg="#031f3c",bd=0)
        right_lbl.place(x=600,y=0,relwidth=1,relheight=1)

        #----------------Frame---------------------------
        login_frame = Frame(self.root,bg="white")
        login_frame.place(x=250,y=100,width=800,height=500)

        title = Label(login_frame,text="STAFF LOGIN",font=("times new roman",30,"bold"),bg="white",fg="#08a3d2").place(x=250,y=50)
        
        email = Label(login_frame,text="EMAIL ADDRESS",font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=250,y=150)
        self.txt_email = Entry(login_frame,font=("times new roman",15,"bold"),bg="lightgray")
        self.txt_email.place(x=250,y=180,width=350,height=35)
        
        password = Label(login_frame,text="PASSWORD",font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=250,y=250)
        self.txt_password = Entry(login_frame,font=("times new roman",15,"bold"),bg="lightgray")
        self.txt_password.place(x=250,y=280,width=350,height=35)

        btn_reg = Button(login_frame,text="Register New Account?",font=("times new roman",14,"bold"),command=self.register_window,bg="white",fg="#b00857",bd=0,cursor="hand2").place(x=250,y=320)
        btn_forget = Button(login_frame,text="Forget Password?",font=("times new roman",14,"bold"),command=self.forget_password_window,bg="white",fg="red",bd=0,cursor="hand2").place(x=460,y=320)
        
        btn_login = Button(login_frame,text="LOGIN",font=("times new roman",20,"bold"),command=self.Login,fg="white",bg="#b00857",cursor="hand2").place(x=250,y=380,width=180,height=40)

        #----------------Clock----------------------
        self.lbl = Label(self.root,text="\nAnalog Clock",font=("Book Antiqua",25,"bold"),fg="white",compound=BOTTOM,bg="#081923",bd=0)
        self.lbl.place(x=90,y=120,width=350,height=450)

        self.working()

    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_password.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_email.delete(0,END)  

    def forget_password(self):
        if self.cmb_quest.get() == "Select" or self.txt_answer.get() == "" or self.txt_new_password.get() == "":
            messagebox.showerror("Error","All fields are required",parent=self.root2)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from staff where email=? and question=? and answer=?",(self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Please Select the Correct Security Question / Enter Answer",parent=self.root2)
                else:
                    cur.execute("update staff set password=? where email=?",(self.txt_new_password.get(),self.txt_email.get(),))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Your Password has been changed,Try to Login with new password",parent=self.root2)
                    self.reset()
                    self.root2.destroy()

            except Exception as es:
                messagebox.showerror("Error",f"Error due to {str(es)}",parent=self.root)


    def forget_password_window(self):
        if self.txt_email.get() == "":
             messagebox.showerror("Error","Please enter the email address to reset your password",parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from staff where email=?",(self.txt_email.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Please enter the valid email address to reset your password",parent=self.root)
                else:
                    self.root2 = Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x400+500+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    title2 = Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)
        
                    #--------------Forget Password----------------------
                    question = Label(self.root2,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        
                    self.cmb_quest = ttk.Combobox(self.root2,font=("times new roman",13,"bold"),state="readonly",justify=CENTER)
                    self.cmb_quest["values"] = ("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name","Your Favorite Crickter Name")
                    self.cmb_quest.place(x=50,y=130,width=250)
                    self.cmb_quest.current(0)

                    answer = Label(self.root2,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=180)
                    self.txt_answer = Entry(self.root2,font=("times new roman",15,"bold"),bg='lightgray')
                    self.txt_answer.place(x=50,y=210,width=250)
        
                    new_password = Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=260)
                    self.txt_new_password = Entry(self.root2,font=("times new roman",15,"bold"),bg='lightgray')
                    self.txt_new_password.place(x=50,y=290,width=250)

                    btn_change_password = Button(self.root2,text="Reset Password",bg="green",fg="white",font=("times new roman",15,"bold"),command=self.forget_password).place(x=90,y=340)   
                                    
                con.close()
                    

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)
            
        
            


    def register_window(self):
        self.root.destroy()
        #from Staff_register import Register_staff
        os.system("python Student_Result_Management_System\Staff_register.py")
      

    def Login(self):
        if self.txt_email.get() == "" or self.txt_password.get() == "":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from staff where email=? and password=?",(self.txt_email.get(),self.txt_password.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid USERNAME AND PASSWORD",parent=self.root)
                else:
                    messagebox.showinfo("Success",f"Welcome: {self.txt_email.get()}",parent=self.root)
                    self.root.destroy()
                    os.system("python Staff_Dashboard.py")                   
                con.close()
                    

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)





    
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

root = Tk()
obj = Login_window_staff(root)
root.mainloop()
