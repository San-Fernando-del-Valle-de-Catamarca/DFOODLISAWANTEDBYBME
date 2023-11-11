import tkinter as tk
from tkinter import messagebox
import random

# 상수 정의
GRID_SIZE = 15
NUM_MINES = 35

# 게임 초기화
root = tk.Tk()
root.title("지뢰찾기")

# 지뢰 필드 초기화
field = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
mines = random.sample(range(GRID_SIZE**2), NUM_MINES)

for idx in mines:
    row, col = divmod(idx, GRID_SIZE)
    field[row][col] = -1

# 추가 기능 변수
flagged = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
revealed = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# 지뢰의 개수 계산
num_mines = NUM_MINES

# GUI 함수 정의
def click(row, col):
    if field[row][col] == -1:
        reveal_mines()
        messagebox.showinfo("게임 종료", "지뢰를 클릭했습니다!\n게임 오버!")
        root.quit()
    elif field[row][col] == 0:
        reveal_empty_cells(row, col)
    else:
        revealed[row][col] = True
        buttons[row][col].config(text=str(field[row][col]), state='disabled', bg='black', fg='white')

def count_adjacent_mines(row, col):
    count = 0
    for i in range(max(0, row - 1), min(GRID_SIZE, row + 2)):
        for j in range(max(0, col - 1), min(GRID_SIZE, col + 2)):
            if field[i][j] == -1:
                count += 1
    return count

def reveal_empty_cells(row, col):
    if revealed[row][col]:
        return
    revealed[row][col] = True
    buttons[row][col].config(state='disabled', bg='black', fg='white')
    count = count_adjacent_mines(row, col)
    if count == 0:
        for i in range(max(0, row - 1), min(GRID_SIZE, row + 2)):
            for j in range(max(0, col - 1), min(GRID_SIZE, col + 2)):
                reveal_empty_cells(i, j)
    else:
        buttons[row][col].config(text=str(count))

def reveal_mines():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if field[i][j] == -1:
                if flagged[i][j]:
                    buttons[i][j].config(text='지뢰', state='disabled', disabledforeground='red', bg='black', fg='white')
                else:
                    buttons[i][j].config(text='지뢰', state='disabled', disabledforeground='red', bg='black', fg='white')
            elif flagged[i][j]:
                buttons[i][j].config(text='깃발', bg='black', fg='white')

def flag(row, col):
    if revealed[row][col]:
        return
    flagged[row][col] = not flagged[row][col]
    if flagged[row][col]:
        buttons[row][col].config(text='깃발', bg='black', fg='white')
    else:
        buttons[row][col].config(text='', bg='black', fg='white')

# 우클릭 이벤트 처리
def on_right_click(event, row, col):
    flag(row, col)
    # 우클릭 이벤트를 무시
    return "break"

# 남은 지뢰 개수 업데이트
def update_mines_label():
    mines_label.config(text=f"지뢰 수: {num_mines}")

# GUI 생성
buttons = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        buttons[i][j] = tk.Button(root, width=4, height=1,
                                  command=lambda row=i, col=j: click(row, col), bg='gray', font=('Arial', 16))  # Added font parameter here
        buttons[i][j].grid(row=i, column=j, padx=1, pady=1)
        buttons[i][j].bind("<Button-3>", lambda event, row=i, col=j: on_right_click(event, row, col))


# 지뢰 수 표시 라벨
mines_label = tk.Label(root, text=f"지뢰 수: {num_mines}")
mines_label.grid(row=GRID_SIZE+1, column=1, columnspan=GRID_SIZE, padx=10, pady=10)

root.mainloop()