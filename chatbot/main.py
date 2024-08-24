#Mục đích cần đạt được

import tkinter
import tkinter as tk

window = tk.Tk()
window.title("Chatbot")

# gui van ban
def send_text():


# Ô đối thoạik
text_area = tk.Text(width =40, height = 20)

# Ô nội dung trò chuyện
text_box = tk.Text(width = 40, height = 2)

# nút Clear
bt_clear = tk.Text(width = 10, height = 2, text = "Clear")

# nút send
bt_send = tk.Text(width = 10, height = 2, text = "send")

text_area.grid(row=0, column=0, padx=(15,5), pady=5)
text_box.grid(row=0, column=0, padx=(15,5), pady=5)


window.mainloop()