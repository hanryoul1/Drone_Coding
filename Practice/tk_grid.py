import tkinter as tk
import tkinter.messagebox as msgbox

window = tk.Tk()
window.title("파이썬")

# row = 행, column = 열

# columspan, rowspan : 몇 칸 차지할지 정하기
# columspan : 가로, rowspan : 세로

# stickly : 크기 늘리기 , news : 모든 방향으로 늘리기
 
button1 = tk.Button(window, text = "1")
button1.grid(row = 0, column = 0, columnspan = 2, sticky="news")
button2 = tk.Button(window, text = "2")
button2.grid(row = 1, column = 0)
button3 = tk.Button(window, text = "3")
button3.grid(row = 1, column = 1)


window.mainloop()