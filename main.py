from tkinter import *
from tkinter import messagebox
import math,random,os
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="black"
        title=Label(self.root,text="CAFE BILLING SYSTEM",bd=12,relief=GROOVE,bg=bg_color,fg="yellow",font=("arial",30,"bold"),pady=2).pack(fill=X)
        #=============Variables======================
        
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.loshan=IntVar()    
        self.rice=IntVar()
        self.food_oil=IntVar() 
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        self.maza=IntVar()
        self.cock=IntVar()
        self.frooti=IntVar()
        self.thumbsup=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()
        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()
        #=============Customer Detail================
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("arial",15,"bold"),fg="yellow",bg=bg_color)
        F1.place(x=0,y=90,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",fg="white",bg=bg_color,font=("arial",14,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=11,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        
        cphn_lbl=Label(F1,text="Phone No.",fg="white",bg=bg_color,font=("arial",14,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=11,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)
        
        cbill_lbl=Label(F1,text="Bill Number",fg="white",bg=bg_color,font=("arial",14,"bold")).grid(row=0,column=4,padx=20,pady=5)
        cbill_txt=Entry(F1,width=11,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)
        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=50,pady=10)

        
        
        #=============cold drink================
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="cold drinks",font=("arial",15,"bold"),fg="yellow",bg=bg_color)
        F2.place(x=3,y=205,width=325,height=380)
        bath_lbl=Label(F2,text="mazza",font=("arial",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("arial",12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=8,pady=10)

        face_crm_lbl=Label(F2,text="fruiti",font=("arial",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_crm_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("arial",12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=8,pady=10)

        face_w_lbl=Label(F2,text="7up",font=("arial",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_w_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("arial",12,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=8,pady=10)
        
        hair_s_lbl=Label(F2,text="limca",font=("arial",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hair_s_txt=Entry(F2,width=10,textvariable=self.spray,font=("arial",12,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=8,pady=10)
        
        hair_gel_lbl=Label(F2,text="coca cola",font=("arial",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_gel_txt=Entry(F2,width=10,textvariable=self.gell,font=("arial",12,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=8,pady=10)

        body_lbl=Label(F2,text="thumbs up",font=("arial",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_txt=Entry(F2,width=10,textvariable=self.loshan,font=("arial",12,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #=============hot drink================
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="hot drinks",font=("arial",15,"bold"),fg="yellow",bg=bg_color)
        F3.place(x=320,y=205,width=285,height=380)
        g1_lbl=Label(F3,text="tea",font=("arial",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F3,width=10,textvariable=self.rice,font=("arial",12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=8,pady=10)

        g2_lbl=Label(F3,text="coffee",font=("arial",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("arial",12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=8,pady=10)

        g3_lbl=Label(F3,text="green tea",font=("arial",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt=Entry(F3,width=10,textvariable=self.daal,font=("arial",12,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=8,pady=10)
        
        g4_lbl=Label(F3,text="leamon tea",font=("arial",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F3,width=10,textvariable=self.wheat,font=("arial",12,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=8,pady=10)
        
        g5_lbl=Label(F3,text="non sugar tea",font=("arial",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt=Entry(F3,width=10,textvariable=self.sugar,font=("arial",12,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=8,pady=10)

        g6_lbl=Label(F3,text="non sugar coffee",font=("arial",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F3,width=10,textvariable=self.tea,font=("arial",12,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #=============snacks================
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="snacks",font=("arial",15,"bold"),fg="yellow",bg=bg_color)
        F4.place(x=600,y=205,width=300,height=380)
        c1_lbl=Label(F4,text="cookies",font=("arial",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(F4,width=10,textvariable=self.maza,font=("arial",12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=8,pady=10)

        c2_lbl=Label(F4,text="pizza",font=("arial",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F4,width=10,textvariable=self.cock,font=("arial",12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=8,pady=10)

        c3_lbl=Label(F4,text="burger",font=("arial",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt=Entry(F4,width=10,textvariable=self.frooti,font=("arial",12,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=8,pady=10)
        
        c4_lbl=Label(F4,text="sandwich",font=("arial",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt=Entry(F4,width=10,textvariable=self.thumbsup,font=("arial",12,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=8,pady=10)
        
        c5_lbl=Label(F4,text="butter sandwich",font=("arial",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt=Entry(F4,width=10,textvariable=self.limca,font=("arial",12,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=8,pady=10)

        c6_lbl=Label(F4,text="jam sandwich",font=("arial",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt=Entry(F4,width=10,textvariable=self.sprite,font=("arial",12,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        
        #=============Bill Area Frame================
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=905,y=205,width=440,height=350)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #=============Button Frame================
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("arial",15,"bold"),fg="yellow",bg=bg_color)
        F6.place(x=3,y=560,relwidth=1,height=140)
        m1_lbl=Label(F6,text="Total cold drink Price",bg=bg_color,fg="white",font=("arial",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=15,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text="Total hot drink Price",bg=bg_color,fg="white",font=("arial",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=15,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl=Label(F6,text="Total snacks Price",bg=bg_color,fg="white",font=("arial",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=15,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        c1_lbl=Label(F6,text="cold drink Tax",bg=bg_color,fg="white",font=("arial",14,"bold")).grid(row=0,column=3,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=15,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=4,padx=10,pady=1)

        c2_lbl=Label(F6,text="hot drink Tax",bg=bg_color,fg="white",font=("arial",14,"bold")).grid(row=1,column=3,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=15,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=4,padx=10,pady=1)

        c3_lbl=Label(F6,text="snacks Tax",bg=bg_color,fg="white",font=("arial",14,"bold")).grid(row=2,column=3,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=15,textvariable=self.cold_drink_tax,font=("arial",10,"bold"),bd=7,relief=SUNKEN).grid(row=2,column=4,padx=10,pady=1)
        btn_f=Frame(F6,bd=7,relief=GROOVE)
        btn_f.place(x=820,width=510,height=180)
        total_btn=Button(btn_f,text="Total",command=self.total,bg="black",fg="white",pady=10,width=10,bd=4,font="arial 10 bold").grid(row=0,column=0,padx=5,pady=5)
        gbill_btn=Button(btn_f,command=self.bill_area,text="Generate Bill",bg="black",fg="white",pady=10,width=10,bd=4,font="arial 10 bold").grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(btn_f,text="Clear",command=self.clear_data,bg="black",fg="white",pady=10,width=10,bd=4,font="arial 10 bold").grid(row=0,column=2,padx=5,pady=5)
        exit_btn=Button(btn_f,text="Exit",command=self.Exit_app,bg="black",fg="white",pady=10,width=10,bd=4,font="arial 10 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()
    def total(self):
        self.c_s_p=self.soap.get()*10
        self.c_fc_p=self.face_cream.get()*10
        self.c_fw_p=self.face_wash.get()*10
        self.c_spr_p=self.spray.get()*10
        self.c_g_p=self.gell.get()*10
        self.c_l_p=self.loshan.get()*10
        self.total_cosmatic_price=float(
                                    self.c_s_p+
                                    self.c_fc_p+
                                    self.c_fw_p+
                                    self.c_spr_p+
                                    self.c_g_p+
                                    self.c_l_p
                                  )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmatic_price))
        self.c_tax=round(self.total_cosmatic_price*0.05,2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))
        self.g_r_p=self.rice.get()*10
        self.g_fo_p=self.food_oil.get()*10
        self.g_w_p=self.wheat.get()*20
        self.g_d_p=self.daal.get()*10
        self.g_s_p=self.sugar.get()*16
        self.g_t_p=self.tea.get()*15
        self.total_grocery_price=float(
                                    self.g_r_p+
                                    self.g_fo_p+
                                    self.g_w_p+
                                    self.g_d_p+
                                    self.g_s_p+
                                    self.g_t_p
                                  )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round(self.total_grocery_price*0.1,2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))
        self.cd_m_p=self.maza.get()*30
        self.cd_c_p=self.cock.get()*50
        self.cd_f_p=self.frooti.get()*40
        self.cd_th_p=self.thumbsup.get()*35
        self.cd_l_p=self.limca.get()*15
        self.cd_s_p=self.sprite.get()*15
        self.total_cold_drink_price=float(
                                    self.cd_m_p+
                                    self.cd_c_p+
                                    self.cd_f_p+
                                    self.cd_th_p+
                                    self.cd_l_p+
                                    self.cd_s_p
                                   )
        self.cold_drink_price.set("Rs. "+str(self.total_cold_drink_price))
        self.cd_tax=round(self.total_cold_drink_price*0.05,2)
        self.cold_drink_tax.set("Rs. "+str(self.cd_tax))
        self.total_bill=float(
            self.total_cosmatic_price+
            self.total_grocery_price+
            self.total_cold_drink_price+
            self.c_tax+
            self.g_tax+
            self.cd_tax
        )
    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\t Welcome TO GENARAL Retail")
        self.textarea.insert(END,f"\n Bill Number :{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name :{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number :{self.c_phon.get()}")
        
        self.textarea.insert(END,f"\n======================================")
        self.textarea.insert(END,f"\n Product\t\tQTY\t\tPrice")
        self.textarea.insert(END,f"\n======================================")
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer Details are Required")
        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","No Product Selected")
        else:
            self.welcome_bill()
            #===cosmatics=====
            if self.soap.get()!=0:
                self.textarea.insert(END,f"\n mazza\t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.face_cream.get()!=0:
                self.textarea.insert(END,f"\n fruti\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
            if self.face_wash.get()!=0:
                self.textarea.insert(END,f"\n 7 up\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
            if self.spray.get()!=0:
                self.textarea.insert(END,f"\n limca\t\t{self.spray.get()}\t\t{self.c_s_p}")
            if self.gell.get()!=0:
                self.textarea.insert(END,f"\n coca cola \t\t{self.gell.get()}\t\t{self.c_g_p}")
            if self.loshan.get()!=0:
                self.textarea.insert(END,f"\n thumbs up\t\t{self.loshan.get()}\t\t{self.c_l_p}")
            #===Grocery=====
            if self.rice.get()!=0:
                self.textarea.insert(END,f"\n tea  \t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.food_oil.get()!=0:
                self.textarea.insert(END,f"\n coffee\t\t{self.food_oil.get()}\t\t{self.g_fo_p}")
            if self.daal.get()!=0:
                self.textarea.insert(END,f"\n green tea \t\t{self.daal.get()}\t\t{self.g_d_p}")
            if self.wheat.get()!=0:
                self.textarea.insert(END,f"\n leamon tea  \t\t{self.wheat.get()}\t\t{self.g_w_p}")
            if self.sugar.get()!=0:
                self.textarea.insert(END,f"\n n-tea  \t\t{self.sugar.get()}\t\t{self.g_s_p}")
            if self.tea.get()!=0:
                self.textarea.insert(END,f"\n n-coffee \t\t{self.tea.get()}\t\t{self.g_t_p}")
            
            #===Cold Drink=====
            if self.maza.get()!=0:
                self.textarea.insert(END,f"\n cookies   \t\t{self.maza.get()}\t\t{self.cd_m_p}")
            if self.cock.get()!=0:
                self.textarea.insert(END,f"\n pizza   \t\t{self.cock.get()}\t\t{self.cd_c_p}")
            if self.frooti.get()!=0:
                self.textarea.insert(END,f"\n burger  \t\t{self.frooti.get()}\t\t{self.cd_f_p}")
            if self.thumbsup.get()!=0:
                self.textarea.insert(END,f"\n sandwich\t\t{self.thumbsup.get()}\t\t{self.cd_th_p}")
            if self.limca.get()!=0:
                self.textarea.insert(END,f"\n b-sandwich\t\t{self.limca.get()}\t\t{self.cd_l_p}")
            if self.sprite.get()!=0:
                self.textarea.insert(END,f"\n j-sandwich  \t\t{self.sprite.get()}\t\t{self.cd_s_p}")
            self.textarea.insert(END,f"\n--------------------------------------")
            if self.cosmetic_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n cold drinkTax \t\t\t{self.cosmetic_tax.get()}")
            
            if self.grocery_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n hot drink Tax \t\t\t{self.grocery_tax.get()}")
                
            if self.cold_drink_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n snacks Tax \t\t\t{self.cold_drink_tax.get()}")
                self.textarea.insert(END,f"\n Total Bill\t\t\t Rs. {self.total_bill}")
                self.textarea.insert(END,f"\n---------------------------------------")
            self.save_bill()
    def save_bill(self):
        #wb = load_workbook('F:\\Codes\\BillGenerator\\excel.xlsx')
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:
            self.bill_data=self.textarea.get('1.0',END)
            f1=open("c:\\project\\bill_app\\invoice\\"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. :{self.bill_no.get()} saved successfull")
        else:
            return
    def find_bill(self):
        present="no"
        for i in os.listdir("c:\\project\\bill_app\\invoice\\"):
            if i.split(".")[0]==self.search_bill.get():
                f1=open(f"c:\\project\\bill_app\\invoice\\{i}","r")
                self.textarea.delete('1.0',END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No")
    def clear_data(self):
        op=messagebox.askyesno("clear","Do you want to Reset Entries?")
        if op>0:
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.loshan.set(0)          
            self.rice.set(0)
            self.food_oil.set(0) 
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)          
            self.maza.set(0)
            self.cock.set(0)
            self.frooti.set(0)
            self.thumbsup.set(0)
            self.limca.set(0)
            self.sprite.set(0)
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")
            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")
            self.c_name.set("")
            self.c_phon.set("")
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()
    def Exit_app(self):
            self.root.destroy()





root=Tk()
obj=Bill_App(root)

root.mainloop()

