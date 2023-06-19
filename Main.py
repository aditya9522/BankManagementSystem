from tkinter import *
from tkinter.simpledialog import askstring
from tkinter import messagebox
import time
import cx_Oracle
from datetime import datetime
import mysql.connector

nowd = datetime.now()
cdate = nowd.strftime("%d-%m-%y")
ctime = nowd.strftime("%H:%M:%S")

root = Tk()
frame = Frame(root,bg="gray",borderwidth=15,highlightbackground="black",highlightthickness=2)
frame.pack(side=LEFT,fill="y")
current = DoubleVar()
pino = StringVar()
pino.set("aditya")

def account_list():
    connection = mysql.connector.connect(host = "127.0.0.1", user = "root", passwd = "aditya", database = "bank_system" )
    cursor = connection.cursor()
    cursor.execute("select account from useraccount_details")
    data = cursor.fetchall()
    cursor.close()
    connection.close()

    accList = []
    for list in data:
        for ele in list:
            accList.append(ele)

    return accList

# def acc(win,fn_temp,fn_ok):
#     ac = StringVar()
#     accn = Entry(win, textvariable=ac,justify="center",width=32,fg="black", bg="white", font=("arial", 15, 'bold'),)
#     accn.insert(0,"Click to enter account number")
#     accn.bind("<FocusIn>",fn_temp)
#     accn.place(x=160, y=150)       
#     errorl = Label(win, text="", font=('arial', 12, 'bold'), bg="aqua")
#     errorl.place(x=190, y=180)
#     ok = Button(win, text="OK", width=10, fg="white", font=('vardana', 15, 'bold'), bg="orange",command=fn_ok)
#     ok.place(x=270, y=300)

def historyb():
    his = Toplevel()
    his.geometry("700x600")
    his.title("History")
    his.configure(bg="steel blue")
    top = Label(his, text="History", fg="red",width=20, bg="pink", font=("arial", 20, 'bold')).pack(side=TOP)
    info = Label(his,text="Transaction Details ➡️", fg="purple", bg="aqua", font=("vardana", 15, 'bold'))
    info.place(x=40,y=80)

    def temp(e):
        accn.delete(0,"end")

    def OK():
        if (ac.get()).isnumeric():
            accn.destroy()
            errorl.destroy()
            ok.destroy()
            youracc = Label(his,text="Your Account Number : ", fg="green", bg="aqua", font=("vardana", 15, 'bold'))
            youracc.place(x=130,y=80)
            youracce = Label(his,text=ac.get(), fg="black", bg="aqua", font=("vardana", 15, 'bold'))
            youracce.place(x=370,y=80)
            info.place(x=40,y=130)
            con = cx_Oracle.connect("system/adp@localhost/xepdb1")
            cursor = con.cursor()
            cursor.execute("select * from atm_data")
            data = cursor.fetchall()
            lst = ["Date","Time","Withdrawals","Deposites","Balance"]
            n = 70
            for i in lst:
                lstd = Label(his,text=i, fg="green",width=9, bg="pink", font=("vardana", 15,"bold")).place(x=n,y=180)
                n = n+120

            a = 70
            b = 212
            for i in data:
                for j in i:
                    data = Label(his,text=j, bg="white",width=9, fg="steel blue", font=("vardana", 15,"bold")).place(x=a,y=b)
                    a = a+120
                b = b+32
                a = 70
            con.commit()
            cursor.close()
            con.close() 

        elif (ac.get() == None) or (ac.get() == ""):
            errorl.config(text="Please, Enter user account number!",fg="red")
        elif ac.get() == "Click to enter account number":
            errorl.config(text="Click above text to enter Acc number",fg="blue")
        else:
            print(ac.get())
            errorl.config(text="Did not match with any user acc !",fg="red")


    ac = StringVar()
    accn = Entry(his, textvariable=ac,justify="center",width=32,fg="black", bg="white", font=("arial", 15, 'bold'),)
    accn.insert(0,"Click to enter account number")
    accn.bind("<FocusIn>",temp)
    accn.place(x=160, y=150)       
    errorl = Label(his, text="", font=('arial', 12, 'bold'), bg="aqua")
    errorl.place(x=190, y=180)
    ok = Button(his, text="OK", width=10, fg="white", font=('vardana', 15, 'bold'), bg="orange",command=OK)
    ok.place(x=270, y=300)

    his.mainloop()

