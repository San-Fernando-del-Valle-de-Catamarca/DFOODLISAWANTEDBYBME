import tkinter as tk

class ChineseFoodVendingMachine:
    def __init__(self, master):
        self.master = master
        self.master.title("중국 음식 자판기")

        self.food_items = ['짜장면', '짬뽕', '탕수육', '볶음밥']
        self.stock = [5, 5, 5, 5]
        self.prices = [1000, 1500, 2000, 1200]
        self.balance = 0

        self.label_balance = tk.Label(master, text="현재 잔액: 0원")
        self.label_balance.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button_insert = tk.Button(master, text="돈 투입", command=self.insert_money)
        self.button_insert.pack()

        self.food_buttons = []
        for i in range(len(self.food_items)):
            button_text = f"{self.food_items[i]} - 가격: {self.prices[i]}원, 재고: {self.stock[i]}개"
            button = tk.Button(master, text=button_text, command=lambda idx=i: self.purchase(idx))
            self.food_buttons.append(button)
            button.pack()

        self.label_action = tk.Label(master, text="")
        self.label_action.pack()

    def insert_money(self):
        try:
            amount = int(self.entry.get())
            self.balance += amount
            self.label_balance.config(text=f"현재 잔액: {self.balance}원")
            self.entry.delete(0, tk.END)
            self.label_action.config(text="돈을 투입했습니다.")
        except ValueError:
            self.label_action.config(text="올바른 숫자를 입력하세요.")

    def purchase(self, idx):
        if self.stock[idx] > 0 and self.balance >= self.prices[idx]:
            self.stock[idx] -= 1
            self.balance -= self.prices[idx]
            self.label_balance.config(text=f"현재 잔액: {self.balance}원")
            self.label_action.config(text=f"{self.food_items[idx]} 구매 완료!")
            self.update_buttons()
        elif self.balance < self.prices[idx]:
            self.label_action.config(text="잔액이 부족합니다.")
        else:
            self.label_action.config(text="해당 음식 품절")

    def update_buttons(self):
        for i in range(len(self.food_items)):
            button_text = f"{self.food_items[i]} - 가격: {self.prices[i]}원, 재고: {self.stock[i]}개"
            self.food_buttons[i].config(text=button_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChineseFoodVendingMachine(root)
    root.mainloop()