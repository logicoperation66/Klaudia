import tkinter as tk
import os

def searchfiles(extension='.txt', folder='/home/stinky/PycharmProjects/KlaudiaZalecenia/Zalecenia'):
    "insert all files in the listbox"
    for r , d, f in os.walk(folder):
        for file in f:
            if file.endswith(extension):
                lb.insert(0, r + "\\" + file)


def open_file():
    os.open(lb.get(lb.curselection()[0]))

root = tk.Tk()
root.geometry("400x400")
bt = tk.Button(root, text="Search", command=lambda:searchfiles())
bt.pack()
lb = tk.Listbox(root)
lb.pack(fill="both", expand=1)
lb.bind("<Double-Button>", lambda x: open_file())
root.mainloop()
