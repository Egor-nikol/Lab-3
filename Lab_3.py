import tkinter as tk
from tkinter import messagebox
import random
import pygame


RANDOM_SIZE_FOR_CODE = 8
SIZE_OF_KEY_ONE = 5
SIZE_OF_KEY_TWO = 2
FIRST_FILE_WINDOW = 'my_bg_orig (1).png'
SECOND_FILE_WINDOW = 'zurg (1).png'
MIUSIC = "toy_story_4_27. You've Got a Friend in Me.mp3"


def generation_key():
    code = ''
    letters_list = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for _ in range(RANDOM_SIZE_FOR_CODE):
        code += random.choice(letters_list)
    return code


def clicked():
    def clic_clac():  
        generation_key_str = generation_key()
        key_first_line = format(txt.get())  #кнопка ввода начального ключа
        key_second_line = generation_key_str[:SIZE_OF_KEY_ONE]
        key_fird_line = generation_key_str[SIZE_OF_KEY_ONE:]
        key_fird_line += key_first_line[:SIZE_OF_KEY_TWO] 

        if (len(key_first_line) != 5):
            messagebox.showinfo('Error', 
                                "Please enter the beginning of the code")
        else:
            lbl_3 = tk.Label(window, text=f'''{key_first_line}-
{key_second_line}-
{key_fird_line}''', font=("Comic Sans MS", 18), bg="green", fg="white",) 
            lbl_3.place(relx=0.4, rely=0.7)
            

    window.bg_img_2 = tk.PhotoImage(file=SECOND_FILE_WINDOW)
    label_bg_2 = tk.Label(window, image=window.bg_img_2)
    label_bg_2.place(x=0, y=0, relwidth=1, relheight=1)

    lbl_1.place_forget()#убираем первую надпись
    btn_1.place_forget()#убираем первую кнопку

    lbl_2 = tk.Label(window, text='''Enter the beginning of the key''', 
                  font=("Comic Sans MS", 15), bg="green", fg="white",) 
    lbl_2.place(relx=0.18, rely=0)


    txt = tk.Entry(window,width=5, font=("Comic Sans MS", 20), bg="green",
              fg="white")  #текстовое окно с вводом начального кода
    txt.focus() #фокус покус
    txt.place(relx=0.35, rely=0.4) 

    btn_2 = tk.Button(window, text="Get", font=("Comic Sans MS", 20), bg="blue",
              fg="white", command=clic_clac)  #кнопка ввода информации
    btn_2.place(relx=0.65, rely=0.37) 


 


window = tk.Tk()
window.geometry('400x394')  
bg_img_1 = tk.PhotoImage(file=FIRST_FILE_WINDOW)
label_bg_1 = tk.Label(window, image=bg_img_1)
label_bg_1.place(x=0, y=0, relwidth=1, relheight=1)
window.title("TOY story 2")

pygame.mixer.init()
pygame.mixer.music.load(MIUSIC)
pygame.mixer.music.play(-1)

lbl_1 = tk.Label(window, text="Mysterious key", font=("Comic Sans MS", 20),
               bg="red", fg="yellow",) 
lbl_1.place(relx=0.25, rely=0)

btn_1 = tk.Button(window, text="Get code", font=("Comic Sans MS", 25), 
               bg="red", fg="yellow", command=clicked)  
btn_1.place(relx=0.45, rely=0.75) 

window.mainloop()