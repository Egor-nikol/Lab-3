from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Radiobutton 
import random


def generation_key():
    code = ''
    letters_list = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(8):
        code += random.choice(letters_list)
    return code


def clicked():


    def clic_clac():  
        res = format(txt.get())  #кнопка ввода начального ключа

        lbl.configure(text=res) 


    lbl.configure(text="Я же просил...")
    
    txt = Entry(window,width=5)  #текстовое окно
    txt.focus() #фокус покус
    txt.grid(column=0, row=1) 

    btn = Button(window, text="Клик!", command=clic_clac)  #кнопка ввода информации

    btn.grid(column=1, row=1)  


 


window = tk.Tk()
window.geometry('600x520')  
#bg_img = tk.PhotoImage(file='my_bg_orig.jpg')
window.title("Добро пожаловать в приложение Goodby_Universiti_Hello_Game")

lbl = Label(window, text="Привет") 
lbl.grid(column=0, row=0)

btn = Button(window, text="Не нажимать!", font=("Arial Bold", 25), bg="red",
              fg="yellow", command=clicked)  
btn.grid(column=1,  row=0)  





window.mainloop()