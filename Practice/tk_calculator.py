import tkinter as tk

window = tk.Tk()
window.title("계산기")

label_result = tk.Label(window, text = "0")
label_result.grid(row = 0, column = 0, columnspan = 5)

button_1 = tk.Button(window, text = "7")
button_1.grid(row = 1, column = 0)
button_2 = tk.Button(window, text = "8")
button_2.grid(row = 1, column = 1)
button_3 = tk.Button(window, text = "9")
button_3.grid(row = 1, column = 2)
button_4 = tk.Button(window, text = "/")
button_4.grid(row = 1, column = 3)

button_5 = tk.Button(window, text = "4")
button_5.grid(row = 2, column = 0)
button_6 = tk.Button(window, text = "5")
button_6.grid(row = 2, column = 1)
button_7 = tk.Button(window, text = "6")
button_7.grid(row = 2, column = 2)

# ----- 2분-----