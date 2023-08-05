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
    connection = mysql.connector.connect(host = "127.0.0.1", user = "root", passwd = "Yourpasswd", database = "YourDatabase" )
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

def NameIdentifier(acc):
    con = mysql.connector.Connect(host = "127.0.0.1", user = "root", passwd = "Yourpasswd", database = "Yourdatabase" )
    cursor = con.cursor()
    cursor.execute("select account,fname,lname from useraccount_details")
    data = cursor.fetchall()
    cursor.close()
    con.close()
    for i in data:
        if i[0] == acc :
            name = "{} {}".format(i[-2], i[-1])
            break
    return name

def historyb():
    his = Toplevel()
    his.geometry("800x600")
    his.title("History")
    his.configure(bg="steel blue")
    top = Label(his, text="History", fg="red",width=18, bg="pink", font=("arial", 20, 'bold')).pack(side=TOP)
    info = Label(his,text="Transaction Details ➡️", fg="purple", bg="aqua", font=("vardana", 15, 'bold'))
    info.place(x=40,y=80)

    def temp(e):
        accn.delete(0,"end")

    def OK():
        if ac.get() == "":
            errorl.config(text="Please, Enter user account number!",fg="yellow")
            accn.delete(0,"end")
        elif ac.get() == "Click to enter account number":
            errorl.config(text="      Click above to enter Acc No.",fg="black")
            accn.delete(0,"end")
        # elif ac.get().isalnum is False:
        #     errorl.config(text="Don't try to enter alphabates / symbols !",fg="red")
        #     accn.delete(0,"end")
        elif int(ac.get()) not in account_list():
            errorl.config(text="      Did not match with any user acc !",fg="red")
            accn.delete(0,"end")
        else:
            accn.destroy()
            errorl.destroy()
            ok.destroy()
            youracc = Label(his,text="Your Account Number : ", fg="green", bg="aqua", font=("vardana", 15, 'bold'))
            youracc.place(x=130,y=80)
            youracce = Label(his,text=ac.get(), fg="black", bg="aqua", font=("vardana", 15, 'bold'))
            youracce.place(x=370,y=80)
            info.place(x=40,y=130)

            userdata = "Hello mr/miss. {}, your transactions listed below : ".format(NameIdentifier(int(ac.get())))
            userlabel = Label(his,text=userdata, fg="black", bg="steel blue", font=("calibri", 14, 'bold'))
            userlabel.place(x=40,y=180)
            
            con = mysql.connector.Connect(host = "127.0.0.1", user = "root", passwd = "Yourpasswd", database = "Yourdatabase" )
            cursor = con.cursor()
            cursor.execute("select tdate,ttime,withdrawals,deposites,current_balance from user_transactions where account= {}".format(ac.get()))
            data = cursor.fetchall()
            lst = ["Date","Time","Withdrawals","Deposites","Balance"]
            n = 100
            for i in lst:
                lstd = Label(his,text=i, fg="green",width=9, bg="pink", font=("vardana", 15,"bold")).place(x=n,y=240)
                n = n+120

            a = 100
            b = 272
            for i in data:
                for j in i:
                    data = Label(his,text=j, bg="white",width=9, fg="steel blue", font=("vardana", 15,"bold")).place(x=a,y=b)
                    a = a+120
                b = b+32
                a = 100
            cursor.close()
            con.close() 

    ac = StringVar()
    accn = Entry(his, textvariable=ac,justify="center",width=32,fg="black", bg="white", font=("arial", 15, 'bold'),)
    accn.insert(0,"Click to enter account number")
    accn.bind("<FocusIn>",temp)
    accn.place(x=210, y=200)       
    errorl = Label(his, text="", font=('calibri', 14, 'bold'), bg="steel blue")
    errorl.place(x=240, y=240)
    ok = Button(his, text="View", width=10, fg="white", font=('calibri', 15, 'bold'), bg="green",command=OK)
    ok.place(x=320, y=350)

    his.mainloop()

