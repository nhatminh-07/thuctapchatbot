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

# H2
bt_4 = Button(text = "4", width = 10, height = 3)
bt_4.grid(row = 2, column = 0)
bt_5 = Button(text = "5", width = 10, height = 3)
bt_5.grid(row = 2, column = 1)
bt_6 = Button(text = "6", width = 10, height = 3)
bt_6.grid(row = 2, column = 2)

# H3
bt_7 = Button(text = "7", width = 10, height = 3)
bt_7.grid(row = 3, column = 0)
bt_8 = Button(text = "8", width = 10, height = 3)
bt_8.grid(row = 3, column = 1)
bt_9 = Button(text = "9", width = 10, height = 3)
bt_9.grid(row = 3, column = 2)

# H0
bt_0 = Button(text = "0", width = 10, height = 3)
bt_0.grid(row = 4, column = 1)

#Luôn để xuống cuối dòng
window.mainloop()
#giống matplotlib
#mục tiêu tạo ra textbox này!!

# 24/5/2020, Tkinter

