from tkinter import *
from PIL import Image, ImageTk
import webbrowser
from subprocess import Popen

class Developer:
    def __init__(self, root):    
        self.root = root
        self.root.geometry("1530x900+0+0")
        self.root.title("Face Recognition System")

        # Title Label
        title_lbl = Label(self.root, text="DEVELOPER DETAILS", font=("times new roman", 35, "bold"), bg="black", fg="orchid")
        title_lbl.place(x=0, y=0, width=1530, height=50)

        # Home Button
        home_btn = Button(self.root, text="Home", cursor="hand2", font=("times new roman", 14, "bold"), bd=0, bg="black", fg="white", command=self.home_page)
        home_btn.place(x=1300, y=15, width=100, height=30)
        
        # Background Image
        bg_img = Image.open(r"D:\face recognition\college images\new bg.jpg").resize((1480, 850), Image.LANCZOS)
        self.photobg_img = ImageTk.PhotoImage(bg_img)

        bg_label = Label(self.root, image=self.photobg_img)
        bg_label.place(x=0, y=50, width=1480, height=850)

        # Main Frame with Border
        main_frame = Frame(bg_label, bd=5, relief="solid", bg="white")
        main_frame.place(x=100, y=320, width=1230, height=450)

        # Profile Image
        my_image = Image.open(r"D:\face recognition\college images\Shreya.jpeg").resize((250, 300), Image.LANCZOS)
        self.photomy_image = ImageTk.PhotoImage(my_image)

        img_label = Label(main_frame, image=self.photomy_image)
        img_label.place(x=10, y=10, width=250, height=300)

        # Developer Info
        Label(main_frame, text="Hello! My name is Shreya", font=("times new roman", 20, "bold"), bg="white", fg="red").place(x=280, y=20)

        text_lines = [
            "I am a motivated and detail-oriented Full-Stack Python Developer with a strong foundation in AI,",
            "Machine Learning, and Cloud Computing. Currently pursuing my Master’s in Computer Applications,",
            "I have hands-on experience with Python, Java, MySQL, and web technologies, along with a passion",
            "for problem-solving and innovation. With experience in Microsoft 365, Azure, and cybersecurity,",
            "I am eager to leverage my skills to build efficient and scalable solutions."
        ]
        
        y_offset = 80
        for line in text_lines:
            Label(main_frame, text=line, font=("Segoe UI", 14), bg="white", fg="black").place(x=280, y=y_offset)
            y_offset += 30

        # Contact Label
        Label(main_frame, text="Feel free to connect with me at :", font=("Segoe UI", 14), bg="white", fg="black").place(x=280, y=260)

        # Clickable Email Label
        email_label = Label(main_frame, text="Email: Shreyajainbox@gmail.com", font=("times new roman", 14, "bold", "underline"), bg="white", fg="blue", cursor="hand2")
        email_label.place(x=570, y=260)
        email_label.bind("<Button-1>", lambda e: self.open_link("mailto:Shreyajainbox@gmail.com"))

        # Clickable LinkedIn Label
        linkedin_label = Label(main_frame, text="LinkedIn: shreya-jainn", font=("times new roman", 14, "bold", "underline"), bg="white", fg="blue", cursor="hand2")
        linkedin_label.place(x=880, y=260)
        linkedin_label.bind("<Button-1>", lambda e: self.open_link("https://www.linkedin.com/in/shreya-jainn"))

    def home_page(self):
        self.root.destroy()
        Popen(["python", "main.py"])

    def open_link(self, url):
        """Opens a given URL in the default web browser."""
        webbrowser.open(url)

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()