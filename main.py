import random
import tkinter as tk
from tkinter import messagebox

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "scissors" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    global user_score, computer_score
    choices = ["rock", "paper", "scissors"]
    user_choice = user_choice_var.get()
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    messagebox.showinfo("Result", f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}")

    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

    score_label.config(text=f"User: {user_score}  Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text=f"User: {user_score}  Computer: {computer_score}")
    user_choice_var.set("")


app = tk.Tk()
app.title("Rock-Paper-Scissors Game")
app.geometry("500x500")

user_score = 0
computer_score = 0


user_choice_label = tk.Label(app, text="Choose: rock, paper, or scissors",font=("open sans", 12, "bold"))
user_choice_label.pack(pady=10)

user_choice_var = tk.StringVar()
user_choice_entry = tk.Entry(app, textvariable=user_choice_var)
user_choice_entry.pack(pady=10)

play_button = tk.Button(app, text="Play", command=play_game,bg="green",fg="white", height=2, width=10, relief=tk.RAISED, borderwidth=3)
play_button.pack(pady=10)

score_label = tk.Label(app, text=f"User: {user_score}  Computer: {computer_score}",font=("open sans", 12, "bold"))
score_label.pack(pady=10)

play_again_button = tk.Button(app, text="Play Again", command=reset_game,fg="white",bg="red", height=2, width=10, relief=tk.RAISED, borderwidth=3)
play_again_button.pack(pady=10)

app.mainloop()