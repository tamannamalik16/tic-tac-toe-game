import tkinter as tk  
from tkinter import messagebox                        # it used to create pop-up dialog boxes, useful for notifications (like when a player wins).

def check_winner():                       # This function checks if there's a winner. It looks at predefined winning combinations of button indices
    for combo in [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] !="":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins! ")
            winner = True      # Set winner to True when someone wins
            root.quit()        # Exit the function
            
def button_click(index):                                          # This function is called when a button is clicked. It updates the button’s text to the current player’s symbol (either "X" or "O").
    if buttons[index]["text"] == "" and not winner:             #  first checks if the button is empty ("") and if no player has won (not winner).
        buttons[index]["text"] = current_player
        check_winner()                                          # Calls check_winner() to see if this move resulted in a win
        toggle_player()                                         #  Calls toggle_player() to switch to the other player
        
def toggle_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"
    label.config(text=f"Player {current_player}'s turn")         # It updates the label to indicate whose turn it is.
    
root = tk.Tk()                                                   # root is the main window of the application. Tk() initializes this window.
root.title("Tic-Tac-Toe")


# creates 9 buttons for the Tic-Tac-Toe grid, lambda ensures that the correct index is passed to button_click when a button is clicked.

buttons = [tk.Button(root, text="", font=("normal",25),width=5,height=2,command=lambda i=i: button_click(i)) for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i //3, column=i% 3)
                                               # This loop arranges buttons in a 3x3 grid using integer division and modulus for row and column placement.

# Initializing Variables
    
current_player = "X"                 # is initialized to "X", meaning player X goes first.
winner = False                       #  is set to False initially, indicating no winner yet.
label = tk.Label(root, text=f"Player {current_player}'s turn",font=("normal",16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()                       # This keeps the window open and responsive to user actions like button clicks.

                        