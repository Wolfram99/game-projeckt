#!/usr/bin/python3
import tkinter as tk
from random import shuffle
from tkinter.constants import COMMAND 

class NewButton(tk.Button):
    def __init__(self, master, x, y, number=0,*args, **kwargs):
        super(NewButton, self).__init__(master,width = 3, font='Calibri 15 bold', *args, **kwargs)
        self.x = x
        self.number = number
        self.y = y
        self.is_mine = False 

    def __repr__(self):
        return f'NewButton {self.number} {self.is_mine}'
      

class Saper:

    window = tk.Tk()  
    ROW = 10
    COLUMNS = 7
    MINES = 7

#добовляем картинку в проект и меняем картинку нашего окна, название и доступ
    photo = tk.PhotoImage(file='image.jpeg')    #в гите нельзя работать с фото 
    window.iconphoto(False, photo)
    window.title('Сапёр') 
    window.resizable(True ,True)

    def __init__(self):
#создание пустого списка для последующего заполнения его кнопками
        self.buttons = []
        for i in range(Saper.ROW+2):
            temp = []                       #создание временного пустого списка для записи строк
            for j in range(Saper.COLUMNS+2):
                btn = NewButton(Saper.window, x = i, y = j)        #создание кнопок котороые распологаются в нашем окне
                btn.config(command = lambda button=btn: self.click(button))
                temp.append(btn)  
            self.buttons.append(temp)                #заполнение основного мсписка временным

    def click (self, clicked_button: NewButton): #после : мы показываем что мы работаем с классом newbutton, а иммено с кнопками 
        if clicked_button.is_mine: 
            clicked_button.config(text="*", background="red")  #мы меняем конфиг кнопки которые передаём в clicked_button
            clicked_button.config( disabledforrground="black")  #т.к.мы поставили что кнопки нажимаются только 1 раз то они со старта серые, а мы этой командой делаем черными
        else:
            clicked_button.config(text=clicked_button.number, background="green", disabledforeground="black")
        clicked_button.config(state='disabled')

    def print_buttons(self):
        for row_btn in self.buttons:
            print(row_btn)

    def create_tables(self):
        for i in range(Saper.ROW+2):
            for j in range(Saper.COLUMNS+2):
                btn = self.buttons[i][j]
                btn.grid(row=i, column=j)

    def open_all_buttons(self):
        for i in range(Saper.ROW+2):
            for j in range(Saper.COLUMNS+2):
                btn = self.buttons[i][j]
                if btn.is_mine: 
                    btn.config(text="*", background="red")  #мы меняем конфиг кнопки которые передаём в clicked_button
                    #т.к.мы поставили что кнопки нажимаются только 1 раз то они со старта серые, а мы этой командой делаем черными
                else:
                    btn.config(text=btn.number, background="green", disabledforeground="black")
        

    def insert_mines(self):
        index_mines = self.get_mines()
        count = 1
        for i in range(1, Saper.ROW + 1):
            for j in range(1, Saper.COLUMNS + 1):
                btn = self.buttons[i][j]
                btn.number = count
                if btn.number in index_mines:
                    btn.is_mine = True
                count += 1

    def get_mines(self):
        index = list(range(1, Saper.ROW * Saper.COLUMNS + 1))   
        shuffle(index)
        return index[:Saper.MINES]         

#выводим окно при помощи обработчика
    def start(self):
        self.create_tables()
        self.insert_mines()
        self.print_buttons()
        self.open_all_buttons()
        Saper.window.mainloop() 
             

start_game = Saper()
start_game.start() 