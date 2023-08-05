from tkinter import *
from tkinter import messagebox
import subprocess

logwin = Tk()
logwin.title("LogIn")
logwin.geometry("800x550")
logwin.configure(bg="pink")
u = StringVar()
p = StringVar()
new_user = StringVar()
new_pass = StringVar()

def comeToMainWin():
    logwin.destroy()
    subprocess.run(["python","D:\Python Projects\Bank Management System\LogIn.py"])
    

def NewAccount():
    msg.destroy()
    name.destroy()
    user.destroy()
    pas.destroy()
    passwd.destroy()
    create.destroy()
    login.destroy()
    error_info.destroy()
    l.destroy()

    def confrm():
        messagebox.showinfo("Information", "Account created successfully.")

    f1.configure(height=350)
    back = Button(logwin, text = "Back", bg="pink",fg="green", font=("vardana",12,"bold"),command=comeToMainWin)
    back.place(x=150,y=90)
    AChead = Label(f1, text = "Sign Up", bg="steel blue", fg="purple", font=("vardana",18,"bold"))
    AChead.place(x=200,y=5)
    
    newuser = Label(f1,text="Enter UserName ",bg="steel blue",fg="black",font=("vardana",13,"bold"))
    newuser.place(x=20,y=110)
    newusere = Entry(f1,textvariable=new_user,bg="white",fg="green",font=("vardana",15,"bold")).place(x=210,y=110)
    newpas = Label(f1,text="Enter Password ",bg="steel blue",fg="black",font=("vardana",13,"bold")).place(x=20,y=160)
    newpasse = Entry(f1,bg="white",fg="green",font=("vardana",15,"bold")).place(x=210,y=160)
    confirmnewpas = Label(f1,text="Confirm Password",bg="steel blue",fg="black",font=("vardana",13,"bold")).place(x=20,y=210)
    confirmnewpasse = Entry(f1,textvariable=new_pass,bg="white",fg="green",font=("vardana",15,"bold")).place(x=210,y=210)

    submitac = Button(f1,text="Submit",width=8,bg="orange",fg="black",font=("vardana",13,"bold"),command=confrm).place(x=210,y=300)

def submited():
    us = u.get()
    pa = p.get()
    if us == "ap123" and pa == "pass":
        error_info.config(text="You have successfully LogIn to the system",bg="steel blue",fg="green",font=("vardana",12,"bold"))
        messagebox.showinfo("msg","LOGIN successful")
        logwin.destroy()
        subprocess.run(["python","D:\Python Projects\Bank Management System\Security.py"])
        
    elif us == "" and pa == "":
        error_info.config(text="All the entries required to fill !",bg="steel blue",fg="red",font=("vardana",12,"bold"))
    else:
        error_info.config(text="Incorrect username or password !",bg="steel blue",fg="red",font=("vardana",12,"bold"))
        user.delete(0,END)
        pas.delete(0,END)


head = Label(logwin, text = "LogIn window", bg="pink", fg="red", font=("vardana",20,"bold"))
head.pack(side = TOP)
l = Label(logwin,text="🛃  Please enter the user ID or Password ",bg="pink",font="arial 15")
l.place(x=100,y=100)
f1 = Frame(logwin,width=500,height=300,bg="steel blue",highlightbackground="blue",highlightthickness=3)
f1.place(x=150,y=160)
msg = Label(f1, text="LOGIN", fg="purple",bg="steel blue",font=("vardana",15,"bold"))
msg.place(x=220,y=10)
name = Label(f1, text="User Name :", fg="black",bg="steel blue",font=("vardana",15,"bold"))
name.place(x=70,y=80)
passwd = Label(f1, text="Password :", fg = "black",bg="steel blue",font=("vardana",15,"bold"))
passwd.place(x=70,y=130)

user = Entry(f1,textvariable=u,fg = "green",bg="white",font=("vardana",15,"bold"))
user.place(x=200,y=80)
pas = Entry(f1,textvariable=p,show="⁕",fg = "green",bg="white",font=("vardana",15,"bold"))
pas.place(x=200,y=130)
create = Button(f1,text="Create an Account",activeforeground="blue",activebackground="steel blue",bd=0, fg = "black",bg="steel blue",font=(" vardana 13 bold underline "),command=NewAccount)
create.place(x=140,y=200)

login = Button(f1,text="LogIn",command=submited,activeforeground="red",font=("vardana",10,"bold") ,activebackground="pink",bg="orange")
login.place(x=300,y=200)
error_info = Label(logwin,text="")
error_info.place(x=270,y=430)

logwin.mainloop()

