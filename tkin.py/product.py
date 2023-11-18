from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class productClass: 
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed by Struggling with bits")
        self.root.config(bg="white")
        self.root.focus_force()
#==========================================
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()

        #--------------------------------------
        product_Frame=Frame(self.root, bd=2, relief=RAISED, bg="cyan")
        product_Frame.place(x=10, y=10,width=450,height=480)

    #==========Title==========      
        title=Label(product_Frame,text="Manage Product Details",font=("monaco",20),bg="#0f4d7d",fg="Yellow").pack(side=TOP,fill=X)
 #-----column1----
        lbl_category=Label(product_Frame,text="Category",font=("goudy old style",20),bg="white").place(x=30,y=60)
        lbl_supplier=Label(product_Frame,text="Supplier",font=("goudy old style",20),bg="white").place(x=30,y=110)
        lbl_product_name=Label(product_Frame,text="Name",font=("goudy old style",20),bg="white").place(x=30,y=160)
        lbl_price=Label(product_Frame,text="Price",font=("goudy old style",20),bg="white").place(x=30,y=210)
        lbl_quantity=Label(product_Frame,text="Quantity",font=("goudy old style",20),bg="white").place(x=30,y=260)
        lbl_status=Label(product_Frame,text="Status",font=("goudy old style",20),bg="white").place(x=30,y=310)

    #-----column2----
        cmb_cat=ttk.Combobox(product_Frame,textvariable=self.var_cat,values=("Select"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_cat.place(x=150,y=60,width=200)
        cmb_cat.current(0)

        cmb_sup=ttk.Combobox(product_Frame,textvariable=self.var_sup,values=("Select"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_sup.place(x=150,y=110,width=200)
        cmb_sup.current(0)

        txt_name=Entry(product_Frame,textvariable=self.var_name,font=("goudy old style",15),bg='light green').place(x=150,y=160,width=200)
        txt_price=Entry(product_Frame,textvariable=self.var_price,font=("goudy old style",15),bg='light green').place(x=150,y=210,width=200)
        txt_qty=Entry(product_Frame,textvariable=self.var_qty,font=("goudy old style",15),bg='light green').place(x=150,y=260,width=200)
        
        cmb_status=ttk.Combobox(product_Frame,textvariable=self.var_status,values=("Active","Inactive"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_status.place(x=150,y=310,width=200)
        cmb_status.current(0)

#----------button------
        btn_save=Button(product_Frame,text="Save",command=self.add,font=("goudy old style",15),bg='#2196f3',fg="white",cursor="hand2").place(x=10,y=400,width=100,height=40)
        btn_update=Button(product_Frame,text="Update",font=("goudy old style",15),bg='#4caf50',fg="white",cursor="hand2").place(x=120,y=400,width=100,height=40)
        btn_delete=Button(product_Frame,text="Delete",font=("goudy old style",15),bg='#f44336',fg="white",cursor="hand2").place(x=230,y=400,width=100,height=40)
        btn_clear=Button(product_Frame,text="Clear",font=("goudy old style",15),bg='#607d8b',fg="white",cursor="hand2").place(x=340,y=400,width=100,height=40)
      
#------search frame-------
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=480,y=10,width=600,height=80)

#-----option----
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Category","Supplier","Name"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg='lightyellow').place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg='#4caf50',fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)

#-----Employee Details-----

        
        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=0,y=350,relwidth=1,height=150)

        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL)


        self.product_table=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)
        self.product_table.heading("eid",text="Emp ID")
        self.product_table.heading("name",text="Name")
        self.product_table.heading("email",text="Email")
        self.product_table.heading("gender",text="Gender")
        self.product_table.heading("contact",text="Contact")
        self.product_table.heading("dob",text="D.O.B")
        self.product_table.heading("doj",text="D.O.J")
        self.product_table.heading("pass",text="Password")
        self.product_table.heading("utype",text="User Type")
        self.product_table.heading("address",text="Address")
        self.product_table.heading("salary",text="Salary")
       
        self.product_table["show"]="headings"
       
        self.product_table.column("eid",width=90)
        self.product_table.column("name",width=100)
        self.product_table.column("email",width=100)
        self.product_table.column("gender",width=100)
        self.product_table.column("contact",width=100)
        self.product_table.column("dob",width=100)
        self.product_table.column("doj",width=100)
        self.product_table.column("pass",width=100)
        self.product_table.column("utype",width=100)
        self.product_table.column("address",width=100)
        self.product_table.column("salary",width=100)
        self.product_table.pack(fill=BOTH,expand=1)
        self.product_table.bind("<ButtonRelease-1>",self.get_data)

        self.show()
#==========================================================
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Must be required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Employee ID already assigned, try different",parent=self.root )
                else:
                    cur.execute("Insert into employee (eid,name,email,gender,contact,dob,doj,pass,utype,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                                                self.var_emp_id.get(),    #stringvar is taken for database mai koi error na aaye
                                                self.var_name.get(),
                                                self.var_email.get(),
                                                self.var_gender.get(),
                                                self.var_contact.get(),
                                                self.var_dob.get(),
                                                self.var_doj.get(),
                                                self.var_pass.get(),
                                                self.var_utype.get(),
                                                self.txt_address.get('1.0', END),
                                                self.var_salary.get(),
                                    
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee Addedd Successfully",parent= self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def show (self):
        con=sqlite3.connect (database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    def get_data(self,ev):
        f=self. EmployeeTable.focus ()
        content=(self.product_table.item (f)) 
        row=content [ 'values']
       # print (row)
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row [5])
        self.var_doj.set(row[6])
        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert (END,row[9])
        self.var_salary.set(row[10])
    
    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Must be required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root )
                else:
                    cur.execute("Update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=?",(
                                                self.var_name.get(),
                                                self.var_email.get(),
                                                self.var_gender.get(),
                                                self.var_contact.get(),
                                                self.var_dob.get(),
                                                self.var_doj.get(),
                                                self.var_pass.get(),
                                                self.var_utype.get(),
                                                self.txt_address.get('1.0', END),
                                                self.var_salary.get(),
                                                self.var_emp_id.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee Updated Successfully",parent= self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Must be required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root )
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Employee Deleted Successfully",parent=self.root)
                        self.clear()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self. var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("") 
        self.var_utype.set("Admin")
        self.txt_address.delete('1.0', END)
        self.var_salary.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()

    def search (self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search By option", parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
        
            else:
                cur.execute("select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self. EmployeeTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error","No record found!!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)





if __name__=="__main__":
    root=Tk()
    obj=productClass(root)
    root.mainloop()