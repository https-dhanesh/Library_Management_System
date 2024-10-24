from tkinter import*
from tkinter import ttk
from datetime import datetime,timedelta
import mysql.connector
import tkinter
from tkinter import messagebox

class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Libray Management System") 
        self.root.geometry("1529x785+0+0")

        #-------------------------------variables------------------------------------------------------------------------------------------
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.first_name=StringVar()
        self.last_name=StringVar()
        self.address1=StringVar()
        self.address2=StringVar()
        self.postcode=StringVar()
        self.mobile_no=StringVar()
        self.book_id=StringVar()
        self.book_title=StringVar()
        self.author=StringVar()
        self.date_borrowed=StringVar()
        self.due_date=StringVar()
        self.days_on_book=StringVar()
        self.late_fine=StringVar()
        self.date_overdue=StringVar()
        self.actual_price=StringVar()

        lbltitle=Label(self.root,text="Library Management System",bg="powder blue",fg="green",bd=15,relief=RIDGE,font=("times new roman",40,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=105,width=1535,height=430)
        #-------------------------------------------------------------------------Dataframeleft-------------------------------------------------------------------------
        
        DataFrameLeft=LabelFrame(frame,text="Library Member Information",fg="green",bg="powder blue",bd=12,relief=RIDGE,font=("times new roman",15,"bold"))
        DataFrameLeft.place(x=0,y=5,width=820,height=390)

        lblMember=Label(DataFrameLeft,bg="powder blue",font=("times new roman",14,"bold"),text="Member Type",padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("times new roman",12,"bold"),width=29,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.grid(row=0,column=1)

        lblPRN_NO=Label(DataFrameLeft,bg="powder blue",text="PRN No",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblPRN_NO.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,textvariable=self.prn_var,font=("times new roman",12,"bold"),width=31)
        txtPRN_NO.grid(row=1,column=1)

        lblID=Label(DataFrameLeft,bg="powder blue",text="Member ID",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblID.grid(row=2,column=0,sticky=W)
        txtID=Entry(DataFrameLeft,textvariable=self.id_var,font=("times new roman",12,"bold"),width=31)
        txtID.grid(row=2,column=1)

        lblFirst_name=Label(DataFrameLeft,bg="powder blue",text="First Name",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblFirst_name.grid(row=3,column=0,sticky=W)
        txtFirst_name=Entry(DataFrameLeft,textvariable=self.first_name,font=("times new roman",12,"bold"),width=31)
        txtFirst_name.grid(row=3,column=1)

        lblLast_name=Label(DataFrameLeft,bg="powder blue",text="Last Name",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblLast_name.grid(row=4,column=0,sticky=W)
        txtLast_name=Entry(DataFrameLeft,textvariable=self.last_name,font=("times new roman",12,"bold"),width=31)
        txtLast_name.grid(row=4,column=1)

        lblAddress1=Label(DataFrameLeft,bg="powder blue",text="Address 1",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,textvariable=self.address1,font=("times new roman",12,"bold"),width=31)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameLeft,bg="powder blue",text="Address 2",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,textvariable=self.address2,font=("times new roman",12,"bold"),width=31)
        txtAddress2.grid(row=6,column=1)

        lblPost_Code=Label(DataFrameLeft,bg="powder blue",text="Post Code",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblPost_Code.grid(row=7,column=0,sticky=W)
        txtPost_Code=Entry(DataFrameLeft,textvariable=self.postcode,font=("times new roman",12,"bold"),width=31)
        txtPost_Code.grid(row=7,column=1)

        lblMob_no=Label(DataFrameLeft,bg="powder blue",text="Mobile No",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblMob_no.grid(row=8,column=0,sticky=W)
        txtMob_no=Entry(DataFrameLeft,textvariable=self.mobile_no,font=("times new roman",12,"bold"),width=31)
        txtMob_no.grid(row=8,column=1)

        lblBook_id=Label(DataFrameLeft,bg="powder blue",text="Book ID",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblBook_id.grid(row=0,column=2,sticky=W)
        txtBook_id=Entry(DataFrameLeft,textvariable=self.book_id,font=("times new roman",12,"bold"),width=31)
        txtBook_id.grid(row=0,column=3)

        lblBook_Title=Label(DataFrameLeft,bg="powder blue",text="Book Title",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblBook_Title.grid(row=1,column=2,sticky=W)
        txtBook_Title=Entry(DataFrameLeft,textvariable=self.book_title,font=("times new roman",12,"bold"),width=31)
        txtBook_Title.grid(row=1,column=3)

        lblAuthor_name=Label(DataFrameLeft,bg="powder blue",text="Author",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblAuthor_name.grid(row=2,column=2,sticky=W)
        txtAuthor_name=Entry(DataFrameLeft,textvariable=self.author,font=("times new roman",12,"bold"),width=31)
        txtAuthor_name.grid(row=2,column=3)

        lblDate_borrowed=Label(DataFrameLeft,bg="powder blue",text="Date Borrowed",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblDate_borrowed.grid(row=3,column=2,sticky=W)
        txtDate_borrowed=Entry(DataFrameLeft,textvariable=self.date_borrowed,font=("times new roman",12,"bold"),width=31)
        txtDate_borrowed.grid(row=3,column=3)

        lblDate_due=Label(DataFrameLeft,bg="powder blue",text="Due Date",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblDate_due.grid(row=4,column=2,sticky=W)
        txtDate_due=Entry(DataFrameLeft,textvariable=self.due_date,font=("times new roman",12,"bold"),width=31)
        txtDate_due.grid(row=4,column=3)

        lblDays_on_book=Label(DataFrameLeft,bg="powder blue",text="Days on Book",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblDays_on_book.grid(row=5,column=2,sticky=W)
        txtDays_on_book=Entry(DataFrameLeft,textvariable=self.days_on_book,font=("times new roman",12,"bold"),width=31)
        txtDays_on_book.grid(row=5,column=3)

        lblfine=Label(DataFrameLeft,bg="powder blue",text="Late Fine",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblfine.grid(row=6,column=2,sticky=W)
        txtfine=Entry(DataFrameLeft,textvariable=self.late_fine,font=("times new roman",12,"bold"),width=31)
        txtfine.grid(row=6,column=3)

        lbloverdue=Label(DataFrameLeft,bg="powder blue",text="Date Overdued",font=("times new roman",14,"bold"),padx=2,pady=6)
        lbloverdue.grid(row=7,column=2,sticky=W)
        txtoverdue=Entry(DataFrameLeft,textvariable=self.date_overdue,font=("times new roman",12,"bold"),width=31)
        txtoverdue.grid(row=7,column=3)

        lblprice=Label(DataFrameLeft,bg="powder blue",text="Actual Price",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblprice.grid(row=8,column=2,sticky=W)
        txtprice=Entry(DataFrameLeft,textvariable=self.actual_price,font=("times new roman",12,"bold"),width=31)
        txtprice.grid(row=8,column=3)

        #------------------------------------------------------------------------Data frame Right-------------------------------------------------------------------------

        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",15,"bold"))
        DataFrameRight.place(x=825,y=5,width=655,height=390)

        self.txtBox=Text(DataFrameRight,padx=2,pady=6,font=("times new roman",13,"bold"),width=42,height=17)
        self.txtBox.grid(row=0,column=2)

        listScrollBar=Scrollbar(DataFrameRight)
        listScrollBar.grid(row=0,column=1,sticky="ns")

        listBooks=['Head Firt Book','Learn Python The Hard Way','Python Programming','Hello Python','Python Cookbook','Intro to Machine Learning','Fluent Python','Machine techno','My Python',
                'The Algorithm','The technich Python','Joss Ellif guru','Elite Jungle Python','Mumbai Python','Pune Python','Machine Python','Advanced Python','Inton Python','RedChilli Python',
                'Guru of Python','Devlope Python'
                ]

        def SelectBook(event=""):
            cs=listBox.curselection()
            x=str(listBox.get(cs))
            if(x=='Head Firt Book'):
                self.book_id.set("BKID5454")
                self.book_title.set("Python Manual")
                self.author.set("Paul Berry")
                
                d1=datetime.now()
                d2=d1.date()
                d3=d2+\
                    timedelta(days=15)

                self.date_borrowed.set(d2)
                self.due_date.set(d3)
                self.days_on_book.set("15 days")
                self.late_fine.set("Rs.50")
                self.date_overdue.set("NO")
                self.actual_price.set("Rs.788")

            elif(x=='Learn Python The Hard Way'):
                self.book_id.set("BKID5454")
                self.book_title.set("Python Manual")
                self.author.set("Tom Holland")
                
                d1=datetime.now()
                d2=d1.date()
                d3=d2+\
                    timedelta(days=15)

                self.date_borrowed.set(d2)
                self.due_date.set(d3)
                self.days_on_book.set("15 days")
                self.late_fine.set("Rs.50")
                self.date_overdue.set("NO")
                self.actual_price.set("Rs.788")

            elif(x=='Python Programming'):
                self.book_id.set("BKID5584")
                self.book_title.set("Python Manual")
                self.author.set("Guido Van Rossum")
                
                d1=datetime.now()
                d2=d1.date()
                d3=d2+\
                    timedelta(days=15)

                self.date_borrowed.set(d2)
                self.due_date.set(d3)
                self.days_on_book.set("15 days")
                self.late_fine.set("Rs.50")
                self.date_overdue.set("NO")
                self.actual_price.set("Rs.900")
        
            elif(x=='Hello Python'):
                self.book_id.set("BKID7584")
                self.book_title.set("Do Python")
                self.author.set("D.D.Shingade")
                
                d1=datetime.now()
                d2=d1.date()
                d3=d2+\
                    timedelta(days=15)

                self.date_borrowed.set(d2)
                self.due_date.set(d3)
                self.days_on_book.set("15 days")
                self.late_fine.set("Rs.50")
                self.date_overdue.set("NO")
                self.actual_price.set("Rs.500")

            elif(x=='Python Cookbook'):
                self.book_id.set("BKID7884")
                self.book_title.set("Easy Python")
                self.author.set("S.V.Warule")
                
                d1=datetime.now()
                d2=d1.date()
                d3=d2+\
                    timedelta(days=15)

                self.date_borrowed.set(d2)
                self.due_date.set(d3)
                self.days_on_book.set("15 days")
                self.late_fine.set("Rs.50")
                self.date_overdue.set("NO")
                self.actual_price.set("Rs.700")

            elif(x=='Intro to Machine Learning'):
                self.book_id.set("BKID7554")
                self.book_title.set("The Steps")
                self.author.set("S.M.Ingle")
                
                d1=datetime.now()
                d2=d1.date()
                d3=d2+\
                    timedelta(days=15)

                self.date_borrowed.set(d2)
                self.due_date.set(d3)
                self.days_on_book.set("15 days")
                self.late_fine.set("Rs.50")
                self.date_overdue.set("NO")
                self.actual_price.set("Rs.600")

            elif(x=='Intro to Machine Learning'):
                self.book_id.set("BKID7354")
                self.book_title.set("The Machine")
                self.author.set("A.D.Kale")
                
                d1=datetime.now()
                d2=d1.date()
                d3=d2+\
                    timedelta(days=15)

                self.date_borrowed.set(d2)
                self.due_date.set(d3)
                self.days_on_book.set("15 days")
                self.late_fine.set("Rs.50")
                self.date_overdue.set("NO")
                self.actual_price.set("Rs.300")

            elif(x=='Fluent Python'):
                self.book_id.set("BKID9355")
                self.book_title.set("Python History")
                self.author.set("S.S.Suryawanshi")
                
                d1=datetime.now()
                d2=d1.date()
                d3=d2+\
                    timedelta(days=15)

                self.date_borrowed.set(d2)
                self.due_date.set(d3)
                self.days_on_book.set("15 days")
                self.late_fine.set("Rs.50")
                self.date_overdue.set("NO")
                self.actual_price.set("Rs.1000") 

            elif(x=='Machine techno'):
                self.book_id.set("BKID5355")
                self.book_title.set("The Machines")
                self.author.set("Tom Cruise")
                
                d1=datetime.now()
                d2=d1.date()
                d3=d2+\
                    timedelta(days=15)

                self.date_borrowed.set(d2)
                self.due_date.set(d3)
                self.days_on_book.set("15 days")
                self.late_fine.set("Rs.50")
                self.date_overdue.set("NO")
                self.actual_price.set("Rs.500") 

            elif(x=='My Python'):
                self.book_id.set("BKID5455")
                self.book_title.set("The Python")
                self.author.set("G.H.Sonar")
                
                d1=datetime.now()
                d2=d1.date()
                d3=d2+\
                    timedelta(days=15)

                self.date_borrowed.set(d2)
                self.due_date.set(d3)
                self.days_on_book.set("15 days")
                self.late_fine.set("Rs.50")
                self.date_overdue.set("NO")
                self.actual_price.set("Rs.600") 

            elif(x=='The Algorithm'):
                self.book_id.set("BKID9455")
                self.book_title.set("Step by Step")
                self.author.set("A.S.Deshmukh")
                
                d1=datetime.now()
                d2=d1.date()
                d3=d2+\
                    timedelta(days=15)

                self.date_borrowed.set(d2)
                self.due_date.set(d3)
                self.days_on_book.set("15 days")
                self.late_fine.set("Rs.50")
                self.date_overdue.set("NO")
                self.actual_price.set("Rs.400") 

            elif(x=='The technich Python'):
                self.book_id.set("BKID9465")
                self.book_title.set("Python")
                self.author.set("N.B.Panzade")
                
                d1=datetime.now()
                d2=d1.date()
                d3=d2+\
                    timedelta(days=15)

                self.date_borrowed.set(d2)
                self.due_date.set(d3)
                self.days_on_book.set("15 days")
                self.late_fine.set("Rs.50")
                self.date_overdue.set("NO")
                self.actual_price.set("Rs.450") 

            elif(x=='Joss Ellif guru'):
                self.book_id.set("BKID9475")
                self.book_title.set("Adison")
                self.author.set("A.S.Gore")
                
                d1=datetime.now()
                d2=d1.date()
                d3=d2+\
                    timedelta(days=15)

                self.date_borrowed.set(d2)
                self.due_date.set(d3)
                self.days_on_book.set("15 days")
                self.late_fine.set("Rs.50")
                self.date_overdue.set("NO")
                self.actual_price.set("Rs.550") 

            elif(x=='Elite Jungle Python'):
                self.book_id.set("BKID6475")
                self.book_title.set("Elite Python")
                self.author.set("D.G.Mante")
                
                d1=datetime.now()
                d2=d1.date()
                d3=d2+\
                    timedelta(days=15)

                self.date_borrowed.set(d2)
                self.due_date.set(d3)
                self.days_on_book.set("15 days")
                self.late_fine.set("Rs.50")
                self.date_overdue.set("NO")
                self.actual_price.set("Rs.650")

            elif(x=='Mumbai Python'):
                self.book_id.set("BKID7475")
                self.book_title.set("Start Python")
                self.author.set("M.D.More")
                
                d1=datetime.now()
                d2=d1.date()
                d3=d2+\
                    timedelta(days=15)

                self.date_borrowed.set(d2)
                self.due_date.set(d3)
                self.days_on_book.set("15 days")
                self.late_fine.set("Rs.50")
                self.date_overdue.set("NO")
                self.actual_price.set("Rs.750")

            elif(x=='Pune Python'):
                self.book_id.set("BKID7575")
                self.book_title.set("Python")
                self.author.set("P.A.Punekr")
                
                d1=datetime.now()
                d2=d1.date()
                d3=d2+\
                    timedelta(days=15)

                self.date_borrowed.set(d2)
                self.due_date.set(d3)
                self.days_on_book.set("15 days")
                self.late_fine.set("Rs.50")
                self.date_overdue.set("NO")
                self.actual_price.set("Rs.650")

            elif(x=='Inton Python'):
                self.book_id.set("BKID7665")
                self.book_title.set("Inton")
                self.author.set("T.R.Pole")
                
                d1=datetime.now()
                d2=d1.date()
                d3=d2+\
                    timedelta(days=15)

                self.date_borrowed.set(d2)
                self.due_date.set(d3)
                self.days_on_book.set("15 days")
                self.late_fine.set("Rs.50")
                self.date_overdue.set("NO")
                self.actual_price.set("Rs.450")

            elif(x=='Machine Python'):
                self.book_id.set("BKID7465")
                self.book_title.set("M Python")
                self.author.set("S.A.Wani")
                
                d1=datetime.now()
                d2=d1.date()
                d3=d2+\
                    timedelta(days=15)

                self.date_borrowed.set(d2)
                self.due_date.set(d3)
                self.days_on_book.set("15 days")
                self.late_fine.set("Rs.50")
                self.date_overdue.set("NO")
                self.actual_price.set("Rs.650")

            elif(x=='RedChilli Python'):
                self.book_id.set("BKID7465")
                self.book_title.set("RedChilli Python")
                self.author.set("T.W.Patil")
                
                d1=datetime.now()
                d2=d1.date()
                d3=d2+\
                    timedelta(days=15)

                self.date_borrowed.set(d2)
                self.due_date.set(d3)
                self.days_on_book.set("15 days")
                self.late_fine.set("Rs.50")
                self.date_overdue.set("NO")
                self.actual_price.set("Rs.650")

            elif(x=='Guru of Python'):
                self.book_id.set("BKID7065")
                self.book_title.set("Guru of Python")
                self.author.set("S.Sonone")
                
                d1=datetime.now()
                d2=d1.date()
                d3=d2+\
                    timedelta(days=15)

                self.date_borrowed.set(d2)
                self.due_date.set(d3)
                self.days_on_book.set("15 days")
                self.late_fine.set("Rs.50")
                self.date_overdue.set("NO")
                self.actual_price.set("Rs.650")

            elif(x=='Devlope Python'):
                self.book_id.set("BKID7265")
                self.book_title.set("Python Basics")
                self.author.set("S.h.More")
                
                d1=datetime.now()
                d2=d1.date()
                d3=d2+\
                    timedelta(days=15)

                self.date_borrowed.set(d2)
                self.due_date.set(d3)
                self.days_on_book.set("15 days")
                self.late_fine.set("Rs.50")
                self.date_overdue.set("NO")
                self.actual_price.set("Rs.650")

            elif(x=='Advanced Python'):
                self.book_id.set("BKID7235")
                self.book_title.set("The Python")
                self.author.set("T.S.Chopde")
                
                d1=datetime.now()
                d2=d1.date()
                d3=d2+\
                    timedelta(days=15)

                self.date_borrowed.set(d2)
                self.due_date.set(d3)
                self.days_on_book.set("15 days")
                self.late_fine.set("Rs.50")
                self.date_overdue.set("NO")
                self.actual_price.set("Rs.950")



        listBox=Listbox(DataFrameRight,font=("times new roman",13,"bold"),width=23,height=17)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollBar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)
        #-------------------------------------------------------------------------Buttons frame-------------------------------------------------------------------------
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1535,height=70)

        btnAddData=Button(Framebutton,command=self.add_data,text="Add Data",font=("times new roman",12,"bold"),width=26,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnshowData=Button(Framebutton,command=self.show_data,text="Show Data",font=("times new roman",12,"bold"),width=26,bg="blue",fg="white")
        btnshowData.grid(row=0,column=1)

        btnupdate=Button(Framebutton,command=self.update,text="Update",font=("times new roman",12,"bold"),width=26,bg="blue",fg="white")
        btnupdate.grid(row=0,column=2)

        btnDelete=Button(Framebutton,command=self.delete,text="Delete",font=("times new roman",12,"bold"),width=26,bg="blue",fg="white")
        btnDelete.grid(row=0,column=3)

        btnReset=Button(Framebutton,command=self.reset,text="Reset",font=("times new roman",12,"bold"),width=26,bg="blue",fg="white")
        btnReset.grid(row=0,column=4)

        btnExit=Button(Framebutton,command=self.iExit,text="Exit",font=("times new roman",12,"bold"),width=26,bg="blue",fg="white")
        btnExit.grid(row=0,column=5)

        #------------------------------------------------------------------------Information frame-------------------------------------------------------------------------
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=590,width=1535,height=205)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1465,height=179)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame,column=("Member type","PRN No","ID","First name","Last name","Address 1","Address 2","Post Code","Mobile No","Book id","Book title",
                                                       "Author","Data Borrowed","Due Date","Days on book","Late Return Fine","Date Overdue","Actual Price"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)


        self.library_table.heading("Member type",text="Member type")
        self.library_table.heading("PRN No",text="PRN No")
        self.library_table.heading("ID",text="ID")
        self.library_table.heading("First name",text="First name")
        self.library_table.heading("Last name",text="Last name")
        self.library_table.heading("Address 1",text="Address 1")
        self.library_table.heading("Address 2",text="Address 2")
        self.library_table.heading("Post Code",text="Post Code")
        self.library_table.heading("Mobile No",text="Mobile No")
        self.library_table.heading("Book id",text="Book id")
        self.library_table.heading("Book title",text="Book title")
        self.library_table.heading("Author",text="Author")
        self.library_table.heading("Data Borrowed",text="Data Borrowed")
        self.library_table.heading("Due Date",text="Due Date")
        self.library_table.heading("Days on book",text="Days on book")
        self.library_table.heading("Late Return Fine",text="Late Return Fine")
        self.library_table.heading("Date Overdue",text="Date Overdue")
        self.library_table.heading("Actual Price",text="Actual Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)


        self.library_table.column("Member type",width=100)
        self.library_table.column("PRN No",width=100)
        self.library_table.column("ID",width=100)
        self.library_table.column("First name",width=100)
        self.library_table.column("Last name",width=100)
        self.library_table.column("Address 1",width=100)
        self.library_table.column("Address 2",width=100)
        self.library_table.column("Post Code",width=100)
        self.library_table.column("Mobile No",width=100)
        self.library_table.column("Book id",width=100)
        self.library_table.column("Book title",width=100)
        self.library_table.column("Author",width=100)
        self.library_table.column("Data Borrowed",width=100)
        self.library_table.column("Due Date",width=100)
        self.library_table.column("Days on book",width=100)
        self.library_table.column("Late Return Fine",width=100)
        self.library_table.column("Date Overdue",width=100)
        self.library_table.column("Actual Price",width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Dhanesh@#56",database="dbms")
        my_cursor=conn.cursor()
        a=self.member_var.get()
        b=self.prn_var.get()
        c=self.id_var.get()
        d=self.first_name.get()
        e=self.last_name.get()
        f=self.address1.get()
        g=self.address2.get()
        h=self.postcode.get()
        i=self.mobile_no.get()
        j=self.book_id.get()
        k=self.book_title.get()
        l=self.author.get()
        m=self.date_borrowed.get()
        n=self.due_date.get()
        o=self.days_on_book.get()
        p=self.late_fine.get()
        q=self.date_overdue.get()
        r=self.actual_price.get()
        sql="insert into dbms.library VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)";
        val=(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r)
        my_cursor.execute(sql,val)
                                                                                                
        conn.commit()
        self.fetch_data()
        messagebox.showinfo("Success","Member has been inserted successfully")
        conn.close()

    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Dhanesh@#56",database="dbms")
        my_cursor=conn.cursor()
        a=self.member_var.get()
        b=self.prn_var.get()
        c=self.id_var.get()
        d=self.first_name.get()
        e=self.last_name.get()
        f=self.address1.get()
        g=self.address2.get()
        h=self.postcode.get()
        i=self.mobile_no.get()
        j=self.book_id.get()
        k=self.book_title.get()
        l=self.author.get()
        m=self.date_borrowed.get()
        n=self.due_date.get()
        o=self.days_on_book.get()
        p=self.late_fine.get()
        q=self.date_overdue.get()
        r=self.actual_price.get()
        sql="update dbms.library set Member_Type=%s,ID=%s,First_Name=%s,Last_Name=%s,Address_1=%s,Address_2=%s,Post_Code=%s,Mobile_No=%s,Book_ID=%s,Book_Title=%s,Author=%s,Date_Borrowed=%s,Due_Date=%s,Days_on_Book=%s,Late_Fine=%s,Date_overdue=%s,Actual_Price=%s where PRN_No=%s";
        val=(a,c,d,e,f,g,h,i,j,k,l,m,n,o,q,r,p,b)
        my_cursor.execute(sql,val)
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success","Member has been updated")

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Dhanesh@#56",database="dbms")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from dbms.library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.first_name.set(row[3]),
        self.last_name.set(row[4]),
        self.address1.set(row[5]),
        self.address2.set(row[6]),
        self.postcode.set(row[7]),
        self.mobile_no.set(row[8]),
        self.book_id.set(row[9]),
        self.book_title.set(row[10]),
        self.author.set(row[11]),
        self.date_borrowed.set(row[12]),
        self.due_date.set(row[13]),
        self.days_on_book.set(row[14]),
        self.late_fine.set(row[15]),
        self.date_overdue.set(row[16]),
        self.actual_price.set(row[17])

    def show_data(self):
        self.txtBox.insert(END,"Member Type\t\t"+self.member_var.get()+"\n")
        self.txtBox.insert(END,"PRN No\t\t"+self.prn_var.get()+"\n")     
        self.txtBox.insert(END,"Member ID\t\t"+self.id_var.get()+"\n")
        self.txtBox.insert(END,"First Name\t\t"+self.first_name.get()+"\n")
        self.txtBox.insert(END,"Last Name\t\t"+self.last_name.get()+"\n")
        self.txtBox.insert(END,"Address 1\t\t"+self.address1.get()+"\n")
        self.txtBox.insert(END,"Address 2\t\t"+self.address2.get()+"\n")
        self.txtBox.insert(END,"Post Code\t\t"+self.postcode.get()+"\n")
        self.txtBox.insert(END,"Mobile No\t\t"+self.mobile_no.get()+"\n")
        self.txtBox.insert(END,"Book ID\t\t"+self.book_id.get()+"\n")
        self.txtBox.insert(END,"Book Ttile\t\t"+self.book_title.get()+"\n")
        self.txtBox.insert(END,"Author\t\t"+self.author.get()+"\n")
        self.txtBox.insert(END,"Date Borrowed\t\t"+self.date_borrowed.get()+"\n")
        self.txtBox.insert(END,"Due Date\t\t"+self.due_date.get()+"\n")
        self.txtBox.insert(END,"Days on Book\t\t"+self.days_on_book.get()+"\n")
        self.txtBox.insert(END,"Late Fine\t\t"+self.late_fine.get()+"\n")
        self.txtBox.insert(END,"Date Overdue\t\t"+self.date_overdue.get()+"\n")
        self.txtBox.insert(END,"Actual Price\t\t"+self.actual_price.get()+"\n")

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.first_name.set(""),
        self.last_name.set(""),
        self.address1.set(""),
        self.address2.set(""),
        self.postcode.set(""),
        self.mobile_no.set(""),
        self.book_id.set(""),
        self.book_title.set(""),
        self.author.set(""),
        self.date_borrowed.set(""),
        self.due_date.set(""),
        self.days_on_book.set(""),
        self.late_fine.set(""),
        self.date_overdue.set(""),
        self.actual_price.set("")
        self.txtBox.delete("1.0",END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return
            
    def delete(self):
        if self.prn_var.get()=="" or self.id_var=="":
            messagebox.showerror("Error","First Select the Member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Dhanesh@#56",database="dbms")
            my_cursor=conn.cursor()
            query=" delete from dbms.library where (PRN_No = %s) and (ID = %s)";
            value=(self.prn_var.get(),self.id_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Member has been deleted")

if __name__=="__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()        
