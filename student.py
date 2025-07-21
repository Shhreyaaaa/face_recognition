from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
from subprocess import Popen

class Student:
    def __init__(self,root):    
        self.root=root
        self.root.geometry("1530x900+0+0")
        self.root.title("Face Recognition System")

        #=============================variables=======================

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_rollno=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        

    
        # img

        img=Image.open(r"D:\face recognition\college images\unive.jpg")
        img=img.resize((1500,150),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1500,height=150 )


        # bg 

        bg_img=Label(self.root,bg="white")
        bg_img.place(x=0,y=150,width=1500,height=810)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="black", fg="orchid")
        title_lbl.place(x=0,y=0,width=1500,height=45)

        home_btn = Button(self.root, text="Back To Home", cursor="hand2", font=("times new roman", 13, "bold"), bd=0, highlightthickness=0, bg="white", fg="blue", command=self.home_page)
        home_btn.place(x=1280, y=830, width=130, height=30)

        # main frame

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=45,width=1425,height=690)

        #left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=720,height=660)

        # current course

        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=10,y=10,width=695,height=150)

        #departemnt

        dep_label=Label(current_course_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        #course

        course_label=Label(current_course_frame,text="Course:",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year

        year_label=Label(current_course_frame,text="Year:",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester

        semester_label=Label(current_course_frame,text="Semester:",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),state="readonly")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class student information

        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=10,y=180,width=695,height=380)

        #student ID

        studentId_label=Label(class_student_frame,text="Student ID",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_id,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # student name

        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_name,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # class division

        class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        Div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly")
        Div_combo["values"]=("Select Division","A","B","C","D")
        Div_combo.current(0)
        Div_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        # Roll No.

        rollno_label=Label(class_student_frame,text="Roll No.:",font=("times new roman",12,"bold"),bg="white")
        rollno_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        rollno_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_rollno,font=("times new roman",13,"bold"))
        rollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Gender

        Gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        Gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        # DOB

        DOB_label=Label(class_student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        DOB_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        DOB_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_dob,font=("times new roman",13,"bold"))
        DOB_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # Email

        Email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        Email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_email,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # Phone No.

        PhoneNo_label=Label(class_student_frame,text="Phone No.:",font=("times new roman",12,"bold"),bg="white")
        PhoneNo_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        PhoneNo_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_phone,font=("times new roman",13,"bold"))
        PhoneNo_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # Address

        Address_label=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        Address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        Address_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_address,font=("times new roman",13,"bold"))
        Address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        # Teacher's Name

        TeacherName_label=Label(class_student_frame,text="Teacher's Name",font=("times new roman",12,"bold"),bg="white")
        TeacherName_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        TeacherName_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_teacher,font=("times new roman",13,"bold"))
        TeacherName_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        # radio buttons
        
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)

        # buttons frame

        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=10,y=230,width=670,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=10,y=265,width=670,height=35)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=33,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=1,column=0)

        update_photo_btn=Button(btn_frame1,command=self.update_photo_sample,text="Update Photo Sample",width=32,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=1,column=1)

        #Right label frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=740,y=10,width=670,height=660)

        img_right=Image.open(r"D:\face recognition\college images\std3.jpeg")
        img_right=img_right.resize((635,230),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=15,y=10,width=635,height=230)

        #======Search System==============

        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=10,y=245,width=645,height=70)

        search_label=Label(Search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",13,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Roll No.","Phone No.")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(Search_frame,text="Search",width=8,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=2)

        showall_btn=Button(Search_frame,text="Show All",width=8,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4,padx=2)

        #=======table frame==============

        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=330,width=645,height=250)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","rollno","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("rollno",text="Roll No.")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone No.")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo Sample Status")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width="100")
        self.student_table.column("course",width="100")
        self.student_table.column("year",width="100")
        self.student_table.column("sem",width="100")
        self.student_table.column("id",width="100")
        self.student_table.column("name",width="100")
        self.student_table.column("div",width="100")
        self.student_table.column("rollno",width="100")
        self.student_table.column("gender",width="100")
        self.student_table.column("dob",width="100")
        self.student_table.column("email",width="100")
        self.student_table.column("phone",width="100")
        self.student_table.column("address",width="100")
        self.student_table.column("teacher",width="100")
        self.student_table.column("photo",width="140")

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #===========================funtion declaration=======================

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fiels are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Shreya@2110",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_id.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_rollno.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get(),      
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    #===================fetch data==========================

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shreya@2110",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!= 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #======================get cursor==============================

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_rollno.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # update function

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fiels are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update these student details?",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Shreya@2110",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,RollNo=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                                                            self.var_sem.get(), 
                                                                                                                                                                                                                            self.var_name.get(),
                                                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                                                            self.var_rollno.get(),
                                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                                                            self.var_id.get()
                                                                                                                                                                                                                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    # delete function

    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student ID is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Shreya@2110",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    # reset function

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_div.set("Select Division")
        self.var_rollno.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    #==============================Generate data set or Take Photo Samples====================================

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fiels are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Shreya@2110",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("Update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,RollNo=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                                                            self.var_sem.get(), 
                                                                                                                                                                                                                            self.var_name.get(),
                                                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                                                            self.var_rollno.get(),
                                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                                                            self.var_id.get()==id+1
                                                                                                                                                                                                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

# ======================Load predefined data on face frontals from opencv=================================

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                # Scaling factor=1.3
                # Minimum Neighbor=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!!!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    # ==============update photo sample============


    def update_photo_sample(self):
        if self.var_id.get() == "":
            messagebox.showerror("Error", "Please enter a valid Student ID", parent=self.root)
            return

        try:
            student_id = self.var_id.get()

            # Connect to MySQL
            conn = mysql.connector.connect(host="localhost", username="root", password="Shreya@2110", database="face_recognizer")
            my_cursor = conn.cursor()

            # Check if student exists
            my_cursor.execute("SELECT Name FROM student WHERE Student_id = %s", (student_id,))
            student = my_cursor.fetchone()
            if student is None:
                messagebox.showerror("Error", "Student ID not found in the database.", parent=self.root)
                return

            # Ensure 'data' folder exists
            if not os.path.exists("data"):
                os.makedirs("data")

            # Load face classifier
            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    return img[y:y+h, x:x+w]  # Return the cropped face
                return None
            
            # Start capturing images
            cap = cv2.VideoCapture(0)
            img_id = 0
            while True:
                ret, frame = cap.read()
                cropped_face = face_cropped(frame)

                if cropped_face is not None:
                    img_id += 1
                    face = cv2.resize(cropped_face, (450, 450))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    file_name_path = f"data/user.{student_id}.{img_id}.jpg"
                    cv2.imwrite(file_name_path, face)
                    cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                    cv2.imshow("Cropped Face", face)

                if cv2.waitKey(1) == 13 or img_id == 100:  
                    break

            cap.release()
            cv2.destroyAllWindows()

            # Update MySQL to mark that a new photo sample exists
            my_cursor.execute("UPDATE student SET PhotoSample = 'Yes' WHERE Student_id = %s", (student_id,))
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Photo sample updated successfully!", parent=self.root)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.root)

    # ===========home page================

    def home_page(self):
        self.root.destroy()
        Popen(["python", "main.py"])


if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()