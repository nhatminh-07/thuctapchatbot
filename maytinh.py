import tkinter
from tkinter import *

#tao man hinh tinh
window = tkinter.Tk()

#thiet lap tieu de
window.title("May tinh bo tui")

e = Entry(width =20, borderwidth=10, font = "Arial 18") # hộp nhập văn bản
e.grid(row = 0, column = 0, columnspan = 5, pady = 10)

def bt_add(num):
    global num1 #global var
    num1 = int(e.get())
    e.delete(0, END)
    global operator
    operator = 1


def click(num):
    e.insert(END, str(num))

def in_ra_ket_qua():
    global num1, operator
    num2 = int(e.get())
    

# các nút bấm
# lambda function: javascript anonymous function
# function as warped into oneself
bt_7 = Button(text = "7", width = 10, height = 3, command = lambda: click(7))
bt_7.grid(row = 1, column = 0)
bt_8 = Button(text = "8", width = 10, height = 3, command = lambda: click(8))
bt_8.grid(row = 1, column = 1)
bt_9 = Button(text = "9", width = 10, height = 3, command = lambda: click(9))
bt_9.grid(row = 1, column = 2)
bt_del = Button(text = "Delete", width = 10, height = 3, command = lambda: e.delete(END))
bt_del.grid(row = 1, column = 3)
bt_AC = Button(text = "AC", width = 10, height = 3, command = lambda: e.delete(0, END))
bt_AC.grid(row = 1, column = 3)

# H2
bt_4 = Button(text = "4", width = 10, height = 3, command = lambda: click(4))
bt_4.grid(row = 2, column = 0)
bt_5 = Button(text = "5", width = 10, height = 3, command = lambda: click(5))
bt_5.grid(row = 2, column = 1)
bt_6 = Button(text = "6", width = 10, height = 3, command = lambda: click(6))
bt_6.grid(row = 2, column = 2)
bt_mul = Button(text = "x", width = 10, height = 3, command = click(1))
bt_mul.grid(row = 2, column = 3)
bt_div = Button(text = ":", width = 10, height = 3, command = click(1))
bt_div.grid(row = 2, column = 4)

# H3
bt_1 = Button(text = "1", width = 10, height = 3, command = lambda: click(1))
bt_1.grid(row = 3, column = 0)
bt_2 = Button(text = "2", width = 10, height = 3, command = lambda: click(2))
bt_2.grid(row = 3, column = 1)
bt_3 = Button(text = "3", width = 10, height = 3, command = lambda: click(3))
bt_3.grid(row = 3, column = 2)
bt_pl = Button(text = "+", width = 10, height = 3)
bt_pl.grid(row = 3, column = 3)
bt_min = Button(text = "-", width = 10, height = 3)
bt_min.grid(row = 3, column = 4)

# H0
bt_dot = Button(text = ".", width = 10, height = 3, command = lambda: click(0))
bt_dot.grid(row = 4, column = 0)
bt_0 = Button(text = "0", width = 10, height = 3, command = lambda: click(0))
bt_0.grid(row = 4, column = 1)
bt_cal = Button(text = "=", width = 10, height = 3, command = lambda: click(0))
bt_cal.grid(row = 4, column = 2)

#Luôn để xuống cuối dòng
window.mainloop()
#giống matplotlib
#mục tiêu tạo ra textbox này!!

# 24/5/2020, Tkinter

