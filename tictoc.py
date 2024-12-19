import tkinter as tk
from tkinter import messagebox

# Function to check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([spot == player for spot in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# Function to check if the board is full (draw)
def is_full(board):
    return all(spot != ' ' for row in board for spot in row)

# Function to handle button clicks
def button_click(row, col):
    global current_player
    
    # If the spot is already taken, do nothing
    if board[row][col] != ' ':
        return
    
    # Update the board
    board[row][col] = current_player
    buttons[row][col].config(text=current_player)
    
    # Check if the current player has won
    if check_win(board, current_player):
        messagebox.showinfo("Game Over", f"Player {current_player} wins!")
        reset_game()
        return
    
    # Check if the game is a draw
    if is_full(board):
        messagebox.showinfo("Game Over", "It's a draw!")
        reset_game()
        return
    
    # Switch player
    current_player = 'O' if current_player == 'X' else 'X'

# Function to reset the game
def reset_game():
    global current_player, board
    current_player = 'X'
    board = [[' ' for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text='')

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Initialize the game variables
current_player = 'X'
board = [[' ' for _ in range(3)] for _ in range(3)]

# Create the buttons for the Tic-Tac-Toe grid
buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=' ', font=('normal', 40), width=5, height=2,
                                  command=lambda row=i, col=j: button_click(row, col))
        buttons[i][j].grid(row=i, column=j)

# Start the main event loop
root.mainloop()
