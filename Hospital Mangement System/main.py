#importing some important dependices
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


#make class for hospital main window
class Hospital:
   #constructor for self call when object created....
   def __init__(self , root2):
    self.root = root2
    self.root.title("Hospital Management System")
    self.root.geometry("1280x800+0+0") 

    self.Nameoftablets= StringVar() 
    self.ref= StringVar() 
    self.Dose= StringVar() 
    self.NumberofTablets= StringVar() 
    self.Lot= StringVar() 
    self.Issuedate= StringVar() 
    self.ExpDate= StringVar()  
    self.DailyDose= StringVar() 
    self.sideEffect= StringVar() 
    self.FurthurInformation= StringVar() 
    self.StorageAdvice= StringVar() 
    self.BloodPressure= StringVar() 
    self.Medication= StringVar() 
    self.PatientId= StringVar()  
    self.nhsNumber= StringVar() 
    self.PatientName= StringVar()  
    self.DateOFBirth= StringVar() 
    self.PatientAddress= StringVar()
        
         #============================Label==========================
        
    lbltitle = Label(self.root,bd=20,relief=RIDGE,text="+ Hospital Management System",fg="red",bg="white",font=("times new roman",50,"bold"))
    lbltitle.pack(side=TOP,fill=X)    
        
         #============================Dataframe==========================
        
    Dataframe = Frame(self.root,bd=20,relief=RIDGE)
    Dataframe.place(x=0,y=130,width=1280,height=400)
    DataFrameLeft = LabelFrame(Dataframe,bd=5,relief=RIDGE,padx=10,font=("times new roman",20,"bold"),text="Patient Information")
    DataFrameLeft.place(x=10,y=5,width=900,height=350)
    DataFrameRight = LabelFrame(Dataframe,bd=5,relief=RIDGE,padx=10,font=("times new roman",20,"bold"),text="Prescription")
    DataFrameRight.place(x=920,y=5,width=300,height=350)
        
        
        #============================Button frame==========================
        
    Buttonframe = Frame(self.root,bd=20,relief=RIDGE)
    Buttonframe.place(x=0,y=530,width=1280,height=70)
       
         #============================Details frame==========================
        
    Detailsframe = Frame(self.root,bd=20,relief=RIDGE)
    Detailsframe.place(x=0,y=600,width=1280,height=130)
         #============================= Data frame Left=========================
           
    lblNametablet = Label(DataFrameLeft,font=("arial",12,"bold"),text="Names of Tablet",padx=2,pady=6)
    lblNametablet.grid(row=0,column=0,sticky=W)
        
    comNametablet = ttk.Combobox(DataFrameLeft,state="readonly",textvariable=self.Nameoftablets,font=("arial",12,"bold"),width=28)
    comNametablet["values"]= ("Panadol","Panadol extra","Brufen","Flygil","Omerazol","Panadol syrup","Berberine","Biotin","Bromelain","Calcium","Chlorella")
    comNametablet.current(0)
    comNametablet.grid(row=0,column=1)
        
        
    lblref = Label(DataFrameLeft,font=("arial",12,"bold"),text="Reference No:",padx=2)
    lblref.grid(row=1,column=0,sticky=W)
    txtref= Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.ref,width=30)
    txtref.grid(row=1,column=1)
        
    lblDose = Label(DataFrameLeft,font=("arial",12,"bold"),text="Dose:",padx=2,pady=4)
    lblDose.grid(row=2,column=0,sticky=W)
    txtDose = Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.Dose,width=30)
    txtDose.grid(row=2,column=1)
        
        
    lblNoOftablets = Label(DataFrameLeft,font=("arial",12,"bold"),text="No Of Tablets::",padx=2,pady=6)
    lblNoOftablets.grid(row=3,column=0,sticky=W)
    txtNoOftablets = Entry(DataFrameLeft,font=("arial",13,"bold"),width=30,textvariable=self.NumberofTablets)
    txtNoOftablets.grid(row=3,column=1)
        
    lblLot = Label(DataFrameLeft,font=("arial",12,"bold"),text="Lot:",padx=2,pady=6)
    lblLot.grid(row=4,column=0,sticky=W)
    txtLot = Entry(DataFrameLeft,font=("arial",13,"bold"),width=30,textvariable=self.Lot)
    txtLot.grid(row=4,column=1)
        
    lblissueDate = Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
    lblissueDate.grid(row=5,column=0,sticky=W)
    txtissueDate = Entry(DataFrameLeft,font=("arial",13,"bold"),width=30,textvariable=self.Issuedate)
    txtissueDate.grid(row=5,column=1)
        
    lblExpDate = Label(DataFrameLeft,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=6)
    lblExpDate.grid(row=6,column=0,sticky=W)
    txtExpDate = Entry(DataFrameLeft,font=("arial",13,"bold"),width=30,textvariable=self.ExpDate)
    txtExpDate.grid(row=6,column=1)
        
    lblDailyDose = Label(DataFrameLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=4)
    lblDailyDose.grid(row=7,column=0,sticky=W)
    txtDailyDose = Entry(DataFrameLeft,font=("arial",13,"bold"),width=30,textvariable=self.DailyDose)
    txtDailyDose.grid(row=7,column=1)
        
    lblSideEffect = Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
    lblSideEffect.grid(row=8,column=0,sticky=W)
    txtSideEffect = Entry(DataFrameLeft,font=("arial",13,"bold"),width=30,textvariable=self.sideEffect)
    txtSideEffect.grid(row=8,column=1)
        
    lblFurtherinfo = Label(DataFrameLeft,font=("arial",12,"bold"),text="Further Information:",padx=2)
    lblFurtherinfo.grid(row=0,column=2,sticky=W)
    txtFurtherinfo = Entry(DataFrameLeft,font=("arial",12,"bold"),width=30,textvariable=self.FurthurInformation)
    txtFurtherinfo.grid(row=0,column=3)
    lblBloodPressure = Label(DataFrameLeft,font=("arial",12,"bold"),text="Blood Pressure:",padx=2,pady=6)
    lblBloodPressure.grid(row=1,column=2,sticky=W)
    txtBloodPressure = Entry(DataFrameLeft,font=("arial",12,"bold"),width=30,textvariable=self.BloodPressure)
    txtBloodPressure.grid(row=1,column=3)
         
    lblStorage = Label(DataFrameLeft,font=("arial",12,"bold"),text="Storage Advice:",padx=2,pady=6)
    lblStorage.grid(row=2,column=2,sticky=W)
    txtStorage = Entry(DataFrameLeft,font=("arial",12,"bold"),width=30,textvariable=self.StorageAdvice)
    txtStorage.grid(row=2,column=3)
  
    lblMedicine = Label(DataFrameLeft,font=("arial",12,"bold"),text="Medication:",padx=2,pady=6)
    lblMedicine.grid(row=3,column=2,sticky=W)
    txtMedicine = Entry(DataFrameLeft,font=("arial",12,"bold"),width=30,textvariable=self.Medication)
    txtMedicine.grid(row=3,column=3,sticky=W)
  
    lblPatientId = Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Id:",padx=2,pady=6)
    lblPatientId.grid(row=4,column=2,sticky=W)
    txtPatientId = Entry(DataFrameLeft,font=("arial",12,"bold"),width=30,textvariable=self.PatientId)
    txtPatientId.grid(row=4,column=3)
  
    lblNhsNumber = Label(DataFrameLeft,font=("arial",12,"bold"),text="NHS Number:",padx=2,pady=6)
    lblNhsNumber.grid(row=5,column=2,sticky=W)
    txtNhsNumber = Entry(DataFrameLeft,font=("arial",12,"bold"),width=30,textvariable=self.nhsNumber)
    txtNhsNumber.grid(row=5,column=3)
        
    lblPatientname = Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Name:",padx=2,pady=6)
    lblPatientname.grid(row=6,column=2,sticky=W)
    txtPatientname = Entry(DataFrameLeft,font=("arial",12,"bold"),width=30,textvariable=self.PatientName)
    txtPatientname.grid(row=6,column=3)
  
  
    lblDateOfBirth = Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Of Birth:",padx=2,pady=6)
    lblDateOfBirth.grid(row=7,column=2,sticky=W)
    txtDateOfBirth = Entry(DataFrameLeft,font=("arial",12,"bold"),width=30,textvariable=self.DateOFBirth)
    txtDateOfBirth.grid(row=7,column=3)
  
    lblPatientAddress = Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Address:",padx=2,pady=6)
    lblPatientAddress.grid(row=8,column=2,sticky=W)
    txtPatientAddress = Entry(DataFrameLeft,font=("arial",12,"bold"),width=30,textvariable=self.PatientAddress)
    txtPatientAddress.grid(row=8,column=3)
        
         #============================= Data frame Right=========================
        
    self.txtPrescription = Text(DataFrameRight,font=("arial",12,"bold"),width=29,height=15.2,padx=2,pady=6)
    self.txtPrescription.grid(row=0,column=0)
        
         #============================ Buttons ==========================
    btnPrescription = Button(Buttonframe,text="Prescription",bg="green",fg="white",font=("arial",12,"bold"),width=18,padx=2,pady=6,command=self.Prescription)
    btnPrescription.grid(row=0,column=0) 
  
    btnPrescriptionData = Button(Buttonframe,text="Prescription Data",bg="green",fg="white",font=("arial",12,"bold"),width=18,padx=2,pady=6,command=self.iprescriptionData)
    btnPrescriptionData.grid(row=0,column=1) 
  
    btnUpdate = Button(Buttonframe,text="Update",bg="green",fg="white",font=("arial",12,"bold"),width=18,padx=2,pady=6,command=self.Update_Record,)
    btnUpdate.grid(row=0,column=2) 
  
    btnDelete = Button(Buttonframe,text="Delete",bg="green",fg="white",font=("arial",12,"bold"),width=18,padx=2,pady=6,command=self.Delete_Record)
    btnDelete.grid(row=0,column=3) 
  
    btnClear = Button(Buttonframe,text="Clear",bg="green",fg="white",font=("arial",12,"bold"),width=18,padx=2,pady=6,command=self.clear_Data)
    btnClear.grid(row=0,column=4) 
  
    btnExit = Button(Buttonframe,text="Exit",bg="green",fg="white",font=("arial",12,"bold"),width=18,padx=2,pady=6,command=self.App_Exit)
    btnExit.grid(row=0,column=5) 
        
         #=============================  Table  ==============================
         #============================= Scroll bar ===========================
    self.HT_Xscrollbar = Scrollbar(Detailsframe,orient='horizontal')
    self.HT_Yscrollbar = Scrollbar(Detailsframe)
    self.HT_Xscrollbar.pack(side=BOTTOM,fill=X)
    self.HT_Yscrollbar.pack(side=RIGHT,fill=Y)

    self.hospital_table = ttk.Treeview(Detailsframe,columns=("ref","nameoftablets","dose","nooftablets","lot","issuedate",
    "expdate","dailydose","storage","nhsnumber","patientname","dob","address"),xscrollcommand=self.HT_Xscrollbar.set,yscrollcommand=self.HT_Yscrollbar.set)
  
    #configure the scrollbar
    self.HT_Xscrollbar.config(command=self.hospital_table.xview)
    self.HT_Yscrollbar.config(command=self.hospital_table.yview)

    
    self.hospital_table.column("ref",width=100)
    self.hospital_table.column("nameoftablets",width=100)
    self.hospital_table.column("dose",width=100)
    self.hospital_table.column("nooftablets",width=100)
    self.hospital_table.column("lot",width=100)
    self.hospital_table.column("issuedate",width=100)
    self.hospital_table.column("expdate",width=100)
    self.hospital_table.column("dailydose",width=100)
    self.hospital_table.column("storage",width=100)
    self.hospital_table.column("nhsnumber",width=100)
    self.hospital_table.column("patientname",width=100)
    self.hospital_table.column("dob",width=100)
    self.hospital_table.column("address",width=100)
    
    self.hospital_table.heading("ref",text="Reference No.")
    self.hospital_table.heading("nameoftablets",text="Name Of Tablets")
    self.hospital_table.heading("dose",text="Dose")
    self.hospital_table.heading("nooftablets",text="No Of Tablets")
    self.hospital_table.heading("lot",text="Lot")
    self.hospital_table.heading("issuedate",text="Issue Date")
    self.hospital_table.heading("expdate",text="Exp Date")
    self.hospital_table.heading("dailydose",text="Daily Dose")
    self.hospital_table.heading("storage",text="Storage")
    self.hospital_table.heading("nhsnumber",text="NHS Number")
    self.hospital_table.heading("patientname",text="Patient Name")
    self.hospital_table.heading("dob",text="DOB")
    self.hospital_table.heading("address",text="Address")
  
    self.hospital_table["show"]= "headings"

  
    
    self.hospital_table.pack(fill=BOTH,expand=1)
    self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)

    self.fatch_data()    


 #==============Functionality declaration=====================

   def iprescriptionData(self):
    if(self.Nameoftablets.get()==''or self.ref.get()==''):
       messagebox.showerror("Error","All fields are required..")
    else:
       conn = mysql.connector.connect(host="localhost",username="root",password='',database='hms_py')
       my_cursor = conn.cursor()
       my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                          (
                              self.ref.get(),
                              self.Nameoftablets.get(),
                              self.Dose .get(),
                              self.NumberofTablets.get(),
                              self.Lot.get(),
                              self.Issuedate.get(),
                              self.ExpDate.get(),
                              self.DailyDose.get(),
                              self.StorageAdvice.get(),
                              self.nhsNumber.get(),
                              self.PatientName.get(),
                              self.DateOFBirth.get(),
                              self.PatientAddress.get()
                           )) 
         
       conn.commit()
       self.fatch_data()
       conn.close()
       messagebox.showinfo("Success","Data inserted Successfully")
   def Update_Record(self):
       conn = mysql.connector.connect(host="localhost",username="root",password='',database='hms_py')
       my_cursor = conn.cursor()
       my_cursor.execute("Update hospital set NameOfTablet=%s,Dose=%s,NumbersOfTablets=%s,LOT=%s,IssueDate=%s,ExpDate=%s,DailyDose=%s,Storage=%s,NHSNumber=%s,PatientName=%s,DOB=%s,PatientAdress=%s where Reference_NO=%s"
                         ,(

                              
                              self.Nameoftablets.get(),
                              self.Dose .get(),
                              self.NumberofTablets.get(),
                              self.Lot.get(),
                              self.Issuedate.get(),
                              self.ExpDate.get(),
                              self.DailyDose.get(),
                              self.StorageAdvice.get(),
                              self.nhsNumber.get(),
                              self.PatientName.get(),
                              self.DateOFBirth.get(),
                              self.PatientAddress.get(),
                              self.ref.get()
                         
                         ))
       conn.commit()
       self.fatch_data()
       conn.close()
   
   def fatch_data(self):
       conn = mysql.connector.connect(host="localhost",username="root",password='',database='hms_py')
       my_cursor = conn.cursor()
       my_cursor.execute("select * from hospital")
       rows = my_cursor.fetchall()
       if len(rows)!=0:
          self.hospital_table.delete(*self.hospital_table.get_children())
          count=0
          for i in rows:
              self.hospital_table.insert(parent="",index='end',iid=count,text="parent",values=i)
              count+=1
       conn.commit()
       conn.close()
       
   def get_cursor(self,event=""):
       cursor_row = self.hospital_table.focus()
       content = self.hospital_table.item(cursor_row)
       row = content["values"]
       self.ref.set(row[0])
       self.Nameoftablets.set(row[1])
       self.Dose.set(row[2])
       self.NumberofTablets.set(row[3])
       self.Lot.set(row[4])
       self.Issuedate.set(row[5])
       self.ExpDate.set(row[6])
       self.DailyDose.set(row[7])
       self.StorageAdvice.set(row[8])
       self.nhsNumber.set(row[9])
       self.PatientName.set(row[10])
       self.DateOFBirth.set(row[11])
       self.PatientAddress.set(row[12])
   def Prescription(self):
      self.txtPrescription.insert(END,"Reference No.\t:\t"+self.ref.get()+"\n")
      self.txtPrescription.insert(END,"PatientName\t:\t"+self.PatientName.get()+"\n")
      self.txtPrescription.insert(END,"PatientId\t:\t"+self.PatientId.get()+"\n")
      self.txtPrescription.insert(END,"PatientAddress\t:\t"+self.PatientAddress.get()+"\n")
      self.txtPrescription.insert(END,"DateOFBirth\t:\t"+self.DateOFBirth.get()+"\n")
      self.txtPrescription.insert(END,"BloodPressure\t:\t"+self.BloodPressure.get()+"\n")
      self.txtPrescription.insert(END,"Name of tablets\t:\t"+self.Nameoftablets.get()+"\n")
      self.txtPrescription.insert(END,"Dose\t:\t"+self.Dose.get()+"\n")
      self.txtPrescription.insert(END,"No. of tablets\t:\t"+self.NumberofTablets.get()+"\n")
      self.txtPrescription.insert(END,"LOT\t:\t"+self.Lot.get()+"\n")
      self.txtPrescription.insert(END,"Issue date\t:\t"+self.Issuedate.get()+"\n")
      self.txtPrescription.insert(END,"Expiry date\t:\t"+ self.ExpDate.get()+"\n")
      self.txtPrescription.insert(END,"DailyDose\t:\t"+self.DailyDose.get()+"\n")
      self.txtPrescription.insert(END,"StorageAdvice\t:\t"+self.StorageAdvice.get()+"\n")
      self.txtPrescription.insert(END,"nhsNumber\t:\t"+self.nhsNumber.get()+"\n")
      self.txtPrescription.insert(END,"sideEffect\t:\t"+self.sideEffect.get()+"\n")
      self.txtPrescription.insert(END,"FurthurInformation\t:\t"+self.FurthurInformation.get()+"\n")
      self.txtPrescription.insert(END,"StorageAdvice\t:\t"+self.StorageAdvice.get()+"\n")
      self.txtPrescription.insert(END,"Medication\t:\t"+self.Medication.get()+"\n")

   def Delete_Record(self):
       conn = mysql.connector.connect(host="localhost",username="root",password='',database='hms_py')
       my_cursor = conn.cursor()
       Del_rec_Q = "Delete from hospital where Reference_NO=%s"
       value = (self.ref.get(),)
       my_cursor.execute(Del_rec_Q,value)
       conn.commit()
       conn.close()
       self.fatch_data()
       messagebox.showinfo("Delete","Patient record deleted successfully..")
       
   def clear_Data(self):
       self.Nameoftablets.set("")
       self.ref.set("")
       self.Dose.set("")
       self.NumberofTablets.set("")
       self.Lot.set("")
       self.Issuedate.set("") 
       self.ExpDate.set("")
       self.DailyDose.set("")
       self.sideEffect.set("")
       self.FurthurInformation.set("")
       self.StorageAdvice.set("") 
       self.BloodPressure.set("") 
       self.Medication.set("") 
       self.PatientId.set("")  
       self.nhsNumber.set("")
       self.PatientName.set("") 
       self.DateOFBirth.set("") 
       self.PatientAddress.set("")
       self.txtPrescription.delete("1.0",END)
   def App_Exit(self):
      Exit_Mgs = messagebox.askyesno("Hospital Management System","Confirm you want to exit")
      if Exit_Mgs:
        self.root.destroy()
        return
      
root = Tk()
ob = Hospital(root)
root.mainloop()
