import tkinter as tk
import tkinter.messagebox as msbox

window = tk.Tk()
window.title("파이썬")

frame1 = tk.Frame(window, relief = "solid", bd = 1, padx = 5, pady = 5)
frame1.pack(side = "left", fill = "both", expand = True)
# side : 어느 방향에 놓을지 / left, right, top, bottom
# fill : 어느 방향으로 채울지 / x, y, both
frame1.pack()

button1 = tk.Button(frame1, text = "frame1")
button1.pack()
button2 = tk.Button(frame1, text = "frame1")
button2.pack()
button3 = tk.Button(frame1, text = "frame1")
button3.pack()

frame2 = tk.Frame(window, relief = "solid", bd = 1, padx = 5, pady = 5)
frame2.pack()
button4 = tk.Button(frame2, text = "frame2")
button4.pack()
button5 = tk.Button(frame2, text = "frame2")
button5.pack()
button6 = tk.Button(frame2, text = "frame2")
button6.pack()

window.mainloop()