def aboutb():
    ab = Toplevel()
    ab.geometry("750x500")
    ab.title("About")
    ab.configure(bg="steel blue")
    top = Label(ab, text="About", fg="red",width=16, bg="pink", font=("arial", 20, 'bold')).pack(side=TOP)
    left = Label(ab,text="Bank Description ➡️", fg="purple", bg="steel blue", font=("vardana", 15, 'bold')).place(x=40,y=80)
    data = """◉ The Indian Bank is a system that is developed by aditya patel.
    The main goal of this system is to make easy transaction for the end
    user.By this user can easily interact with the system because I have
    provided a very interactive and user friendly interface and also
    provides consistency,durability & atomacity of the transactions.\n
    ◉ It provides all the services that is needed to bank.\n
    ◉ In this system, Please mantain minimum 100 rupees in account. 
    """
    lab1 = Label(ab, text=data, fg="black",bg="steel blue", font=("calibri", 15)).place(x=90,y=120)
    l2 = Label(ab,text="Technology used ➡️", fg="purple", bg="steel blue", font=("arial", 15, 'bold')).place(x=40,y=340)
    l2 = Label(ab,text="◉ Python Programming\n◉ Tkinter\n◉ Oracle DataBase(MySQL) ", fg="black", bg="steel blue", font=("calibri", 15)).place(x=200,y=370)

    ab.mainloop()

def curb(ac):
    con = mysql.connector.Connect(host = "127.0.0.1", user = "root", passwd = "Yourpasswd", database = "Yourdatabase" )
    cursor = con.cursor()
    cursor.execute("select current_balance from user_transactions where account= {}".format(ac))
    data = cursor.fetchall()
    avb = data[-1][0]
    current.set(avb)
    cursor.close()
    con.close()

def balance():
    bal = Toplevel()
    bal.geometry("550x400")
    bal.title("Balance Check")
    bal.configure(bg="steel blue")
    current_bal = StringVar()

    def show():
        if ac.get() == "":
            errorl.config(text="Please, Enter user account number !",fg="yellow")
            accn.delete(0,"end")
        elif ac.get() == "Click to enter account number":
            errorl.config(text="      Click above to enter Acc No.",fg="black")
            accn.delete(0,"end")
        # elif ac.get().isalnum is False:
        #     errorl.config(text="Don't try to enter alphabates / symbols !",fg="red")
        #     accn.delete(0,"end")
        elif int(ac.get()) not in account_list():
            errorl.config(text="      Did not match with any user acc !",fg="red")
            accn.delete(0,"end")
        else:
            curb(int(ac.get()))
            b =  "{}/-".format(current.get())
            current_bal.set(b)
            lb = Label(bal, text=current_bal.get(), fg="purple", font=('calibri', 15, 'bold'), bg="steel blue")
            lb.place(x=310, y=330)
            accshow = Label(bal, text=ac.get(), fg="black", font=('calibri', 15, 'bold'), bg="steel blue")
            accshow.place(x=310, y=170)
            n = NameIdentifier(int(ac.get()))
            uname = Label(bal, text=n.upper(),fg="black", bg="steel blue", font=('calibri', 15, 'bold'))
            uname.place(x=310, y=210)
            errorl.config(text="✓ User account successfully detected",fg="#00FF66")
            
            

    def temp(e):
        accn.delete(0,"end")

    ac = StringVar()
    top = Label(bal, text="Check Balance", fg="red", bg="pink", width=15, font=("arial", 18, 'bold'))
    top.pack(side=TOP)
    accn = Entry(bal, textvariable=ac,justify="center",width=32,fg="black", bg="white", font=("arial", 15, 'bold'),)
    accn.insert(0,"Click to enter account number")
    accn.bind("<FocusIn>",temp)
    accn.place(x=80, y=90)       
    errorl = Label(bal, text=" ", font=('arial', 12, 'bold'), bg="steel blue")
    errorl.place(x=120, y=120)
    balance1 = Label(bal, text="User Account Number :", fg="white", font=('ariel', 15, 'bold'), bg="steel blue")
    balance1.place(x=75, y=170)
    userName = Label(bal, text="User Name :",justify="right", fg="white", font=('ariel', 15, 'bold'), bg="steel blue")
    userName.place(x=75, y=210)
    balance = Button(bal, text="show", width=10, fg="white", font=('arial', 15, 'bold'), bg="green", command=show)
    balance.place(x=210, y=270)
    lab1 = Label(bal, text="Available amount :     ₹", fg="white",bg="steel blue", font=("arial", 15, 'bold'))
    lab1.place(x=80, y=330)
    
    bal.mainloop()


