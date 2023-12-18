import tkinter as tk
from tkinter import messagebox


class ReversiGUI:
    BOARD_SIZE = 8
    BUTTON_WIDTH = 7
    BUTTON_HEIGHT = 3
    def __init__(self, master, reversi):
        self.master = master
        self.reversi = reversi
        self.buttons = [[None] * self.BOARD_SIZE for _ in range(self.BOARD_SIZE)]
        self.create_board()
        self.create_score_display()

    def create_board(self):
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                self.buttons[i][j] = tk.Button(self.master, text='', width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT,
                                               command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)
        self.update_board()

    def create_score_display(self):
        score_label = tk.Label(self.master, text="Rezultatas:")
        score_label.grid(row=self.BOARD_SIZE, column=0, columnspan=self.BOARD_SIZE)

        for player in ['X', 'O']:
            score_value = tk.StringVar()
            score_value.set(f"{player}: {self.reversi.get_score(player)}")
            score_label = tk.Label(self.master, textvariable=score_value)
            score_label.grid(row=9, column=['X', 'O'].index(player), sticky='nsew')

    def update_board(self):
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                if self.reversi.is_valid_move(i, j):
                    self.buttons[i][j].config(text='', bg='orange')
                else:
                    self.buttons[i][j].config(text=self.reversi.board[i][j],
                                              bg='white' if (i + j) % 2 == 0 else 'light gray')

    def make_move(self, row, col):
        self.reversi.make_move(row, col)
        self.update_board()
        self.update_scores_display()
        if self.reversi.is_game_over():
            self.show_game_over_message()

    def update_scores_display(self):
        for player in ['X', 'O']:
            score_value = tk.StringVar()
            score_value.set(f"{player}: {self.reversi.get_score(player)}")
            score_label = tk.Label(self.master, textvariable=score_value)
            score_label.grid(row=9, column=['X', 'O'].index(player), sticky='nsew')

    def show_game_over_message(self):
        winner = self.reversi.get_winner()
        result = f"Žaidimas baigtas!! {'Lygiosios' if winner == 'Lygiosios' else f'{winner} laimėjo'}."
        messagebox.showinfo("Žaidimas baigtas!", result)
        self.master.destroy()
