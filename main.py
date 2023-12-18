import tkinter as tk
from reversi_game import ReversiGame
from reversi_gui import ReversiGUI

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Reversi")
    reversi_game = ReversiGame()
    reversi_gui = ReversiGUI(root, reversi_game)
    root.mainloop()