#Mục đích cần đạt được

import tkinter
import tkinter as tk

window = tk.Tk()
window.title("Chatbot")

# gui van ban
def send_text():
    user_text = text_box.get('1.0', tk.END)
    text_area.insert(tk.END, "You: " + user_text)
    text_box.delete("1.0", tk.END)
    computer_response(user_text)

def computer_response(text):
    if "hello" in text:
        computer_text = "hi, nice to meet you"
    text_area.insert(tk.END, "Computer: " + computer_text)

# Ô đối thoạik
text_area = tk.Text(width =40, height = 20)

# Ô nội dung trò chuyện
text_box = tk.Text(width = 40, height = 2)

# nút Clear
bt_clear = tk.Button(width = 10, height = 2, text = "Clear", command = lambda: text_area.delete(0, tk.END))

# nút send
bt_send = tk.Button(width = 10, height = 2, text = "send", command = lambda: send_text())

text_area.grid(row=0, column=0, padx=(15,5), pady=5)
text_box.grid(row=1, column=0, padx=(15,5), pady=5)
bt_clear.grid(row=0, column=1, sticky="N", padx=5, pady=5)
bt_send.grid(row=1, column=1, padx=5, pady=5)

window.mainloop()