def exit():
    root.destroy()

def deposite():
    dep = Toplevel()
    dep.geometry("650x400")
    dep.title("Deposite")
    dep.configure(bg="steel blue")
    deposite_amount = DoubleVar()
    ac = StringVar()

    def OK():
        if deposite_amount.get() == 0.0 or deposite_amount.get().is_integer == False:
            messagebox.showerror("Warning" ,"Please,\nEnter valid amount !")
            money_entry.delete(0,"end")
        else:
            curb(int(ac.get()))
            total = current.get() + deposite_amount.get()
            connection = mysql.connector.connect(host = "127.0.0.1", user = "root", passwd = "Yourpasswd", database = "Yourdatabase" )
            cursor = connection.cursor()
            cursor.execute("insert into user_transactions values (%s,%s,%s,%s,%s,%s)", (int(ac.get()), cdate, ctime, 0, deposite_amount.get(),total))
            connection.commit()
            cursor.close()
            connection.close()
            data = "Hello Mr/miss {},\nIn your account ₹{}/- deposited successfully.".format(NameIdentifier(int(ac.get())),deposite_amount.get())
            dep.destroy()
            messagebox.showinfo("Information" , data)
            


    def accCheckButton():
        if int(ac.get()) not in account_list():
            accCheck.config(text="Didn't match with any account number", fg="red")
        else:
            accCheck.config(text="Account successfully Detected ", fg="yellow")

    top = Label(dep, text="Deposite Money", width=15, fg="red", bg="pink",font=("calibri", 18, 'bold'))
    top.pack(side=TOP)
    account_label = Label(dep, text="Enter Account Number :", fg="white", font=('arial', 15, 'bold'), bg="steel blue")
    account_label.place(x=75, y=100)
    account_entry = Entry(dep, textvariable = ac, fg="white", font=('calibri', 15, 'bold'), bg="steel blue")
    account_entry.place(x=320, y=100)
    money_label = Label(dep, text = "Enter amount :", fg="white", font=('arial', 15, 'bold'), bg="steel blue")
    money_label.place(x=75, y=180)
    money_entry = Entry(dep, textvariable = deposite_amount, fg="white", font=('calibri', 15, 'bold'), bg="steel blue")
    money_entry.place(x=320, y=180)
    accCheck = Button(dep, text="varify acc number", font=('calibri', 13),bd=0, bg="steel blue", fg="blue", activebackground="steel blue",command=accCheckButton)
    accCheck.place(x=320, y=130)
    ok = Button(dep, text="deposite", width=8, fg="white", font=('calibri', 15, 'bold'), bg="green", command=OK)
    ok.place(x=270, y=300)
    
    dep.mainloop()