def aboutb():
    ab = Toplevel()
    ab.geometry("700x450")
    ab.title("About")
    ab.configure(bg="aqua")
    top = Label(ab, text="About", fg="red", bg="aqua", font=("arial", 20, 'bold')).pack(side=TOP)
    left = Label(ab,text="Bank Description ➡️", fg="purple", bg="aqua", font=("vardana", 18, 'bold')).place(x=40,y=80)
    data = """               The Sagar Bank is a system. And it is designed by a team, 
              contain three members as named as Ajay patel, Ajay 
              patel and aditya patel. The main goal of this system is to
              make easy transaction for the end user.By this user can easily
              interact with the system because we have provided a very 
              interactive and user friendly interface for the user and also
              provides consistency,durability & atomacity of the transaction,
              So the user will feel good experience with the system.
              Thak-You """
    lab1 = Label(ab, text=data, fg="black",bg="aqua", font=("arial", 15)).place(x=20,y=110)
    l2 = Label(ab,text="Technology used ➡️", fg="purple", bg="aqua", font=("vardana", 15, 'bold')).place(x=40,y=330)
    l2 = Label(ab,text="* Python Programming\n* Tkinter\n* Oracle DataBase(/SQL) ", fg="black", bg="aqua", font=("airal", 15)).place(x=200,y=360)

    ab.mainloop()

def curb():
    con = cx_Oracle.connect("system/adp@localhost/xepdb1")
    cursor = con.cursor()
    cursor.execute("select current_balance from atm_data")
    dt = cursor.fetchall()
    avb = dt[-1][0]
    current.set(avb)
    con.commit()
    con.close()

def balance():
    bal = Toplevel()
    bal.geometry("500x400")
    bal.title("Balance Check")
    bal.configure(bg="aqua")
    current_bal = DoubleVar()
    curb()

    def show():
        if (ac.get()).isnumeric():
            lb = Entry(bal, text=current_bal,bd=0 ,width=20, fg="purple", font=('vardana', 15, 'bold'), bg="aqua").place(x=300, y=280)
            b =  "{}/-".format(current.get())
            current_bal.set(b)
            accshow = Label(bal, text=ac.get(), fg="black", font=('ariel', 15, 'bold'), bg="aqua").place(x=300, y=170)
            errorl.config(text="User account detected",fg="green")
            errorl.place(x=170, y=120)

        elif (ac.get() == None) or (ac.get() == ""):
            errorl.config(text="Please, Enter user account number!",fg="red")
        elif ac.get() == "Click to enter account number":
            errorl.config(text="Click above text to enter Acc number",fg="blue")
        else:
            print(ac.get())
            errorl.config(text="Did not match with any user acc !",fg="red")

    def temp(e):
        accn.delete(0,"end")
        
    ac = StringVar()
    top = Label(bal, text="Check Balance", fg="red", bg="aqua", font=("arial", 20, 'bold'), pady=10).pack(side=TOP)
    accn = Entry(bal, textvariable=ac,justify="center",width=32,fg="black", bg="white", font=("arial", 15, 'bold'),)
    accn.insert(0,"Click to enter account number")
    accn.bind("<FocusIn>",temp)
    accn.place(x=80, y=90)       
    errorl = Label(bal, text=" ", font=('arial', 12, 'bold'), bg="aqua")
    errorl.place(x=120, y=120)
    balance1 = Label(bal, text="User Account Number :", fg="green", font=('ariel', 15, 'bold'), bg="aqua").place(x=75, y=170)
    balance = Button(bal, text="Balance", width=10, fg="white", font=('ariel', 15, 'bold'), bg="blue", command=show).place(x=180, y=220)
    lab1 = Label(bal, text="Available amount :     ₹", fg="green",bg="aqua", font=("arial", 15, 'bold')).place(x=80, y=280)
    bal.mainloop()


def exit():
    root.destroy()

