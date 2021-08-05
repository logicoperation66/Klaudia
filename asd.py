import tkinter
import glob


### creating a window.
#root = tkinter.Tk()
#root.geometry('800x800')

### Use glob to find input all .txt files to variable.
files = glob.glob("Zalecenia/*.txt")
number = files
root = tkinter.Tk()

def onClick(i):
    choice =
    path = files[choice - 1]
        text = open(path, 'r')
        f = open(final_filename, '+a')
        f.writelines(f"\n...\n{text.read()}")

##rec_check as list of recomendation check :>
def rec_check():
    n = 1
    for file in files:
        _file = open(file, 'r')
        napis = (f"Zalecenie nr.{n} \n{_file.read(50)}...")
        # tkinter.Label(root, text=napis).pack(anchor='w')
        b = tkinter.Button(root, text=napis, command=lambda i=file: onClick(i))
        b.pack()
        n += 1



def start():
    #buttons = []
    for i in range(10):
        b = tkinter.Button(win, height=1, width=100, command=lambda i=i:
        onClick(i))
        b.pack()
        #buttons.append(b)

rec_check()
root.mainloop()

