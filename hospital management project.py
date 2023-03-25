from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector



class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1550x800+0+0")

        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvise=StringVar()
        self.BloodPressure=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()



        lbltitle= Label(self.root,text="+HOSPITAL MANAGEMENT SYSTEM", bg= "white", fg="red",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

       

         # ===================================== Data frame Left   =========================================


        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)


        DataFrameLeft=LabelFrame(frame,text="Patient Information", bg= "powder blue", fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lblMember=Label(DataFrameLeft,text="Names of Tablets",bg= "powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.Nameoftablets,font=("times new roman",12,"bold"),width=27,state="readonly")
        comMember["values"]=("Nice","Corona Virus","Acetaminophen","Adderall","Amlodiphine","Activan")
        comMember.grid(row=0,column=1)

        lblref=Label(DataFrameLeft,text="Reference No",bg= "powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataFrameLeft,textvariable=self.ref,font=("times new roman",12,"bold"),width=29)
        txtref.grid(row=1,column=1)

        
        lblDose=Label(DataFrameLeft,text="Dose",bg= "powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataFrameLeft,textvariable=self.Dose,font=("times new roman",12,"bold"),width=29)
        txtDose.grid(row=2,column=1)

        
        lblNoOfTablets=Label(DataFrameLeft,text="No Of Tablets",bg= "powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNoOfTablets.grid(row=3,column=0,sticky=W)
        txtNoOfTablets=Entry(DataFrameLeft,textvariable=self.NumberofTablets,font=("times new roman",12,"bold"),width=29)
        txtNoOfTablets.grid(row=3,column=1)

     


        lblLot=Label(DataFrameLeft,text="Lot",bg= "powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataFrameLeft,textvariable=self.Lot,font=("times new roman",12,"bold"),width=29)
        txtLot.grid(row=4,column=1)

        lblissueDate=Label(DataFrameLeft,text="Issue Date",bg= "powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(DataFrameLeft,textvariable=self.Issuedate,font=("times new roman",12,"bold"),width=29)
        txtissueDate.grid(row=5,column=1)


        lblExpDate=Label(DataFrameLeft,text="Exp Date",bg= "powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataFrameLeft,textvariable=self.ExpDate,font=("times new roman",12,"bold"),width=29)
        txtExpDate.grid(row=6,column=1)


        lblDailyDose=Label(DataFrameLeft,text="Daily Dose",bg= "powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataFrameLeft,textvariable=self.DailyDose,font=("times new roman",12,"bold"),width=29)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(DataFrameLeft,text="Side Effect",bg= "powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataFrameLeft,textvariable=self.sideEffect,font=("times new roman",12,"bold"),width=29)
        txtSideEffect.grid(row=8,column=1)

        lblFurtherinfo=Label(DataFrameLeft,text="Further Information",bg= "powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo=Entry(DataFrameLeft,textvariable=self.FurtherInformation,font=("times new roman",12,"bold"),width=29)
        txtFurtherinfo.grid(row=0,column=3)


        lblBloodPressure=Label(DataFrameLeft,text="Blood Pressure",bg= "powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(DataFrameLeft,textvariable=self.BloodPressure,font=("times new roman",12,"bold"),width=29)
        txtBloodPressure.grid(row=1,column=3)


        lblStorage=Label(DataFrameLeft,text="Storage Advise",bg= "powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataFrameLeft,textvariable=self.StorageAdvise,font=("times new roman",12,"bold"),width=29)
        txtStorage.grid(row=2,column=3)


        lblMedicine=Label(DataFrameLeft,text="Medication",bg= "powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataFrameLeft,textvariable=self.HowToUseMedication,font=("times new roman",12,"bold"),width=29)
        txtMedicine.grid(row=3,column=3)


        lblPatientId=Label(DataFrameLeft,text="Patient Id",bg= "powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(DataFrameLeft,textvariable=self.PatientId,font=("times new roman",12,"bold"),width=29)
        txtPatientId.grid(row=4,column=3)

        lblNhsNumber=Label(DataFrameLeft,text="NHS Number",bg= "powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(DataFrameLeft,textvariable=self.nhsNumber,font=("times new roman",12,"bold"),width=29)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientName=Label(DataFrameLeft,text="Patient Name",bg= "powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W)
        txtPatientName=Entry(DataFrameLeft,textvariable=self.PatientName,font=("times new roman",12,"bold"),width=29)
        txtPatientName.grid(row=6,column=3)

        lblDateOfBirth=Label(DataFrameLeft,text="Date Of birth",bg= "powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth=Entry(DataFrameLeft,textvariable=self.DateOfBirth,font=("times new roman",12,"bold"),width=29)
        txtDateOfBirth.grid(row=7,column=3)

        lblPatientAddress=Label(DataFrameLeft,text="Patient Address",bg= "powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(DataFrameLeft,textvariable=self.PatientAddress,font=("times new roman",12,"bold"),width=29)
        txtPatientAddress.grid(row=8,column=3)




         # ===================================== Data frame Right  =========================================

        DataFrameRight=LabelFrame(frame,text="Prescription", bg= "powder blue",bd=12,padx=20,relief=RIDGE,font=("arial",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)

        self.txtPrescription=Text(DataFrameRight,font=("arial",12,"bold"),width=46,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)  


        # =====================================Button frame =========================================

        FrameButton=LabelFrame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameButton.place(x=0,y=530,width=1530,height=70)

        btnPrescription=Button(FrameButton,command=self.iPrescriptionData,text="Prescription Data", bg= "green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData=Button(FrameButton,command=self.iprescription,text="Prescription", bg= "green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate=Button(FrameButton,command=self.update_data,text="update", bg= "green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(FrameButton,command=self.idelete,text="Delete", bg= "green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(FrameButton,command=self.clear,text="Clear", bg= "green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnClear.grid(row=0,column=4)

        btnExit=Button(FrameButton,command=self.iexit ,text="Exit", bg= "green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnExit.grid(row=0,column=5)

         # =====================================information frame =========================================

        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=600,width=1530,height=195)

        # ======================================Scroll Bar  ==========================================

        scroll_x=ttk.Scrollbar(FrameDetails,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(FrameDetails,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(FrameDetails,columns=("nameoftablets","ref","dose","nooftablets","lot","issuedate","expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftablets",text="Name of Table")
        self.hospital_table.heading("ref",text="Referece No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No Of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")

        self.hospital_table["show"]="headings"

       


        self.hospital_table.column("nameoftablets",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)
        
        self.hospital_table.pack(fill=BOTH,expand=1)

        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()



        #===============================Functionality Declaration============================================

    def iPrescriptionData(self):
        if self.Nameoftablets.get()=="" or self.ref.get()=="" :
            messagebox.showerror("Error","All Field Are Required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="Mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    
                                                                                                    self.Nameoftablets.get(),
                                                                                                    self.ref.get(),
                                                                                                    self.Dose.get(),
                                                                                                    self.NumberofTablets.get(),
                                                                                                    self.Lot.get(),
                                                                                                    self.Issuedate.get(),
                                                                                                    self.ExpDate.get(),
                                                                                                    self.DailyDose.get(),
                                                                                                    self.StorageAdvise.get(),
                                                                                                    self.nhsNumber.get(),
                                                                                                    self.PatientName.get(),
                                                                                                    self.DateOfBirth.get(),
                                                                                                    self.PatientAddress.get()
                                                                                                    
                                                                                                    ) )
            conn.commit()
            self.fetch_data()
            conn.close()

            messagebox.showinfo("Success","Member Has Been Inserted Successfully")

    def update_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="Mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update hospital set Nameoftablets=%s, dose=%s, Numbersoftablets=%s, lot=%s, issuedate=%s, expdate=%s, dailydose=%s, storage=%s, nhsnumber=%s, patientname=%s, DOB=%s, patientaddress=%s where  Reference_No=%s",(

                                                                                                    self.Nameoftablets.get(),
                                                                                                    self.Dose.get(),
                                                                                                    self.NumberofTablets.get(),
                                                                                                    self.Lot.get(),
                                                                                                    self.Issuedate.get(),
                                                                                                    self.ExpDate.get(),
                                                                                                    self.DailyDose.get(),
                                                                                                    self.StorageAdvise.get(),
                                                                                                    self.nhsNumber.get(),
                                                                                                    self.PatientName.get(),
                                                                                                    self.DateOfBirth.get(),
                                                                                                    self.PatientAddress.get(),
                                                                                                    self.ref.get()
        ))


        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success","Member Has Been updated Successfully")

        



    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="Mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
        conn.commit()
        conn.close()



    def get_cursor(self,event=""):
        cursor_rows=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_rows)
        row=content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvise.set(row[8])
        self.nhsNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])


    def iprescription(self):
        self.txtPrescription.insert(END,"Name Of Tablets: \t\t\t"+self.Nameoftablets.get()+"\n")
        self.txtPrescription.insert(END,"Reference No:\t\t\t"+self.ref.get()+"\n")
        self.txtPrescription.insert(END,"Dose: \t\t\t"+self.Dose.get()+"\n")
        self.txtPrescription.insert(END,"Number Of Tablets:\t\t\t"+self.NumberofTablets.get()+"\n")
        self.txtPrescription.insert(END,"Lot:\t\t\t"+self.Lot.get()+"\n")
        self.txtPrescription.insert(END,"Issue Date:\t\t\t"+self.Issuedate.get()+"\n")
        self.txtPrescription.insert(END,"Exp date:\t\t\t"+self.ExpDate.get()+"\n")
        self.txtPrescription.insert(END,"Daily Dose:\t\t\t"+self.DailyDose.get()+"\n")
        self.txtPrescription.insert(END,"Side Effect: \t\t\t"+self.sideEffect.get()+"\n")
        self.txtPrescription.insert(END,"Further Information: \t\t\t"+self.FurtherInformation.get()+"\n")
        self.txtPrescription.insert(END,"StorageAdvise:\t\t\t"+self.StorageAdvise.get()+"\n")
        self.txtPrescription.insert(END,"Blood Pressure: \t\t\t"+self.BloodPressure.get()+"\n")
        self.txtPrescription.insert(END,"Patient Id: \t\t\t"+self.PatientId.get()+"\n")
        self.txtPrescription.insert(END,"NHS Number: \t\t\t"+self.nhsNumber.get()+"\n")
        self.txtPrescription.insert(END,"Patient Name: \t\t\t"+self.PatientName.get()+"\n")
        self.txtPrescription.insert(END,"DOB: \t\t\t"+self.DateOfBirth.get()+"\n")
        self.txtPrescription.insert(END,"Patient address: \t\t\t"+self.PatientAddress.get()+"\n")
        


    def idelete(self):
        if self.ref.get()=="":
            messagebox.showerror("Error","First Select the Member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="Mydata")
            my_cursor=conn.cursor()
            query="delete from hospital where Reference_No=%s"
            value=(self.ref.get())
            my_cursor.execute(query,(value,))

            conn.commit()
            self.fetch_data()
            self.clear()
            conn.close()
            
            messagebox.showinfo("Delete","Member Has Been deleted Successfully")

    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.sideEffect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvise.set("")
        self.BloodPressure.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0",END)


    def iexit(self):
        iexit=messagebox.askyesno("Hospital Management System","confirm you want to exit")
        if iexit>0:
            root.destroy()
            return















if __name__ == "__main__":
    root=Tk()
    obj=Hospital(root)
    root.mainloop()
