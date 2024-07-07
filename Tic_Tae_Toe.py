import tkinter as tk
from tkinter import messagebox
import random


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe AI GAME")

        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.window, text='', font=('Timesnewroman', 40), width=5, height=2,
                                               command=lambda row=i, col=j: self.click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

      
    def click(self, row, col):
        if self.board[row][col] == ' ' and self.current_player == 'X':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_win(self.current_player):
                self.game_over(self.current_player)
            elif self.board_full():
                self.game_over('Tie')
            else:
                self.current_player = 'O'
                self.ai_move()

    def ai_move(self):
        best_score = -float('inf')
        best_move = None

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'O'
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = ' '

                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        if best_move:
            row, col = best_move
            self.board[row][col] = 'O'
            self.buttons[row][col].config(text='O')

            if self.check_win('O'):
                self.game_over('O')
            elif self.board_full():
                self.game_over('Tie')
            else:
                self.current_player = 'X'

    def minimax(self, board, depth, is_maximizing):
        if self.check_win('O'):
            return 1
        elif self.check_win('X'):
            return -1
        elif self.board_full():
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'O'
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = ' '
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'X'
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = ' '
                        best_score = min(score, best_score)
            return best_score

    def check_win(self, player):
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)):  # Check row
                return True
            if all(self.board[j][i] == player for j in range(3)):  # Check column
                return True
        if all(self.board[i][i] == player for i in range(3)):  # Check diagonal
            return True
        if all(self.board[i][2 - i] == player for i in range(3)):  # Check anti-diagonal
            return True
        return False

    def board_full(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))

    def game_over(self, winner):
        if winner == 'Tie':
            messagebox.showinfo("Tic Tac Toe AI GAME ", "oohhh!!!  NO , The game is a tie!")
            exit()
        else:
            messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!!!!!")
            exit()
           
        
    def run(self):
        self.window.mainloop()

game = TicTacToe()
game.run()
