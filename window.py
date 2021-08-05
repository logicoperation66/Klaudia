import tkinter

root = tkinter.Tk()
root.geometry('640x640')



def funkcjaguzik1():
    print('Wciśnięto przycisk 1')
def funkcjaguzik2(event):
    print('Wciśnięto przycisk 2')
def funkcjaguzik3(event):
    print('Wciśnięto przycisk 3')

b1 = tkinter.Button(root,text='guzik1', command = funkcjaguzik1)
b1.pack()
b2 = tkinter.Button(root,text='guzik2')
b2.bind('<Button-1>',funkcjaguzik2)
b2.pack()
b3 = tkinter.Button(root,text='guzik3')
b3.bind('<Button-1>',funkcjaguzik3)
b3.pack()

root.bind
root.mainloop()

