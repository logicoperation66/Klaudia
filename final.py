import os
from glob import *
from tkinter import *
from pathlib import Path

def entrybt1():
    filename = edit.get()
    final_file = open(filename, '+a')
    return final_file

def searchfiles(extension='.txt', folder='/home/stinky/PycharmProjects/KlaudiaZalecenia/Zalecenia'):
    "insert all files in the listbox"
    for r , d, f in os.walk(folder):
        for file in f:
            if file.endswith(extension):
                lb.insert(0, r + "\\" + file)

def input():
    selected_files = [lb.get(i) for i in lb.curselection()]
    for file in selected_files:
        x = open(file, '+a')
        entrybt1()
        f = entrybt1()
        f.writelines(f"\n...\n{x.read()}")

def take():
    selected_list = [listbox.get(i) for i in listbox.curselection()]
    for file in selected_list:
        x = open(file, 'r')
        f = entrybt1()
        # f = open(final_name, '+a')
        f.writelines(f"\n...\n{x.read()}")

# Adding button to create file with name from entry


# Using glob to take all .txt files into variable called "files"
# files = glob("Zalecenia/*.txt")
# path = r"/home/stinky/PycharmProjects/KlaudiaZalecenia/Zalecenia"
# files = os.listdir(path)

# Creating a tkinter window
root = Tk()
root.geometry('800x600')
root.title("Zalecenia")

# Adding a listbox to window
lb = Listbox(root, width=50, height=10,
                  selectmode="multiple")
lb.pack()


prompt = "Podaj nazwę dla pliku"
label = Label(root, text=prompt)
label.pack()

edit = Entry(root)
edit.pack()


# bt1 = Button(root, text="Utwórz", command=entrybt1)
# bt1.pack()

bt3 = Button(root, text='test', command=searchfiles())
bt3.pack()

bt3 = Button(root, text='Dodaj', command=input())
bt3.pack()
root.mainloop()
