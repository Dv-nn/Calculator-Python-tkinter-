import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title('Calculator')
root.geometry('470x510+100+200')
root.resizable(False, False)
root.configure(bg='#17161b')

photo = PhotoImage(file='energy.png')
root.iconphoto(False, photo)

equation = ''


def show(value):
    global equation
    equation += value
    label_result.config(text=equation)


def clear():
    global equation
    equation = ''
    label_result.config(text=equation)


def calculate():
    global equation
    result = ''
    if equation != '':
        try:
            result = eval(equation)
        except:
            result = 'error'
            equation = ''
    label_result.config(text=result)


label_result = Label(root, width=25, height=2, text='', font=('Ubuntu', 30))
label_result.pack()

Button(root, text='C', width=5, font=('Ubuntu', 24), bd=1, fg='#fff', bg='#3697f5',
       command=lambda: clear()).place(x=20, y=110)
Button(root, text='/', width=5, font=('Ubuntu', 24), bd=1, fg='#fff', bg='#2a2d36',
       command=lambda: show('/')).place(x=130, y=110)
Button(root, text='%', width=5, font=('Ubuntu', 24), bd=1, fg='#fff', bg='#2a2d36',
       command=lambda: show('%')).place(x=240, y=110)
Button(root, text='*', width=5, font=('Ubuntu', 24), bd=1, fg='#fff', bg='#2a2d36',
       command=lambda: show('*')).place(x=350, y=110)

Button(root, text='7', width=5, font=('Ubuntu', 24), bd=1, fg='#fff', bg='#2a2d36',
       command=lambda: show('7')).place(x=20, y=190)
Button(root, text='8', width=5, font=('Ubuntu', 24), bd=1, fg='#fff', bg='#2a2d36',
       command=lambda: show('8')).place(x=130, y=190)
Button(root, text='9', width=5, font=('Ubuntu', 24), bd=1, fg='#fff', bg='#2a2d36',
       command=lambda: show('9')).place(x=240, y=190)
Button(root, text='-', width=5, font=('Ubuntu', 24), bd=1, fg='#fff', bg='#2a2d36',
       command=lambda: show('-')).place(x=350, y=190)

Button(root, text='4', width=5, font=('Ubuntu', 24), bd=1, fg='#fff', bg='#2a2d36',
       command=lambda: show('4')).place(x=20, y=270)
Button(root, text='5', width=5, font=('Ubuntu', 24), bd=1, fg='#fff', bg='#2a2d36',
       command=lambda: show('5')).place(x=130, y=270)
Button(root, text='6', width=5, font=('Ubuntu', 24), bd=1, fg='#fff', bg='#2a2d36',
       command=lambda: show('6')).place(x=240, y=270)
Button(root, text='+', width=5, font=('Ubuntu', 24), bd=1, fg='#fff', bg='#2a2d36',
       command=lambda: show('+')).place(x=350, y=270)

Button(root, text='1', width=5, font=('Ubuntu', 24), bd=1, fg='#fff', bg='#2a2d36',
       command=lambda: show('1')).place(x=20, y=350)
Button(root, text='2', width=5, font=('Ubuntu', 24), bd=1, fg='#fff', bg='#2a2d36',
       command=lambda: show('2')).place(x=130, y=350)
Button(root, text='3', width=5, font=('Ubuntu', 24), bd=1, fg='#fff', bg='#2a2d36',
       command=lambda: show('3')).place(x=240, y=350)
Button(root, text='0', width=10, font=('Ubuntu', 24), bd=1, fg='#fff', bg='#2a2d36',
       command=lambda: show('0')).place(x=20, y=430)

Button(root, text='.', width=5, font=('Ubuntu', 24), bd=1, fg='#fff', bg='#2a2d36',
       command=lambda: show('.')).place(x=240, y=430)
Button(root, text='=', width=5, height=3, font=('Ubuntu', 24), bd=1, fg='#fff', bg='#fe9037',
       command=lambda: calculate()).place(x=350, y=350)

root.mainloop()
