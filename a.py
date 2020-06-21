from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Burtgel")
window.geometry("400x400")
window.resizable(0,0)

# reg_no, owog, ner, utas
reg_no = StringVar()
owog = StringVar()
ner = StringVar()
utas = StringVar()


Label(window, text="registr: ").grid(row=0, column=0)
Entry(window, textvariable=reg_no).grid(row=0, column=1)

Label(window, text="owog: ").grid(row=1, column=0)
Entry(window, textvariable=owog).grid(row=1, column=1)

Label(window, text="ner: ").grid(row=2, column=0)
Entry(window, textvariable=ner).grid(row=2, column=1)

Label(window, text="utas: ").grid(row=3, column=0)
Entry(window, textvariable=utas).grid(row=3, column=1)


def user_save():
    if reg_no.get() == "" or owog.get() == "" or ner.get() == "" or utas.get() == "":
        messagebox.showwarning("Warning", "Medeelliig buren oruulna uu")
    else:
        list_data.insert(END,reg_no.get() + "  " + owog.get() + "  " + ner.get() + "  " + utas.get())
        user_clear()
def user_update():
    index1 = list_data.curselection()[0]
    if reg_no.get() == "" or owog.get() == "" or ner.get() == "" or utas.get() == "":
        messagebox.showwarning("Warning", "Medeelliig buren oruulna uu")
    else:
        list_data.delete(index1)
        list_data.insert(index1,reg_no.get() + "  " + owog.get() + "  " + ner.get() + "  " + utas.get())
        user_clear()
def user_delete():
    index1 = list_data.curselection()[0]
    answer = messagebox.askokcancel("Warning", "Do you want to delete?")
    if answer == True:
        list_data.delete(index1)
def user_clear():
    reg_no.set("")
    owog.set("")
    ner.set("")
    utas.set("")
def user_select():
    selected_user = list_data.get(list_data.curselection()[0])
    data = selected_user.split(" ")
    reg_no.set(data[0])
    owog.set(data[1])
    ner.set(data[2])
    utas.set(data[3])
Button(window, text="hadgalah", command=user_save).grid(row=0, column=3)
Button(window, text="zasvarlah", command=user_update).grid(row=1,column=3)
Button(window, text="ustgah", command=user_delete).grid(row=2, column=3)
Button(window, text="arilgah", command=user_clear).grid(row=3, column=3)

list_data = Listbox(window, width=50, height=10)
list_data.grid(row=4, rowspan=4, column=0, columnspan=4)
list_data.bind("<<ListboxSelect>>")
list_data.insert(END, "register1  owog1  ner1  utas1")
list_data.insert(END, "register2  owog2  ner2  utas2")
list_data.insert(END, "register3  owog3  ner3  utas3")

scroll = Scrollbar(window)
scroll.grid(row=4, column=4)
list_data.configure(yscrollcommand=scroll.set)
scroll.configure(command=list_data.yview)


window.mainloop()