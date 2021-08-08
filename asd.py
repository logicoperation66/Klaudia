import tkinter
import glob


# creating a window.
#root = tkinter.Tk()


#Use glob to find input all .txt files to variable.
files = glob.glob("Zalecenia/*.txt")
number = files
root = tkinter.Tk()
root.geometry('800x600')

def onClick(i):
    print(f"Przycisk :{i}")


#rec_check as list of recomendation check :>
def RecCheck():
    n = 0
    for file in files:
        _file = open(file, 'r')
        napis = (f"{_file.read(50)}...")
        b = tkinter.Button(root, text=napis, activeforeground='blue',
                           state='active',
                           command=lambda \
                i=file: onClick(i))
        b.pack()
        n += 1


def FileName():
    name = tkinter.Entry(root, text = "Podaj nazwę dla pliku")
    name.pack()


def start():
    #buttons = []
    for i in range():
        b = tkinter.Button(win, height=1, width=100, command=lambda i=i:
        onClick(i))
        b.pack()
        #buttons.append(b)



#Zrobić list box z opcją zaznaczania wielu opcji na raz.
#Coś tu się chujowo dzieje... Do poprawy.
def ListBox():
    listbox = tkinter.Listbox(root, width=50, height = 4,
                              selectmode="multiple",)
    listbox.pack()
    for file in files:
        listbox.insert(tkinter.END, file)
    return listbox





FileName()
ListBox()

root.mainloop()

