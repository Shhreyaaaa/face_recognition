from tkinter import*
from tkinter import ttk
import tkinter.messagebox
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
import tkinter
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import HelpDesk

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x900+0+0")
        self.root.title("Face recognition system")

        # bg image

        self.img1 = Image.open(r"D:\face recognition\college images\Blue and White Illustrative Page Border Document A4.png")
        self.img1 = self.img1.resize((1530, 900), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(self.img1)

        bg_img=Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=0,width=1530,height=900)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="black", fg="darkorchid")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #=================time==================

        def time():
            string =strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl = Label(title_lbl,font=("times new roman",11,"bold"),bg="black",fg="white")
        lbl.place(x=0,y=0,width=110,height=50)
        time()


        # student button

        img2=Image.open(r"D:\face recognition\college images\std.jpg")
        img2=img2.resize((220,220),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        b1=Button(bg_img,image=self.photoimg2,command=self.student_details,cursor="hand2")
        b1.place(x=160,y=200,width=220,height=220)

        b1=Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue", fg="white") 
        b1.place(x=160,y=400,width=220,height=40)


        # Detect face button

        img3=Image.open(r"D:\face recognition\college images\fd4.jpg")
        img3=img3.resize((220,220),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        b1=Button(bg_img,image=self.photoimg3,cursor="hand2",command=self.face_data)
        b1.place(x=460,y=200,width=220,height=220)

        b1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue", fg="white") 
        b1.place(x=460,y=400,width=220,height=40)

        # Attendance face button

        img4=Image.open(r"D:\face recognition\college images\attendance1.png")
        img4=img4.resize((220,220),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.attendance_data)
        b1.place(x=760,y=200,width=220,height=220)

        b1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue", fg="white") 
        b1.place(x=760,y=400,width=220,height=40)

        # Help face button

        img5=Image.open(r"D:\face recognition\college images\help.jpg")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.help_data)
        b1.place(x=1060,y=200,width=220,height=220)

        b1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue", fg="white") 
        b1.place(x=1060,y=400,width=220,height=40)

        # Train face button

        img6=Image.open(r"D:\face recognition\college images\training.jpg")
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.train_data)
        b1.place(x=160,y=500,width=220,height=220)

        b1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue", fg="white") 
        b1.place(x=160,y=700,width=220,height=40)

        # Photos face button

        img7=Image.open(r"D:\face recognition\college images\photo2.jpg")
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.open_img)
        b1.place(x=460,y=500,width=220,height=220)

        b1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue", fg="white") 
        b1.place(x=460,y=700,width=220,height=40)

        # Developer face button

        img8=Image.open(r"D:\face recognition\college images\developer3.jpg")
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.developer_data)
        b1.place(x=760,y=500,width=220,height=220)

        b1=Button(bg_img,text="Developer Details",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue", fg="white") 
        b1.place(x=760,y=700,width=220,height=40)

        # Exit face button

        img9=Image.open(r"D:\face recognition\college images\exit1.jpg")
        img9=img9.resize((220,220),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.iExit)
        b1.place(x=1060,y=500,width=220,height=220)

        b1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue", fg="white") 
        b1.place(x=1060,y=700,width=220,height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit?",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return


    #=======Functions Buttons==============

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=HelpDesk(self.new_window)




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

    
