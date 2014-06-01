#代码由vitual tkinter 生成
from Tkinter import *
from ttk import *
root=Tk()

def calcu():
    cal.set(eval(cal.get()))
 
NONE=StringVar()
Label(text= "calculator!",foreground="red").place(x=232,y=67) 
cal=StringVar()
Entry(textvariable= cal,foreground="red",background="white").place(x=144,y=122) 
Button(text= "click",command=calcu).place(x=331,y=116)
root.geometry("500x500+0+0")
root.mainloop()
