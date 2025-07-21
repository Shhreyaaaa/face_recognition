from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
from subprocess import Popen


mydata=[]

class Attendance:
    def __init__(self,root):    
        self.root=root
        self.root.geometry("1530x900+0+0")
        self.root.title("Face Recognition System")

        # ============variables=============

        self.var_attend_id=StringVar()
        self.var_attend_rollno=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_dep=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_attendance=StringVar()
        

       # second img

        img=Image.open(r"D:\face recognition\college images\unive.jpg")
        img=img.resize((1500,170),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1500,height=170 )
        # bg 

        bg_img=Label(self.root,bg="white")
        bg_img.place(x=0,y=170,width=1500,height=810)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="black", fg="orchid")
        title_lbl.place(x=0,y=0,width=1500,height=45)

        home_btn = Button(self.root, text="Back To Home", cursor="hand2", font=("times new roman", 13, "bold"), bd=0, highlightthickness=0, bg="white", fg="blue", command=self.home_page)
        home_btn.place(x=1280, y=825, width=130, height=30)

        #main label frame

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=45,width=1425,height=690)

        #left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=720,height=630)

        img_left=Image.open(r"college images\att.jpg")
        img_left=img_left.resize((330,200),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=15,y=10,width=330,height=200)

        img_right=Image.open(r"college images\students.jpg")
        img_right=img_right.resize((330,200),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Left_frame,image=self.photoimg_right)
        f_lbl.place(x=370,y=10,width=330,height=200)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=20,y=230,width=674,height=330)

        # Label and entry

        #attendance id

        attendanceId_label=Label(left_inside_frame,text="Attendance ID:",font=("times new roman",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        attendanceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_id,font=("times new roman",13,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        #Roll No

        RollNolabel=Label(left_inside_frame,text="Roll No.:",font=("times new roman",12,"bold"),bg="white")
        RollNolabel.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        RollNoentry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_rollno,font=("times new roman",13,"bold"))
        RollNoentry.grid(row=0,column=3,padx=10,pady=10,sticky=W)
        
        #Name

        Name_label=Label(left_inside_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        Name_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        Name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_name,font=("times new roman",13,"bold"))
        Name_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        #date

        date_label=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=1,column=2,padx=10,pady=10,sticky=W)

        date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_date,font=("times new roman",13,"bold"))
        date_entry.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        #department

        department_label=Label(left_inside_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        department_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        department_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_dep,font=("times new roman",13,"bold"))
        department_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        #time

        time_label=Label(left_inside_frame,text="Time",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=2,padx=10,pady=10,sticky=W)

        time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_time,font=("times new roman",13,"bold"))
        time_entry.grid(row=2,column=3,padx=10,pady=10,sticky=W)

        #Attendance Status

        attendance_label=Label(left_inside_frame,text="Attendance Status:",font=("times new roman",12,"bold"),bg="white")
        attendance_label.grid(row=3,column=0,padx=10,pady=10,sticky=W)
        
        self.attendance_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_attend_attendance,font=("times new roman",12,"bold"),state="readonly")
        self.attendance_combo["values"]=("Status","Absent","Present")
        self.attendance_combo.current(0)
        self.attendance_combo.grid(row=3,column=1,padx=10,pady=10,sticky=W)

        # buttons frame

        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=250,width=670,height=35)

        importcsv_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        importcsv_btn.grid(row=0,column=0)

        exportcsv_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        exportcsv_btn.grid(row=0,column=1)

        update_btn=Button(btn_frame,text="Update",width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=16,command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        #Right label frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=740,y=10,width=670,height=630)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=10,y=10,width=640,height=550)

        #=======scroll bar=============

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","dep","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll No.")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("dep",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("id",width="100")
        self.AttendanceReportTable.column("roll",width="100")
        self.AttendanceReportTable.column("name",width="100")
        self.AttendanceReportTable.column("dep",width="100")
        self.AttendanceReportTable.column("time",width="100")
        self.AttendanceReportTable.column("date",width="100")
        self.AttendanceReportTable.column("attendance",width="100")

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #==========================fetch data=====================

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    #import csv

    def importCsv(self):
        global mydata
        mydata.clear()
        flname=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(flname) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #export csv

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to export",parent=self.root)
                return False
            flname=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(flname,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data has been Exported to "+os.path.basename(flname)+" successfully.")
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def get_cursor(self, event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]

        self.var_attend_id.set(rows[0])
        self.var_attend_rollno.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_dep.set(rows[3])
        self.var_attend_time.set(rows[4])
        self.var_attend_date.set(rows[5])
        self.var_attend_attendance.set(rows[6])

    def reset_data(self):
        self.var_attend_id.set()
        self.var_attend_rollno.set()
        self.var_attend_name.set()
        self.var_attend_dep.set()
        self.var_attend_time.set()
        self.var_attend_date.set()
        self.var_attend_attendance.set()

    def home_page(self):
        self.root.destroy()
        Popen(["python", "main.py"])


  
        


if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()

