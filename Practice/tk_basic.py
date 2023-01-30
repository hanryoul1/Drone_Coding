import tkinter as tk
import tkinter.messagebox as msbox

window = tk.Tk()
window.title("파이썬")
window.geometry("300x300")
window.resizable(False, False)

def click_button():
    # print("버튼을 클릭했습니다.")
    # button.config(bg = "blue") # 위젯 속성 변경

    # label.config(text = text.get("1.0", tk.END))
    label.config(text = entry.get())

    msbox.showinfo("알림", "버튼을 클릭했습니다.")
    
label = tk.Label(window, text = "레이블")
label.pack()

button = tk.Button(window, padx = 20, pady = 20, text = "버튼", command = click_button)
# button = tk.Button(window, width = 10, height = 3, text = "버튼")
# button = tk.Button(window, fg = "red", bg = "yellow", text = "버튼")
button.pack()

entry = tk.Entry(window) # 한 줄로만 입력 가능
entry.pack()

text = tk.Text(window, width = 100, height = 3) # 여러 줄로 입력 가능
text.insert(tk.END, "글자를 입력하세요")
text.pack()
 
window.mainloop()