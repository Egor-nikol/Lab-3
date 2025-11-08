from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Radiobutton 
import random


def generation_key():
    code = ''
    letters_list = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for i in range(8):
        code += random.choice(letters_list)
    return code


def clicked():


    def clic_clac():  
        generation_key_str = generation_key()
        key_first_line = format(txt.get())  #кнопка ввода начального ключа
        key_second_line = generation_key_str[:5]
        key_fird_line = key_first_line[-2:] + generation_key_str[5:]   

        if (len(key_first_line) != 5):
            messagebox.showinfo('Error', "Please enter the beginning of the code")
        else:
            messagebox.showinfo('Key', f'''{key_first_line}-
{key_second_line}-
{key_fird_line}''')  
            

    window.bg_img_2 = tk.PhotoImage(file='zurg (1).png')
    label_bg_2 = tk.Label(window, image=window.bg_img_2)
    label_bg_2.place(x=0, y=0, relwidth=1, relheight=1)

    lbl_1.place_forget()#убираем первую надпись
    btn_1.place_forget()#убираем первую кнопку

    lbl_2 = Label(window, text='''Enter the beginning of the key''', 
                  font=("Comic Sans MS", 15), bg="blue", fg="white",) 
    lbl_2.place(relx=0.18, rely=0)

    txt = Entry(window,width=5, font=("Comic Sans MS", 20), bg="green",
              fg="white")  #текстовое окно
    txt.focus() #фокус покус
    txt.place(relx=0.5, rely=0.6) 

    btn_2 = Button(window, text="Get", font=("Comic Sans MS", 20), bg="blue",
              fg="white", command=clic_clac)  #кнопка ввода информации
    btn_2.place(relx=0.8, rely=0.57) 


 


window = tk.Tk()
window.geometry('400x394')  
bg_img_1 = tk.PhotoImage(file='my_bg_orig (1).png')
label_bg_1 = tk.Label(window, image=bg_img_1)
label_bg_1.place(x=0, y=0, relwidth=1, relheight=1)
window.title("TOY story 2")

lbl_1 = Label(window, text="Mysterious key", font=("Comic Sans MS", 20), bg="red",
              fg="yellow",) 
lbl_1.place(relx=0.25, rely=0)

btn_1 = Button(window, text="Get code", font=("Comic Sans MS", 25), bg="red",
              fg="yellow", command=clicked)  
btn_1.place(relx=0.45, rely=0.75) 





window.mainloop()