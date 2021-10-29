#!/usr/bin/python3
import tkinter as tk
from random import shuffle 

class NewButton(tk.Button):
    def __init__(self, master, x, y, number,*args, **kwargs):
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
    photo = tk.PhotoImage(file='image.jpeg')
    window.iconphoto(False, photo)
    window.title('Сапёр') 
    window.resizable(True ,True)

    def __init__(self):
#создание пустого списка для последующего заполнения его кнопками
        self.buttons = []
        count = 1
        for i in range(Saper.ROW):
            temp = []                       #создание временного пустого списка для записи строк
            for j in range(Saper.COLUMNS):
                btn = NewButton(Saper.window, x = i, y = j, number = count)        #создание кнопок котороые распологаются в нашем окне
                temp.append(btn)  
                count += 1              #заполнение путого списка кнопками
            self.buttons.append(temp)                #заполнение основного мсписка временным

    def print_buttons(self):
        for row_btn in self.buttons:
            print(row_btn)

    def create_tables(self):
        for i in range(Saper.ROW):
            for j in range(Saper.COLUMNS):
                btn = self.buttons[i][j]
                btn.grid(row=i, column=j)

    def insert_mines(self):
        index_mines = self.get_mines()
        for row_btn in self.buttons:
            for btn in row_btn:
                if btn.number in index_mines:
                    btn.is_mine = True

    def get_mines(self):
        index = list(range(1, Saper.ROW * Saper.COLUMNS + 1))   
        shuffle(index)
        return index[:Saper.MINES]         

#выводим окно при помощи обработчика
    def start(self):
        self.create_tables()
        self.insert_mines()
        self.print_buttons()
        Saper.window.mainloop() 
             

start_game = Saper()
start_game.start() 