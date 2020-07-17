from tkinter import *

shall = Tk()
shall.title("Loan calculator")
shall.geometry('539x388')
shall.resizable(0,0)

def calculate_instalment():
   r=(float(rate_interest.get())/100)/12
   p=float(loan_amt.get())
   n=float(nbr_installment.get())
   i=p*r*(1+r)**n /((1+r)**n-1)
   l4.config(text="Installment is : %8.2f" % (i))

#Frame for design & name of programmer.
dsgn_f=Frame(shall,borderwidth=2)
dsgn_f.config(bg='#4b0082')
dsgn_f.place(x=0,y=0,width=538.5,height=80)

#Frame for all attributes.
att_frame=Frame(shall,borderwidth=2,bg="black")
att_frame.place(x=0,y=82,width=538.5,height=303)

#Label of top
wel=Label(dsgn_f,text="Welcome To Shuaib Creation",font={"clibri",56,"bold"},fg="black")
wel.place(x=0,y=20,width=255,height=30)


#first row
abt=Label(att_frame,text="Loan Calculator Project",font=7,bg="black",fg="white")
abt.place(x=100,y=0,width=300,height=30)

#second row
loan_amt=Label(att_frame,text="Loan Ammount",font=5,bg="black",fg="white")
loan_amt.place(x=55,y=50,width=150,height=30)

#third row
nbr_installment=Label(att_frame,text="Number of Installments",font=5,bg="black",fg="white")
nbr_installment.place(x=70,y=90,width=170,height=30)

#fourth row
rate_interest=Label(att_frame,text="Rate of Interest",font=5,bg="black",fg="white")
rate_interest.place(x=55,y=130,width=150,height=30)

#first row of input field
loan_amt=Entry(shall,font={"Arial",5,'solid'})
loan_amt.place(x=280,y=140,width=200,height=25)

#second row of input field
nbr_installment=Entry(shall,font={"Arial",5,'bold'})
nbr_installment.place(x=280,y=180,width=200,height=25)

#third row of input field
rate_interest=Entry(shall,font=5)
rate_interest.place(x=280,y=220,width=200,height=25)


#button for check result
chk_btn=Button(att_frame,text="Check Installment",font=5,fg="black",bg="white",cursor="hand2",command=calculate_instalment)
chk_btn.place(x=100,y=200,width=150,height=30)

#button for exit screen
exit_btn=Button(att_frame,text="Exit",background="#EEEEEE",font=5,fg="black",bg="white",cursor="hand2",command=shall.destroy)
exit_btn.place(x=300,y=200,width=100,height=30)

#result Label
l4=Label(att_frame,text="Result will be soon",font=5,bg='white',fg="red")
l4.place(x=170,y=260,width=200,height=25)


shall.mainloop()