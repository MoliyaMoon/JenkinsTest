import os,sys
import Tkinter

top = Tkinter.Tk()
label = Tkinter.Label(top, text='Hello World!')
label.pack()
quit = Tkinter.Button(top, text='Hello World!',command=top.quit)
quit.pack()
Tkinter.mainloop()