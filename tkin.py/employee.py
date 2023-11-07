from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
class employeeClass:
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


        self.var_emp_id=StringVar()     #stringvar is taken for database mai koi error na aaye
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        




                #------search frame-------
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)

#-----option----
        cmb_search=ttk.Combobox(SearchFrame,values=("Select","Email","Name","Contact"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,font=("goudy old style",15),bg='lightyellow').place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",font=("goudy old style",15),bg='#4caf50',fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)


      #------title-----
        title=Label(self.root,text="Employee Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)  



    #------content------








if __name__=="__main__":
    root=Tk()
    obj=employeeClass(root)
    root.mainloop()            