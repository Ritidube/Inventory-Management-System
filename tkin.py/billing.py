from tkinter import*
from PIL import Image,ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed by Struggling with bits")
        self.root.config(bg="white")
        #headingtitle
        orignal_image=Image.open("tkin.py/Images/Logo.png")
        resized_image=orignal_image.resize((150, 70))
        self.icon_title=ImageTk.PhotoImage(resized_image)
        title=Label(self.root,text="Invntory Managemen System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #button__logout
        btn_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,height=50,width=150)
        #welcomemsg__clock__date
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#4D636D",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
