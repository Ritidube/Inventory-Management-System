from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed by Struggling with bits")
        self.root.config(bg="white")
        self.root.focus_force()

        #--------------------------------------
        #All variables
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()


        self.var_sup_invoice=StringVar()     #stringvar is taken for database mai koi error na aaye
        self.var_name=StringVar()
        self.var_contact=StringVar()
       
        




                #------search frame-------
        

#-----option----
        lbl_search=Label(self.root,text="Invoice No.",bg="white",font=("goudy old style",15))
        lbl_search.place(x=700,y=80)
        

        txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("goudy old style",15),bg='lightyellow').place(x=800,y=80,width=160)
        btn_search=Button(self.root,text="Search",font=("goudy old style",15),bg='#4caf50',fg="white",cursor="hand2").place(x=980,y=79,width=100,height=28)


      #------title-----
        title=Label(self.root,text="Supplier Details",font=("goudy old style",20,"bold"),bg="#0f4d7d",fg="white").place(x=50,y=10,width=1000,height=40)  



    #------content------
        #------row1--------
        lbl_supplier_invoice=Label(self.root,text="Invoice No",font=("goudy old style",15),bg="white").place(x=50,y=80)  
        txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("goudy old style",15),bg="white").place(x=180,y=80,width=180)  
        
        #-------row2--------
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=120)  
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg='lightyellow').place(x=180,y=120,width=180)  
        

    #-------row3-------------
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=50,y=160)  
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg='lightyellow').place(x=180,y=160,width=180)  
        
    #-------row4-------------
        lbl_description=Label(self.root,text="Description",font=("goudy old style",15),bg="white").place(x=50,y=200)  
        

        self.txt_description=Text(self.root,font=("goudy old style",15),bg='lightyellow')
        self.txt_description.place(x=180,y=200,width=470,height=120)  
        
    #----------button------
        btn_save=Button(self.root,text="Save",font=("goudy old style",15),bg='#2196f3',fg="white",cursor="hand2").place(x=180,y=370,width=110,height=35)
        btn_update=Button(self.root,text="Update",font=("goudy old style",15),bg='#4caf50',fg="white",cursor="hand2").place(x=300,y=370,width=110,height=35)
        btn_delete=Button(self.root,text="Delete",font=("goudy old style",15),bg='#f44336',fg="white",cursor="hand2").place(x=420,y=370,width=110,height=35)
        btn_clear=Button(self.root,text="Clear",font=("goudy old style",15),bg='#607d8b',fg="white",cursor="hand2").place(x=540,y=370,width=110,height=35)


    #-----Employee Details-----
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=700,y=120,width=380,height=350)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)


        self.supplierTable=ttk.Treeview(emp_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)
        self.supplierTable.heading("invoice",text="Invoice No")
        self.supplierTable.heading("name",text="Name")
        self.supplierTable.heading("contact",text="Contact")
        self.supplierTable.heading("desc",text="Description")
       
        self.supplierTable["show"]="headings"
       
        self.supplierTable.column("invoice",width=90)
        self.supplierTable.column("name",width=100)
        self.supplierTable.column("contact",width=100)
        self.supplierTable.column("desc",width=100)
       
        
        
        
        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
#---------------------------------------------------------------------------------------------


if __name__=="__main__":
    root=Tk()
    obj=supplierClass(root)
    root.mainloop()            