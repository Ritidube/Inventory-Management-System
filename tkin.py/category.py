from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed by Struggling with bits")
        self.root.config(bg="white")
        self.root.focus_force()
        #----Variables---------
        self.var_cat_id=StringVar()
        self.var_name=StringVar()
#----------Title-----------
        lbl_title=Label(self.root,text="Manage Product Category",font=("goudy old style",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
        lbl_name=Label(self.root,text="Enter Category Name",font=("goudy old style",30),bg="white").place(x=50,y=100)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",18),bg="lightyellow").place(x=50,y=170,width=300)


        btn_add=Button(self.root,text="ADD",font=("goudy old style",18),bg="#4caf50",fg="white",cursor="hand2").place(x=360,y=170,width=150,height=30)
        btn_delete=Button(self.root,text="Delete",font=("goudy old style",18),bg="red",fg="white",cursor="hand2").place(x=520,y=170,width=150,height=30)
        


if __name__=="__main__":
    root=Tk()
    obj=categoryClass(root)
    root.mainloop()            