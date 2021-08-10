from glob import *
from tkinter import *
import os

# Using glob to take all .txt files into variable called "files"
files = glob("Zalecenia/*.txt")

# Creating a tkinter window
root = Tk()
root.geometry('800x600')
root.title("Zalecenia")

# Adding a listbox to window
listbox_items = StringVar(value=files)
listbox = Listbox(root, listvariable=listbox_items, width=50, height=10,
                  selectmode="multiple")
listbox.pack()
# Adding files to listbox

# for file in files:
#     _file = open(file)
#     listbox.insert(END, _file.read(30))





prompt = "Podaj nazwę dla pliku"
label = Label(root, text=prompt)
label.pack()

edit = Entry(root)
edit.pack()

# Adding button to create file with name from entry
def entrybt1():
    filename = edit.get()
    final_file = open(filename, '+a')
    return final_file

def take():
    selected_list = [listbox.get(i) for i in listbox.curselection()]
    for _ in selected_list:
        entrybt1()
        x = open(_, 'r')
        f = entrybt1()
        # f = open(final_name, '+a')
        f.writelines(f"\n...\n{x.read()}")


bt1 = Button(root, text="Utwórz", command=entrybt1)
bt1.pack()

bt3 = Button(root, text='test', command=take)
bt3.pack()




root.mainloop()