def deposite():
    dep = Toplevel()
    dep.geometry("600x400")
    dep.title("Deposite")
    dep.configure(bg="aqua")
    deposite_amount = DoubleVar()
    ac = StringVar()

    def submit():
        if (deposite_amount.get()).is_integer and deposite_amount.get() > 0.0:
            curb()
            now = current.get() + deposite_amount.get()
            con = cx_Oracle.connect("system/adp@localhost/xepdb1")
            cursor = con.cursor()
            depa = deposite_amount.get()
            cursor.execute("insert into atm_data values(&tdate,&ttime,0.0,&deposites,&current_balance)",(cdate,ctime,depa,now))
            con.commit()
            con.close()
            text = "₹{}/- successfully deposited \nIn Acc number : 986038450335".format(deposite_amount.get())
            messagebox.showinfo("Information", text)
            dep.destroy()
        elif deposite_amount.get() == 0.0:
            dep.destroy()
            messagebox.showwarning("Warning","Enter valid amount")

    def temp(e):
        accn.delete(0,"end")

    def OK():
        if (ac.get()).isnumeric():
            accn.destroy()
            errorl.destroy()
            ok.destroy()

            lbl = Label(dep, text="Enter amount :", font=('arial', 15, 'bold'), fg="blue", bg="aqua").place(x=110, y=150)
            entry = Entry(dep,textvariable=deposite_amount, width=20, fg="green", font=('arial', 15, 'bold'), bg="white").place(x=280, y=150)
            error2 = Label(dep, text="", font=('arial', 12, 'bold'), bg="aqua")
            error2.place(x=140, y=180)
            btn = Button(dep, text="submit", width=10, fg="white", font=('vardana', 15, 'bold'), bg="orange", command=submit).place(x=220, y=300)

        elif (ac.get() == None) or (ac.get() == ""):
            errorl.config(text="Please, Enter user account number!",fg="red")
        elif ac.get() == "Click to enter account number":
            errorl.config(text="Click above text to enter Acc number",fg="blue")
        else:
            print(ac.get())
            errorl.config(text="Did not match with any user acc !",fg="red")



    top = Label(dep, text="Deposite Money", fg="red", bg="aqua",font=("arial", 20, 'bold'), pady=10).pack(side=TOP)
    accn = Entry(dep, textvariable=ac,justify="center",width=32,fg="black", bg="white", font=("arial", 15, 'bold'),)
    accn.insert(0,"Click to enter account number")
    accn.bind("<FocusIn>",temp)
    accn.place(x=110, y=150)       
    errorl = Label(dep, text="", font=('arial', 12, 'bold'), bg="aqua")
    errorl.place(x=140, y=180)
    ok = Button(dep, text="OK", width=10, fg="white", font=('vardana', 15, 'bold'), bg="orange", command=OK)
    ok.place(x=220, y=300)
    
    dep.mainloop()

def withdraw():
    withd = Toplevel()
    withd.geometry("600x400")
    withd.title("Withdraw")
    withd.configure(bg="aqua")
    withdraw_amount = DoubleVar()
    ac = StringVar()

    def submit2():
        if withdraw_amount.get() > current.get():
            withd.destroy()
            messagebox.showerror("Invalid Operation","You have not sufficient amount, Please Try Again!")
        elif withdraw_amount.get() == 0.0 or withdraw_amount.get().is_integer == False :
            withd.destroy()
            messagebox.showwarning("Warning","Enter valid amount")
        else:     
            curb()
            now = current.get() - withdraw_amount.get()
            con = cx_Oracle.connect("system/adp@localhost/xepdb1")
            cursor = con.cursor()
            witha = withdraw_amount.get()
            cursor.execute("insert into atm_data values(&tdate,&ttime,&withdrawals,0.0,&current_balance)",(cdate,ctime,witha,now))
            con.commit()
            con.close()
            txt = "₹{}/-  successfully Withdraw\nFrom Acc Number : 743938503925".format(withdraw_amount.get())
            messagebox.showinfo("Information", txt)
            
            withd.destroy()

    def temp(e):
            accn.delete(0,"end")

    def OK():
        if (ac.get()).isnumeric():
            accn.destroy()
            errorl.destroy()
            ok.destroy()

            lbl = Label(withd, text="Enter amount :", font=('arial', 15, 'bold'), fg="blue", bg="aqua").place(x=110, y=150)
            entry = Entry(withd,textvariable=withdraw_amount, width=20, fg="green", font=('arial', 15, 'bold'), bg="white").place(x=280, y=150)
            error2 = Label(withd, text="", font=('arial', 12, 'bold'), bg="aqua")
            error2.place(x=140, y=180)
            btn = Button(withd, text="submit", width=10, fg="white", font=('vardana', 15, 'bold'), bg="orange", command=submit2).place(x=220, y=300)
        elif (ac.get() == None) or (ac.get() == ""):
            errorl.config(text="Please, Enter user account number!",fg="red")
        elif ac.get() == "Click to enter account number":
            errorl.config(text="Click above text to enter Acc number",fg="blue")
        else:
            print(ac.get())
            errorl.config(text="Did not match with any user acc !",fg="red")

    top = Label(withd, text="Withdraw Money", fg="red", bg="aqua",font=("arial", 20, 'bold'), pady=10).pack(side=TOP)
    accn = Entry(withd, textvariable=ac,justify="center",width=32,fg="black", bg="white", font=("arial", 15, 'bold'),)
    accn.insert(0,"Click to enter account number")
    accn.bind("<FocusIn>",temp)
    accn.place(x=110, y=150)       
    errorl = Label(withd, text="", font=('arial', 12, 'bold'), bg="aqua")
    errorl.place(x=140, y=180)
    ok = Button(withd, text="OK", width=10, fg="white", font=('vardana', 15, 'bold'), bg="orange", command=OK)
    ok.place(x=220, y=300)
    
    withd.mainloop()
    