def withdraw():
    withd = Toplevel()
    withd.geometry("650x400")
    withd.title("Withdraw amount")
    withd.configure(bg="steel blue")
    withdraw_amount = DoubleVar()
    ac = StringVar()
    
    def OK():
        if  withdraw_amount.get() == 0.0 or withdraw_amount.get().is_integer == False:
            messagebox.showwarning("Warning" ,"Please,\nEnter valid amount !")
            money_entry.delete(0,"end")
        elif withdraw_amount.get() > current.get():
            messagebox.showerror("Error" ,"Please,\nEnter sufficient amount !")
            money_entry.delete(0,"end")
        else:
            curb(int(ac.get()))
            total = current.get() - withdraw_amount.get()
            connection = mysql.connector.connect(host = "127.0.0.1", user = "root", passwd = "Yourpasswd", database = "Yourdatabase" )
            cursor = connection.cursor()
            cursor.execute("insert into user_transactions values (%s,%s,%s,%s,%s,%s)", (int(ac.get()), cdate, ctime, withdraw_amount.get(), 0,total))
            connection.commit()
            cursor.close()
            connection.close()
            data = "Hello Mr/miss {},\nIn your account ₹{}/- withdrawn successfully.".format(NameIdentifier(int(ac.get())),withdraw_amount.get())
            withd.destroy()
            messagebox.showinfo("Information" , data)
            

    def accCheckButton():
        if int(ac.get()) not in account_list():
            accCheck.config(text="Didn't match with any account number", fg="red")
        else:
            accCheck.config(text="Account successfully Detected ", fg="yellow")

    top = Label(withd, text="Withdraw Money", width=15, fg="red", bg="pink",font=("calibri", 18, 'bold'))
    top.pack(side=TOP)
    account_label = Label(withd, text="Enter Account Number :", fg="white", font=('arial', 15, 'bold'), bg="steel blue")
    account_label.place(x=75, y=100)
    account_entry = Entry(withd, textvariable = ac, fg="white", font=('calibri', 15, 'bold'), bg="steel blue")
    account_entry.place(x=320, y=100)
    money_label = Label(withd, text = "Enter amount :", fg="white", font=('arial', 15, 'bold'), bg="steel blue")
    money_label.place(x=75, y=180)
    money_entry = Entry(withd, textvariable = withdraw_amount, fg="white", font=('calibri', 15, 'bold'), bg="steel blue")
    money_entry.place(x=320, y=180)
    accCheck = Button(withd, text="varify acc number", font=('calibri', 13),bd=0, bg="steel blue", fg="blue", activebackground="steel blue",command=accCheckButton)
    accCheck.place(x=320, y=130)
    ok = Button(withd, text="withdraw", width=8, fg="white", font=('calibri', 15, 'bold'), bg="green", command=OK)
    ok.place(x=270, y=300)
    
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
            d = cdate
            t = ctime
            connection = mysql.connector.connect(host = "127.0.0.1", user = "root", passwd = "Yourpasswd", database = "Yourdatabase" )
            cursor = connection.cursor()
            cursor.execute("insert into useraccount_details (account, fname, lname, gender, phone, age, address, pincode) values(%s, %s, %s, %s, %s, %s, %s, %s)",(ac,f,l,g,p,a,ad,pin))
            cursor.execute("insert into user_transactions values (%s, %s, %s, 0, 100.0, 100.0)",(ac,d,t))
            connection.commit()
            cursor.close() 
            connection.close()
            messagebox.showinfo("Information","Hii, mr/miss - {}\nYour account number: {}\nAnd ₹100.00/- has credited to your acc.".format(f+" "+l,ac))
            New.destroy()

    def reset():
        fn.set("")
        gender.set("")
        ln.set("")
        ph.set(0)
        age.set(0)
        add.set("")
        pc.set(0)

    top = Label(New,text="Open Bank Account",width=20,bg="pink",fg="red",font=("vardana",18,"bold")).pack(side=TOP)
    enter = Label(New,text="Enter Details ➡️",bg="steel blue",fg="purple",font=("vardana",17,"bold")).place(x=50,y=100)
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
        
    tp = Label(ACDetail,text="User Account Details",width=18,bg="pink",fg="red",font=("arial 18 bold"))
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
            accn.delete(0,"end")
        elif ac.get() == "Click to enter account number":
            errorl.config(text="        Click above to enter Acc No.",fg="red")
            accn.delete(0,"end")
        elif ac.get().isalnum is False:
            errorl.config(text="Don't try to enter alphabates / symbols !",fg="red")
            accn.delete(0,"end")
        elif int(ac.get()) not in account_list():
            errorl.config(text="        Did not match with any user acc !",fg="red")
            accn.delete(0,"end")
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

            connection = mysql.connector.connect(host = "127.0.0.1", user = "root", passwd = "Yourpasswd", database = "Yourdatabase" )
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
        top = Label(pin, text="Change PIN Number", fg="red", bg="pink", font=("arial", 20, 'bold'), pady=10).pack(side=TOP)
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
    active.geometry("1300x600")
    active.title("Active Users")
    active.configure(bg="steel blue")
    top = Label(active, text="Account List", fg="red",width=20, bg="pink", font=("arial", 20, 'bold')).pack(side=TOP)
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
    
    cursor.close()
    connection.close()
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
top = Label(root, text="Bank Management System", fg="red",width=30, bg="pink",font=("arial", 20, 'bold')).pack(side=TOP)
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
