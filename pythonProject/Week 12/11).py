from tkinter import *
w = Tk()
w.geometry("700x500")
w.title("Simple Message App")
l1 = Label(w, text="Enter your message:")
l1.pack()
e1 = Entry(w)
e1.pack()
b1 = Button(w, text="Submit")
b1.pack()
def show_message():
    message = e1.get()
    if message.strip() != "":
        l2 = Label(w, text=message)
        l2.pack()
        e1.delete(0, END)
b1.config(command=show_message)
w.mainloop()