def NewAC():
    New = Toplevel()
    New.title("Create Acc")
    New.geometry("800x700")
    New.configure(bg="steel blue")

    fn = StringVar()
    gender = StringVar()
    ln = StringVar()
    ph = IntVar()
    age = IntVar()
    add = StringVar()
    pc = IntVar()

    def generateAcc():
        if (fn.get() == "") or (ln.get() == "") or (gender.get() == "") or (ph.get() == 0) or (age.get() == 0) or (add.get() == "") or (pc.get() == 0) :
            errorl.config(text="All entries are required to fill !",fg="red")
        else:
            import random
            ac = random.randint(100000000000,999999999999)
            f = fn.get()
            l = ln.get()
            g = gender.get()
            p = ph.get()
            a = age.get()
            ad = add.get()
            pin = pc.get()
            
            connection = mysql.connector.connect(host = "127.0.0.1", user = "root", passwd = "aditya", database = "bank_system" )
            cursor = connection.cursor()
            cursor.execute("insert into useraccount_details (account, fname, lname, gender, phone, age, address, pincode) values(%s, %s, %s, %s, %s, %s, %s, %s)",(ac,f,l,g,p,a,ad,pin))
            connection.commit()
            connection.close()
            messagebox.showinfo("Information","Hii, mr/miss - {}\nYour account number: {}".format(f+" "+l,ac))
            New.destroy()

    def reset():
        fn.set("")
        gender.set("")
        ln.set("")
        ph.set(0)
        age.set(0)
        add.set("")
        pc.set(0)

    top = Label(New,text="Create Bank Account",width=20,bg="steel blue",fg="red",font=("vardana",20,"bold")).pack(side=TOP)
    enter = Label(New,text="Enter Details ➡️",bg="steel blue",fg="purple",font=("vardana",18,"bold")).place(x=50,y=100)
    lbl = Label(New, text="First Name", font=('arial', 15, 'bold'), fg="blue", bg="steel blue").place(x=250, y=150)
    entry = Entry(New,textvariable=fn, width=20, fg="red", font=('arial', 15, 'bold'), bg="white").place(x=450, y=150)
    lbl2 = Label(New, text="Last Name", font=('arial', 15, 'bold'), fg="blue", bg="steel blue").place(x=250, y=200)
    entry2 = Entry(New,textvariable=ln, width=20, fg="red", font=('arial', 15, 'bold'), bg="white").place(x=450, y=200)
    lbl3 = Label(New, text="Gender", font=('arial', 15, 'bold'), fg="blue", bg="steel blue").place(x=250, y=250)
    entry3 = Entry(New,textvariable=gender, justify=CENTER, width=10, fg="red", font=('arial', 15, 'bold'), bg="white").place(x=560, y=250)

    radiobutton_1 = Radiobutton(New, text='Male', fg="white", bg="steel blue", font=('arial', 12, 'bold'), variable=gender, value="Male")
    radiobutton_1.place(x=450, y=250)
    radiobutton_2 = Radiobutton(New, text='Female', fg="white", bg="steel blue", font=('arial', 12, 'bold'), variable=gender, value="Female")
    radiobutton_2.place(x=450, y=290)
    radiobutton_3 = Radiobutton(New, text='Other', fg="white", bg="steel blue", font=('arial', 12, 'bold'), variable=gender, value="Other")
    radiobutton_3.place(x=450, y=330)

    lbl3 = Label(New, text="Phone number", font=('arial', 15, 'bold'), fg="blue", bg="steel blue").place(x=250, y=380)
    entry3 = Entry(New,textvariable=ph, width=20, fg="red", font=('arial', 15, 'bold'), bg="white").place(x=450, y=380)
    lbl3 = Label(New, text="Age", font=('arial', 15, 'bold'), fg="blue", bg="steel blue").place(x=250, y=430)
    entry3 = Entry(New,textvariable=age, width=20, fg="red", font=('arial', 15, 'bold'), bg="white").place(x=450, y=430)
    lbl3 = Label(New, text="Address", font=('arial', 15, 'bold'), fg="blue", bg="steel blue").place(x=250, y=480)
    entry3 = Entry(New,textvariable=add, width=20, fg="red", font=('arial', 15, 'bold'), bg="white").place(x=450, y=480)
    lbl3 = Label(New, text="PIN Code", font=('arial', 15, 'bold'), fg="blue", bg="steel blue").place(x=250, y=530)
    entry3 = Entry(New,textvariable=pc, width=20, fg="red", font=('arial', 15, 'bold'), bg="white").place(x=450, y=530)
    
    btn = Button(New, text="Reset", fg="red", font=('arial', 12, 'bold'), bg="white",command=reset).place(x=100, y=150)

    btn = Button(New, text="Generate Acc number", width=18, fg="white", font=('arial', 15, 'bold'), bg="green",command=generateAcc).place(x=340, y=620)
    errorl = Label(New, text="", bg="steel blue", font=('arial', 15, 'bold'))
    errorl.place(x=320, y=580)

    New.mainloop()


