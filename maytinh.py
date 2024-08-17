import tkinter
from tkinter import *

#tao man hinh tinh
window = tkinter.Tk()


#thiet lap tieu de
window.title("May tinh bo tui")

e = Entry(width =20, borderwidth=10, font = "Arial 18") # hộp nhập văn bản
e.grid(row = 0, column = 0, columnspan = 4, pady = 10)

# các nút bấm
bt_1 = Button(text = "1", width = 10, height = 3)
bt_1.grid(row = 1, column = 0)
bt_2 = Button(text = "2", width = 10, height = 3)
bt_2.grid(row = 1, column = 1)
bt_3 = Button(text = "3", width = 10, height = 3)
bt_3.grid(row = 1, column = 2)

# các nút bấm
bt_1 = Button(text = "1", width = 10, height = 3)
bt_1.grid(row = 1, column = 0)
bt_2 = Button(text = "2", width = 10, height = 3)
bt_2.grid(row = 1, column = 1)
bt_3 = Button(text = "3", width = 10, height = 3)
bt_3.grid(row = 1, column = 2)


#Luôn để xuống cuối dòng
window.mainloop()
#giống matplotlib
#mục tiêu tạo ra textbox này!!

# 24/5/2020, Tkinter

