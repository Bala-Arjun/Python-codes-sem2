from tkinter import *
from tkinter import messagebox as mb
w = Tk()
w.geometry("700x500")
l1 = Label(w, text="Login Page", font=("Arial", 16, "bold"))
l2 = Label(w, text="username")
l3 = Label(w, text="password")
username = Entry(w)
password = Entry(w)
def checkuser():
    user = username.get()
    p = password.get()
    if user == "Mlrit" and p == "1234":
        mb.showinfo(message="Login success")
    else:
        mb.showerror(message="Login failed")
b = Button(w, text="Login", command=checkuser)
l1.grid(row=0, columnspan=2)
l2.grid(row=1, column=0)
l3.grid(row=2, column=0)
username.grid(row=1, column=1)
password.grid(row=2, column=1)
b.grid(row=3, columnspan=2)
w.mainloop()
