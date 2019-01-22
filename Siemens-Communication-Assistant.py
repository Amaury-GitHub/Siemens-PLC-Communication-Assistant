#-*coding:utf-8-*-
from tkinter import *
app = Tk()
app.title ('西门子通讯助手')
app.geometry ('290x550')
app.resizable (width = False , height = False)
def Transform(self):
    t.delete(0.0 , END)
    strlist = list(input.get())
    strlen = len(strlist)
    a = 0
    while a < strlen:
        strlist[a] = hex(ord(strlist[a]))
        a += 1
    b = 0
    while b < strlen:
        strlist[b] = strlist[b][2:].upper()
        b += 1
    t.insert(END , '长度:')
    t.insert(END , str(strlen))
    t.insert(END , "\n")
    e = 0
    while e < strlen:
        t.insert(END , '16#')
        t.insert(END , strlist[e])
        t.insert(END , "\n")
        e += 1
Label(app , text = '字符串输入' , font = ('Consolas')).pack()
input = StringVar()
Entry(app , textvariable = input , width = 30 , font = ('Consolas')).pack()
Label(app , text = '转换结果' , font = ('Consolas')).pack()
t = Text(app , width = 15, font = ('Consolas')) 
t.pack()
app.bind('<Key>', Transform)
app.mainloop()
