from tkinter import*
from PIL import Image,ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass

from sales import salesClass
from billing import BillClass
from product import productClass

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

        #LEFT MENU
        self.MenuLogo=Image.open("tkin.py/Images/side-menu.jpg")
        self.MenuLogo=self.MenuLogo.resize((200,200))
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)
        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)
        

        lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)
       
       
        btn_employee=Button(LeftMenu,text="Employee",command=self.employee,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2")
        btn_employee.pack(side=TOP,fill=X)
        btn_Supplier=Button(LeftMenu,text="Supplier",command=self.supplier,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2")
        btn_Supplier.pack(side=TOP,fill=X)
        btn_Category=Button(LeftMenu,text="Category",command=self.category,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2")
        btn_Category.pack(side=TOP,fill=X)
        btn_products=Button(LeftMenu,text="Products",command=self.product,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2")
        btn_products.pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="Sales",command=self.sales,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2")
        btn_sales.pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Exit",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2")
        btn_exit.pack(side=TOP,fill=X)

       #content
        self.lbl_employee=Label(self.root,text="Total Employee\n[0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=650,y=120,height=150,width=300)
        self.lbl_ssupplier=Label(self.root,text="Total Supplier\n[0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_ssupplier.place(x=300,y=120,height=150,width=300)
        self.lbl_ccategory=Label(self.root,text="Total Category\n[0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_ccategory.place(x=1000,y=120,height=150,width=300)
        self.lbl_pproduct=Label(self.root,text="Total Product\n[0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_pproduct.place(x=300,y=300,height=150,width=300)
        self.lbl_ssales=Label(self.root,text="Total Sales\n[0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_ssales.place(x=650,y=300,height=150,width=300)

        #footer
        self.lbl_footer=Label(self.root,text="Vyपार-Inventory Management System | Developed by Struggling with bits\nFor any Technical issue Contact:1234567890\n Email:Strugglingwidbits@gmail.com",font=("times new roman",12),bg="#4D636D",fg="white").pack(side=BOTTOM,fill=X)
#=============================================================================================================================================================================================================================================================================================
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

#==========================================================================
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)     
#==========================================================================
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win) 
#===========================================================================   
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)



    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)     

    def billing(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=BillClass(self.new_win)


if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()    