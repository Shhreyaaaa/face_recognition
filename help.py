from tkinter import *
from PIL import Image, ImageTk
import webbrowser
from subprocess import Popen

class HelpDesk:
    def __init__(self, root):    
        self.root = root
        self.root.geometry("1530x900+0+0")
        self.root.title("Face Recognition System")

        # Title Label
        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 35, "bold"), bg="black", fg="palevioletred")
        title_lbl.place(x=0, y=0, width=1530, height=50)

        # Home Button
        home_btn = Button(self.root, text="Home", cursor="hand2", font=("times new roman", 14, "bold"), bd=0, highlightthickness=0, bg="black", fg="white", command=self.home_page)
        home_btn.place(x=1300, y=15, width=100, height=30)

        # Background Images
        bg_img = Image.open(r"D:\face recognition\college images\bg3.jpg").resize((600, 850), Image.LANCZOS)
        self.photobg_img = ImageTk.PhotoImage(bg_img)
        Label(self.root, image=self.photobg_img).place(x=0, y=50, width=600, height=850)

        bg_img1 = Image.open(r"D:\face recognition\college images\Blue and White Illustrative Page Border Document A4.png").resize((900, 850), Image.LANCZOS)
        self.photobg_img1 = ImageTk.PhotoImage(bg_img1)
        Label(self.root, image=self.photobg_img1).place(x=600, y=50, width=900, height=850)

        # Main Frame
        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=680, y=130, width=680, height=670)

        # Welcome Text
        Label(main_frame, text="WELCOME TO FACE RECOGNITION SYSTEM", font=("times new roman", 21, "bold", "underline"), bg="white", fg="black").place(x=30, y=10)

        # Help Desk Image
        img_right = Image.open(r"D:\face recognition\college images\help desk.png").resize((650, 270), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        Label(main_frame, image=self.photoimg_right).place(x=20, y=50, width=650, height=270)

        text_lines = [
            "Face Recognition Attendance System, is an advanced application that utilizes facial",
            "recognition technology to automate attendance tracking. Built using Python, Open",
            "CV, and MySQL, this system captures and processes student images to create a",
            "database of facial samples. Using Haar Cascade Classifier, it detects faces in real-time",
            "via a webcam and matches them against stored records for accurate identification.",
            "The system also includes features like student data management, photo sample",
            "updates, and a help desk with email integration. This project enhances security,",
            "reduces manual effort, and ensures a seamless, automated attendance process."
        ]
        
        y_offset = 300
        for line in text_lines:
            Label(main_frame, text=line, font=("Segoe UI", 13), bg="white", fg="black").place(x=20, y=y_offset)
            y_offset += 25

        Label(main_frame, text="Submit your queries on :", font=("times new roman", 14, "bold"), bg="white", fg="black").place(x=20, y=590)

        # **Email Label with Clickable Link**
        email_label = Label(main_frame, text="Email: Shreyajainbox@gmail.com", font=("times new roman", 13, "bold", "underline"), bg="white", fg="blue", cursor="hand2")
        email_label.place(x=230, y=590)
        email_label.bind("<Button-1>", lambda e: self.open_email())  # Binds click event to function

    def home_page(self):
        self.root.destroy()
        Popen(["python", "main.py"])

    def open_email(self):
        webbrowser.open("mailto:Shreyajainbox@gmail.com")  # Opens email client

if __name__ == "__main__":
    root = Tk()
    obj = HelpDesk(root)
    root.mainloop()