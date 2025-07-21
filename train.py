from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from subprocess import Popen

class Train:
    def __init__(self,root):    
        self.root=root
        self.root.geometry("1530x900+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="black", fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=50)

        home_btn = Button(self.root, text="Home", cursor="hand2", font=("times new roman", 14, "bold"), bd=0, highlightthickness=0, bg="black", fg="white", command=self.home_page)
        home_btn.place(x=1300, y=15, width=100, height=30)

        img=Image.open(r"D:\face recognition\college images\bgg1.jpg")
        img=img.resize((1530,840),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=50,width=1530,height=840)

        img_top=Image.open(r"D:\face recognition\college images\train.jpeg")
        img_top=img_top.resize((1300,700),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=80,y=120,width=1280,height=680)

        #button

        b1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",20,"bold"),bg="red", fg="white") 
        b1.place(x=320,y=560,width=200,height=60)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # Gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #==================================Train the classifier and Save========================

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!!")

    def home_page(self):
        self.root.destroy()
        Popen(["python", "main.py"])

                





if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