def UserDetail():
    ACDetail = Toplevel()
    ACDetail.title("Acc Details")
    ACDetail.geometry("700x600")
    ACDetail.configure(bg="steel blue")
    
    def temp(e):
            accn.delete(0,"end")

    def closeb():
        ACDetail.destroy()
        
    tp = Label(ACDetail,text="User Account Details",bg="steel blue",fg="red",font=("arial 18 bold"))
    tp.pack()
    close = Button(ACDetail, text="Close", fg="red", font=('arial', 12, 'bold'), bg="steel blue",command=closeb)
    close.place(x=500, y=50)
    l = Label(ACDetail,text="Details ▷",bg="steel blue",fg="blue",font=("arial 16 bold"))
    l.place(x=100,y=100)
    f3 = Frame(ACDetail,width=500,height=400,highlightbackground="blue",highlightthickness=3)
    f3.place(x=100,y=125)

    def OK():
        if ac.get() == "":
            errorl.config(text="Please, Enter user account number!",fg="red")
        elif ac.get() == "Click to enter account number":
            errorl.config(text="        Click above to enter Acc No.",fg="red")
        # elif ac.get().isalpha:
        #     errorl.config(text="Don't try to enter alphabates / symbols !",fg="red")
        elif int(ac.get()) not in account_list():
            errorl.config(text="        Did not match with any user acc !",fg="red")
        else:
            accn.destroy()
            ok.destroy()
            errorl.destroy()
            l1 = Label(f3,text="Your Acc number :",fg="blue",font=("arial 16 bold"))
            l1.place(x=60,y=50)
            l2 = Label(f3,text="First Name :",fg="blue",font=("arial 16 bold"))
            l2.place(x=60,y=90)
            l3 = Label(f3,text="Last Name :",fg="blue",font=("arial 16 bold"))
            l3.place(x=60,y=130)
            l4 = Label(f3,text="Gender",fg="blue",font=("arial 16 bold"))
            l4.place(x=60,y=170)
            l5 = Label(f3,text="Phone Number :",fg="blue",font=("arial 16 bold"))
            l5.place(x=60,y=210)
            l6 = Label(f3,text="Age :",fg="blue",font=("arial 16 bold"))
            l6.place(x=60,y=250)
            l7 = Label(f3,text="Address :",fg="blue",font=("arial 16 bold"))
            l7.place(x=60,y=290)
            l8 = Label(f3,text="Pin Code :",fg="blue",font=("arial 16 bold"))
            l8.place(x=60,y=330)

            connection = mysql.connector.connect(host = "127.0.0.1", user = "root", passwd = "aditya", database = "bank_system" )
            cursor = connection.cursor()
            cursor.execute("select * from useraccount_details where account = %s",(int(ac.get()),))
            data = cursor.fetchall()
            cursor.close()
            connection.close()

            e1 = Label(f3,text=data[0][0],fg="black",font=("arial 16 bold"))
            e1.place(x=280,y=50)
            e2 = Label(f3,text=data[0][1],fg="black",font=("arial 16 bold"))
            e2.place(x=280,y=90)
            e3 = Label(f3,text=data[0][2],fg="black",font=("arial 16 bold"))
            e3.place(x=280,y=130)
            e4 = Label(f3,text=data[0][3],fg="black",font=("arial 16 bold"))
            e4.place(x=280,y=170)
            e5 = Label(f3,text=data[0][4],fg="black",font=("arial 16 bold"))
            e5.place(x=280,y=210)

            year = "{} Year".format(data[0][5])
            e6 = Label(f3,text=year,fg="black",font=("arial 16 bold"))
            e6.place(x=280,y=250)
            e7 = Label(f3,text=data[0][6],fg="black",font=("arial 16 bold"))
            e7.place(x=280,y=290)
            e8 = Label(f3,text=data[0][7],fg="black",font=("arial 16 bold"))
            e8.place(x=280,y=330)


    ac = StringVar()
    accn = Entry(f3, textvariable=ac,justify="center",width=32,fg="black", bg="white", font=("arial", 15, 'bold'),)
    accn.insert(0,"Click to enter account number")
    accn.bind("<FocusIn>",temp)
    accn.place(x=70, y=150)       
    errorl = Label(f3, text="", font=('arial', 12, 'bold'))
    errorl.place(x=100, y=190)
    ok = Button(f3, text="Fetch Details", width=13, fg="white", font=('vardana', 13, 'bold'), bg="green", command=OK)
    ok.place(x=170, y=250)

    ACDetail.mainloop()

