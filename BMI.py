import tkinter as tk
from tkinter import filedialog

# 그림판 초기화 함수
def clear_canvas():
    canvas.delete("all")

# 그림 저장 함수
def save_image():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        canvas.postscript(file=file_path, colormode='color')

# 마우스 클릭 이벤트 핸들러
def on_canvas_click(event):
    x, y = event.x, event.y
    canvas.create_line(x, y, x+1, y+1, fill=current_color, width=line_width, capstyle=tk.ROUND, smooth=tk.TRUE)

# 색상 선택 함수
# 색상 선택 함수
def choose_color(value):
    global current_color
    current_color = value


# 초기화 및 저장 버튼 생성
root = tk.Tk()
root.title("간단한 그림판")

canvas = tk.Canvas(root, bg="white", width=800, height=600)
canvas.pack(expand=tk.YES, fill=tk.BOTH)

clear_button = tk.Button(root, text="초기화", command=clear_canvas)
clear_button.pack(side=tk.LEFT)

save_button = tk.Button(root, text="저장", command=save_image)
save_button.pack(side=tk.LEFT)

# 색상 선택 메뉴
colors = ["black", "OrangeRed", "green", "blue","yellow","gold","silver","purple","aquamarine","orange","violet"]
color_var = tk.StringVar(root)
color_var.set(colors[0])
color_menu = tk.OptionMenu(root, color_var, *colors, command=choose_color)
color_menu.pack(side=tk.LEFT)

# 현재 색상 및 선 굵기 설정
current_color = color_var.get()
line_width = 2

# 마우스 클릭 이벤트 바인딩
canvas.bind("<B1-Motion>", on_canvas_click)

root.mainloop()
