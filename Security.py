from tkinter import *
from tkinter import messagebox
import subprocess

security = Tk()
security.configure(bg="steel blue")
security.title("Authentication")
security.geometry("400x300")

pin = 'aditya'
def submit():
    if p.get() == pin:
        messagebox.showinfo("information","Permission Granted")
        security.destroy()
        # Run the other script
        subprocess.run(["python", "D:\Python Projects\Bank Management System\Main.py"])
                
    elif p.get() == (None or ""):
        messagebox.showwarning("Warning","Please Enter Password")
    else:
        messagebox.showerror("Error","Invalid password !")

msg = Label(security, text = "System Secutiry ",bg="steel blue", fg = "purple", font=('Times New Roman', 20, 'bold'),padx=100)
msg.pack(side = TOP)
securitys = Label(security, text="System PIN Number",bg="steel blue", fg = "black", font=("arial",13,"bold"))
securitys.place(x=110,y=115)
p = StringVar()
password = Entry(security,show="⁕",justify="center",fg="red",font=("arial",14,"bold"),width=20,textvariable=p)
password.place(x=80,y=140)
submit = Button(security,text="Go",command=submit,width=6, fg="white", font=(
            'arial', 12, 'bold'), bg="orange",activeforeground="red", activebackground="pink").place(x=160,y=220)

security.mainloop()