def changePin():
    pas = askstring("Verification","Enter Password of system",show="⁕")
    if pas == pino.get():
        pin = Toplevel()
        pin.geometry("600x400")
        pin.title("Change PIN")
        pin.configure(bg="aqua")
        pinn = StringVar()
        def confirm():
            new = pinn.get() 
            pino.set(new)
            messagebox.showinfo("Information","PIN number has updated")
            pin.destroy()

        p = StringVar()
        top = Label(pin, text="Change PIN Number", fg="red", bg="aqua", font=("arial", 20, 'bold'), pady=10).pack(side=TOP)
        lbl = Label(pin, text="Current PIN Number : ", font=('arial', 15, 'bold'), fg="blue", bg="aqua").place(x=50, y=100)
        entry = Entry(pin, width=20,textvariable=p, fg="green", font=('arial', 15, 'bold'), bg="white").place(x=350, y=100)
        p.set(pino.get())
        lbl2 = Label(pin, text="New PIN Number :   ", font=('arial', 15, 'bold'), fg="blue", bg="aqua").place(x=50, y=150)
        entry2 = Entry(pin,textvariable=pinn,show="⁕", width=20, fg="red", font=('arial', 15, 'bold'), bg="white").place(x=350, y=150)
        lbl3 = Label(pin, text="Verify PIN Number : ", font=('arial', 15, 'bold'), fg="blue", bg="aqua").place(x=50, y=200)
        entry3 = Entry(pin,textvariable=pinn, width=20, fg="red", font=('arial', 15, 'bold'), bg="white").place(x=350, y=200)
        btn = Button(pin, text="submit", width=10, fg="white", font=('arial', 15, 'bold'), bg="orange", command=confirm).place(x=250, y=250)

        pin.mainloop()
    else:
        messagebox.showwarning("Invalid password","Please try again!")

