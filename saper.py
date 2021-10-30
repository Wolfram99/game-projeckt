#!/usr/bin/python3
import tkinter as tk
from random import sample, shuffle

colors = {
    1:  'blue',
    2:  '#E5BE01',
    3:  'red',
    4:  'green',
    5:  '#66000E',
    6:  '#DF1663',
    7:  'orange',
    8:  '#273B0C'
}

class NewButton(tk.Button):
    def __init__(self, master, x, y, number=0,*args, **kwargs):
        super(NewButton, self).__init__(master,width = 3, font='Calibri 15 bold', *args, **kwargs)
        self.x = x
        self.number = number
        self.y = y
        self.is_mine = False 
        self.count_bomb = 0
        self.is_open = False

    def __repr__(self):
        return f'NewButton {self.number} {self.is_mine}'
      

class Saper:

    window = tk.Tk()  
    ROW = 10
    COLUMNS = 7
    MINES = 10

#добовляем картинку в проект и меняем картинку нашего окна, название и доступ
    photo = tk.PhotoImage(file='image.jpeg')    #можно
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
            #clicked_button.config( disabledforrground="black")  #т.к.мы поставили что кнопки нажимаются только 1 раз то они со старта серые, а мы этой командой делаем черными
            clicked_button.is_open = True
        else:
            color = colors.get(clicked_button.count_bomb, 'black')
            if clicked_button.count_bomb:
                clicked_button.config(text=clicked_button.count_bomb, disabledforeground=color)
                clicked_button.is_open = True
            else:
               self.breadth_first_search(clicked_button) 
        clicked_button.config(state='disabled')
        clicked_button.config(relief=tk.SUNKEN)

    def breadth_first_search(self, btn: NewButton):
        queue = [btn]
        while queue:

            cur_btn =  queue.pop()
            color=colors.get(cur_btn.count_bomb, 'black')
            if cur_btn.count_bomb:
                cur_btn.config(text=cur_btn.count_bomb, disabledforeground=color)
            else:
                cur_btn.config(text='', disabledforeground=color)
            cur_btn.is_open = True
            cur_btn.config(state='disabled')
            cur_btn.config(relief=tk.SUNKEN)

            if cur_btn.count_bomb == 0:
                x, y = cur_btn.x, cur_btn.y
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if not abs(dx-dy) == 1:
                            continue

                        next_btn = self.buttons[x+dx][y+dy]
                        if not next_btn.is_open and 1<=next_btn.x<=Saper.ROW and 1<=next_btn.y<=Saper.COLUMNS and next_btn not in queue:
                            queue.append(next_btn)

    def print_buttons(self):
        for i in range(1, Saper.ROW + 1):
            for j in range(1, Saper.COLUMNS + 1):
                btn = self.buttons[i][j]
                if btn.is_mine:
                    print("B", end = ' ')
                else:
                    print(btn.count_bomb, end = ' ')
            print()        

    def create_tables(self):
        for i in range(1, Saper.ROW+1):
            for j in range(1, Saper.COLUMNS+1):
                btn = self.buttons[i][j]
                btn.grid(row=i, column=j)

    def open_all_buttons(self):
        for i in range(Saper.ROW+2):
            for j in range(Saper.COLUMNS+2):
                btn = self.buttons[i][j]
                if btn.is_mine: 
                    btn.config(text="*", background="red")  #мы меняем конфиг кнопки которые передаём в clicked_button
                    #т.к.мы поставили что кнопки нажимаются только 1 раз то они со старта серые, а мы этой командой делаем черными
                #elif btn.count_bomb == 0:
                #    btn.config(text = btn.count_bomb, fg = 'blue') 
                #elif btn.count_bomb == 2:
                #    btn.config(text=btn.count_bomb, fg = 'yelow')
                #elif btn.count_bomb == 3:
                #    btn.config(text = btn.count_bomb, fg = 'red')
                #elif btn.count_bomb == 4:
                #    btn.config(text = btn.count_bomb, fg = 'green') 
                #elif btn.count_bomb == 5:
                #    btn.config(text=btn.count_bomb, fg = 'orange')
                #elif btn.count_bomb == 6:
                #    btn.config(text = btn.count_bomb, fg = '#DF1663')
                #elif btn.count_bomb == 7:
                #    btn.config(text=btn.count_bomb, fg = '#66000E')
                #elif btn.count_bomb == 8:
                #    btn.config(text = btn.count_bomb, fg = '#273B0C')    

                elif btn.count_bomb in colors:
                    color = colors.get(btn.count_bomb, "black")
                    btn.config(text=btn.count_bomb, fg = color)
        

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

    def count_mines_in_ceils(self):
        for i in range(1, Saper.ROW + 1):
            for j in range(1, Saper.COLUMNS+1):
                btn = self.buttons[i][j]
                count_bomb = 0
                if not btn.is_mine:
                    for row_dx in [-1, 0, 1]:
                        for col_dx in [-1, 0, 1]:
                            sosed = self.buttons[i + row_dx][j + col_dx]
                            if sosed.is_mine:
                                count_bomb += 1
                btn.count_bomb = count_bomb

    def get_mines(self):
        index = list(range(1, Saper.ROW * Saper.COLUMNS + 1))   
        shuffle(index)
        return index[:Saper.MINES]         

#выводим окно при помощи обработчика
    def start(self):
        self.create_tables()
        self.insert_mines()
        self.count_mines_in_ceils()
        self.print_buttons()
        #self.open_all_buttons()
        Saper.window.mainloop() 
             

start_game = Saper()
start_game.start() 