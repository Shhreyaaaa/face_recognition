from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System

def main():
    window=Tk() 
    app=Login_Window(window)
    window.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Page")
        self.root.geometry("1530x900+0+0")

        # Load and resize image
        img=Image.open(r"D:\face recognition\college images\bg1.jpeg")
        img=img.resize((1530,900),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg,bg="black")
        bg_img.place(x=0,y=0,width=1530,height=900)

        title_lbl=Label(bg_img,text="FACIAL RECOGNITION ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="black", fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        frame=Frame(self.root,bg="black")
        frame.place(x=550,y=220,width=460,height=450)

        img1=Image.open(r"D:\face recognition\college images\user profile.png")
        img1=img1.resize((100,100), Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        img1_lbl=Label(frame,image=self.photoimg1,bg="black",borderwidth=0)
        img1_lbl.place(x=180,y=15,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=155,y=115)

        #username and password label

        username_lbl=Label(frame,text="Username:",font=("times new roman",15,"bold"),fg="white",bg="black")
        username_lbl.place(x=50,y=175)

        self.textuser=StringVar()
        self.textpass=StringVar()

        textuser=ttk.Entry(frame,textvariable=self.textuser,font=("times new roman",15,"bold"))
        textuser.place(x=160,y=175,width=240)

        password_lbl=Label(frame,text="Password:",font=("times new roman",15,"bold"),fg="white",bg="black")
        password_lbl.place(x=50,y=220)

        textpass=ttk.Entry(frame,textvariable=self.textpass,font=("times new roman",15,"bold"))
        textpass.place(x=160,y=220,width=240)

        #icon images

        img2=Image.open(r"D:\face recognition\college images\user profile.png")
        img2=img2.resize((28,28), Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        img2_lbl=Label(frame,image=self.photoimg2,bg="black",borderwidth=0)
        img2_lbl.place(x=20,y=175,width=28,height=28)

        img3=Image.open(r"D:\face recognition\college images\pass1.png")
        img3=img3.resize((28,28), Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        img3_lbl=Label(frame,image=self.photoimg3,bg="black",borderwidth=0)
        img3_lbl.place(x=20,y=220,width=28,height=28)

        #login button

        login_btn=Button(frame,borderwidth=3,text="Login",command=self.login,cursor="hand2",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        login_btn.place(x=170,y=280,width=120,height=38)

        #register button

        register_btn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",11,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        register_btn.place(x=10,y=350,width=160)

        #forget pass button

        fgPass_btn=Button(frame,text="Forget Password",command=self.forget_pass,font=("times new roman",11,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        fgPass_btn.place(x=2,y=372,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.textuser.get()=="" or self.textpass.get()=="":
            messagebox.showerror("Error","All fields are required.")
        elif self.textuser.get()=="Shreya" and self.textpass.get()=="siya2110":
            messagebox.showinfo("Success","Welcome to the 'Face Recognition Sytem'")
        else:
            conn=mysql.connector.connect(host="HOSTNAME",user="YOUR_USERNAME",password="YOUR_DATABASE_PASSWORD",database="YOUR_DATABASE_NAME")
            cursor=conn.cursor()
            cursor.execute("select * from register where email=%s and pass=%s",(
                                                                                    self.textuser.get(),
                                                                                    self.textpass.get()  
                                                                                ))
            row=cursor.fetchone()
            # print row
            if row==None:
                messagebox.showerror("Error","Invalid username or password")
            else:
                open_main=messagebox.askyesno("Yes/No","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
                conn.commit()
                conn.close()

# ==========================reset password=======================

    def reset_pass(self):
        if self.Security_Q_combo.get()=="Select":
            messagebox.showerror("Error","Select the Security Question",parent=self.root2)
        elif self.security_A_entry.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.new_pass_entry.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="HOSTNAME",user="YOUR_USERNAME",password="YOUR_DATABASE_PASSWORD",database="YOUR_DATABASE_NAME")
            cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.textuser.get(),self.Security_Q_combo.get(),self.security_A_entry.get(),)
            cursor.execute(query,value)
            row=cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct Answer",parent=self.root2)
            else:
                query=("update register set pass=%s where email=%s")
                value=(self.new_pass_entry.get(),self.textuser.get())
                cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Reset","Your password has been reset, Please login with new password to confirm",parent=self.root2)
                self.root2.destroy()


# =========================forget password===============

    def forget_pass(self):
        if self.textuser.get()=="":
            messagebox.showerror("Error","Please enter the email to reset password")
        else:
            conn=mysql.connector.connect(host="HOSTNAME",user="YOUR_USERNAME",password="YOUR_DATABASE_PASSWORD",database="YOUR_DATABASE_NAME")
            cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.textuser.get(),)
            cursor.execute(query,value)
            row=cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("Error", "No user found with this email.")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Pssword")
                self.root2.geometry("340x450+610+710")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                Security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",13,"bold"),bg="white",fg="black")
                Security_Q.place(x=50,y=80)

                self.Security_Q_combo=ttk.Combobox(self.root2,font=("times new roman",12,"bold"),state="readonly")
                self.Security_Q_combo["values"]=("Select Question","What is your Birth Place?","What is your pet's name?","What is your favourite book?","What is the name of your first School?")
                self.Security_Q_combo.current(0)
                self.Security_Q_combo.place(x=50,y=110,width=250)

                security_A=Label(self.root2,text="Security Answer:",font=("times new roman",13,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.security_A_entry=ttk.Entry(self.root2,font=("times new roman",13,"bold"))
                self.security_A_entry.place(x=50,y=180,width=250)

                new_pass=Label(self.root2,text="New Password:",font=("times new roman",13,"bold"),bg="white",fg="black")
                new_pass.place(x=50,y=220)

                self.new_pass_entry=ttk.Entry(self.root2,font=("times new roman",13,"bold"))
                self.new_pass_entry.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",13,"bold"),bg="green",fg="white")
                btn.place(x=100,y=290)

# ============================Register page============================

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registeration Page")
        self.root.geometry("1530x900+0+0")

        # =========================variables===================

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        # Load and resize image
        bg_img = Image.open(r"D:\face recognition\college images\bg img2.jpg")
        bg_img = bg_img.resize((1530, 900), Image.LANCZOS)  # Resize to match window
        self.photobg_img = ImageTk.PhotoImage(bg_img)

        # Label to show background
        lbl = Label(self.root, image=self.photobg_img)
        lbl.place(x=0, y=0, width=1530, height=900)  # Explicit width & height

        frame=Frame(self.root,bg="black")
        frame.place(x=160,y=170,width=1120,height=550)

        img1=Image.open(r"D:\face recognition\college images\register.jpg")
        img1=img1.resize((400,490), Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        img1_lbl=Label(frame,image=self.photoimg1,bg="black",borderwidth=0)
        img1_lbl.place(x=30,y=30,width=400,height=490)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="black",fg="white")
        register_lbl.place(x=460,y=30)

        # ================label and entry================

        frame1=Frame(frame,bg="white")
        frame1.place(x=460,y=70,width=630,height=450)

        fname=Label(frame1,text="First Name:",font=("times new roman",13,"bold"),bg="white",fg="black")
        fname.place(x=30,y=30)

        fname_entry=ttk.Entry(frame1,textvariable=self.var_fname,font=("times new roman",13,"bold"))
        fname_entry.place(x=30,y=60,width=250)

        lname=Label(frame1,text="Last Name:",font=("times new roman",13,"bold"),bg="white",fg="black")
        lname.place(x=320,y=30)

        lname_entry=ttk.Entry(frame1,textvariable=self.var_lname,font=("times new roman",13,"bold"))
        lname_entry.place(x=320,y=60,width=250)

        contact=Label(frame1,text="Contact No.:",font=("times new roman",13,"bold"),bg="white",fg="black")
        contact.place(x=30,y=110)

        contact_entry=ttk.Entry(frame1,textvariable=self.var_contact,font=("times new roman",13,"bold"))
        contact_entry.place(x=30,y=140,width=250)

        email=Label(frame1,text="Email:",font=("times new roman",13,"bold"),bg="white",fg="black")
        email.place(x=320,y=110)

        email_entry=ttk.Entry(frame1,textvariable=self.var_email,font=("times new roman",13,"bold"))
        email_entry.place(x=320,y=140,width=250)

        Security_Q=Label(frame1,text="Select Security Question",font=("times new roman",13,"bold"),bg="white",fg="black")
        Security_Q.place(x=30,y=190)

        Security_Q_combo=ttk.Combobox(frame1,textvariable=self.var_securityQ,font=("times new roman",12,"bold"),state="readonly")
        Security_Q_combo["values"]=("Select Question","What is your Birth Place?","What is your pet's name?","What is your favourite book?","What is the name of your first School?")
        Security_Q_combo.current(0)
        Security_Q_combo.place(x=30,y=220,width=250)

        security_A=Label(frame1,text="Security Answer:",font=("times new roman",13,"bold"),bg="white",fg="black")
        security_A.place(x=320,y=190)

        security_A_entry=ttk.Entry(frame1,textvariable=self.var_securityA,font=("times new roman",13,"bold"))
        security_A_entry.place(x=320,y=220,width=250)

        pswd=Label(frame1,text="Password:",font=("times new roman",13,"bold"),bg="white",fg="black")
        pswd.place(x=30,y=270)

        pswd_entry=ttk.Entry(frame1,textvariable=self.var_pass,font=("times new roman",13,"bold"))
        pswd_entry.place(x=30,y=300,width=250)

        confirm_pswd=Label(frame1,text="Confirm Password:",font=("times new roman",13,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=320,y=270)

        confirm_pswd_entry=ttk.Entry(frame1,textvariable=self.var_confpass,font=("times new roman",13,"bold"))
        confirm_pswd_entry.place(x=320,y=300,width=250)

        #======checkbutton============

        self.var_check=IntVar()
        checkbtn=Checkbutton(frame1,variable=self.var_check,text="I agree to the Terms & Conditions.",font=("times new roman",11,"bold"),bg="white",fg="black",onvalue=1,offvalue=0)
        checkbtn.place(x=30,y=350)

        #=====buttons================

        img2=Image.open(r"D:\face recognition\college images\REGISTER.png")
        img2=img2.resize((140,45),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        b1=Button(frame1,image=self.photoimg2,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",13,"bold"))
        b1.place(x=110,y=390,width=140,height=45)

        img3=Image.open(r"D:\face recognition\college images\login.png")
        img3=img3.resize((140,45),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        b1=Button(frame1,image=self.photoimg3,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",13,"bold"))
        b1.place(x=330,y=390,width=140,height=45)

#==================function details=========================

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()==" Select Question":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password and Confirm Password must be same.",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree to our terms and conditions.",parent=self.root)
        else:
            conn=mysql.connector.connect(host="HOSTNAME",user="YOUR_USERNAME",password="YOUR_DATABASE_PASSWORD",database="YOUR_DATABASE_NAME")
            cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            cursor.execute(query,value)
            row=cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists, Please try another email",parent=self.root)
            else:
                cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Welcome, Registeration has been completed")

    def return_login(self):
        self.root.destroy()

    


    


if __name__ == "__main__":
    main()