def active_users():
    active = Toplevel()
    active.geometry("700x600")
    active.title("Active Users")
    active.configure(bg="steel blue")
    top = Label(active, text="Account List", fg="red",width=20, bg="steel blue", font=("arial", 20, 'bold')).pack(side=TOP)
    info = Label(active,text="Active Account List ➡️", fg="purple", bg="steel blue", font=("vardana", 15, 'bold')).place(x=40,y=80)

    connection = mysql.connector.connect(host = "127.0.0.1", user = "root", passwd = "aditya", database = "bank_system" )
    cursor = connection.cursor()
    cursor.execute("select * from useraccount_details")
    data = cursor.fetchall()
    
    lst = ["Acc.No.","Fname","Lname","Gender","Phone", "Age", "Address", "PinCode"]
    n = 70
    for i in lst:
        lstd = Label(active,text=i, justify=CENTER, fg="green",width=12, bg="pink", font=("vardana", 15,"bold")).place(x=n,y=180)
        n = n+145
    a = 70
    b = 212
    for i in data:
        for j in i:
            data = Label(active,text=j, justify=CENTER, bg="white",width=12, fg="steel blue", font=("vardana", 15,"bold")).place(x=a,y=b)
            a = a+145
        b = b+32
        a = 70
    connection.commit()
    cursor.close()

    active.mainloop()

activeuser = Button(frame,fg="black",bd=1,bg="white",width=7,font=("arial", 13, 'bold'), text="AccList",activebackground="pink",relief=SUNKEN, command=active_users)
activeuser.pack(pady=8)
history = Button(frame,fg="black",bd=1,bg="white",width=7,font=("arial", 13, 'bold'), text="History",activebackground="pink",relief=SUNKEN, command=historyb)
history.pack(pady=9)
about = Button(frame,fg="black",bd=1,bg="white",width=7,font=("arial", 13, 'bold'), text="About",activebackground="pink",relief=SUNKEN, command=aboutb)
about.pack(pady=10)
exitb = Button(frame,fg="black",bd=1,bg="white",width=7,font=("arial", 13, 'bold'), text="Exit",activebackground="pink",relief=SUNKEN, command=exit)
exitb.pack(pady=11)

root.geometry("950x600")
root.title("Menu")
root.configure(bg="steel blue")
top = Label(root, text="Welcome To Sagar Bank", fg="red",width=30, bg="pink",font=("arial", 20, 'bold')).pack(side=TOP)
localtime = time.asctime(time.localtime(time.time()))
time = Label(root, font=('aria', 15), text=localtime,fg="blue", anchor=W,bg="aqua", padx=10)
time.pack()
lbl = Label(root, font=('aria', 15,"bold"), text="Services provided by Bank",fg="white",bg="purple")
lbl.place(x=220,y=120)
# Operation buttons
frame3 = Frame(root,width=600,height=350,bg="blue",highlightbackground="purple",highlightthickness=3).place(x=200,y=150)
enquiry = Button(frame3, padx=10, pady=15,width=16, bd=2, fg="blue", font=('arial', 15, 'bold'), text="Check Balance", bg="aqua", activebackground="purple1", command=balance)
enquiry.place(x=250, y=200)
withdrawm = Button(frame3, padx=10, pady=15,width=16, bd=2, fg="blue", font=('arial', 15, 'bold'), text="Money Withdraw", bg="aqua", activebackground="purple1", command=withdraw)
withdrawm.place(x=250, y=300)
depositem = Button(frame3, padx=10, pady=15,width=16, bd=2, fg="blue", font=('arial', 15, 'bold'), text="Money Deposite", bg="aqua", activebackground="purple1", command=deposite)
depositem.place(x=550, y=200)
changep = Button(frame3, padx=10, pady=15,width=16, bd=2, fg="blue", font=('arial', 15, 'bold'), text="Change System PIN", bg="aqua", activebackground="purple1", command=changePin)
changep.place(x=550, y=300)
Acc = Button(frame3, padx=10, pady=15, bd=2,width=16, fg="blue", font=('arial', 15, 'bold'), text="Open Account", bg="aqua", activebackground="purple1", command=NewAC)
Acc.place(x=250, y=400)
Details = Button(frame3, padx=10, pady=15,width=16, bd=2,fg="blue",bg="aqua",font=("arial", 15, 'bold'), text="Acc Detail", activebackground="purple1", command=UserDetail)
Details.place(x=550, y=400)
l = Label(root, text = "Thankyou for Using",bg="yellow",width=80, fg = "purple", font=('Times New Roman', 20,'bold')) 
l.pack(side = BOTTOM)

root.mainloop()