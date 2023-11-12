from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

import tkinter as one

file_name = None
def new_file():
    global file_name
    file_name="Без названия"
    text.delete('1.0', END)


#функция сохранения
def save_as():
    out = asksaveasfile(mode='w', defaultextension='.txt')
    data = text.get('1.0', END)
    try:
        out.write(data.rstrip())
    except Exception:
        messagebox.showerror("Извините, нельзя сохранить файл")

def open_file():
    global file_name
    inp = askopenfile(mode='r')
    if inp is None:
        return
        file_name = inp.name
    data = inp.read()
    text.delete('1.0', END)
    text.insert('1.0', data)

# имя и размер окна заметки
root = one.Tk()
root.title('Моя первая заметка ')
root.geometry("300x400+100+200")

#размеры поля
text = Text(root, width=400, height=400)
text.pack()


menu_bar = Menu(root)
file_menu = Menu(menu_bar)

file_menu.add_command(label="Новый", command=new_file)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить как", command=save_as)

menu_bar.add_cascade(label="Файл", menu=file_menu)


root.config(menu=menu_bar)
root.mainloop()


