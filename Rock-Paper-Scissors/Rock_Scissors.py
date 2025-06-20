import tkinter as tk
import random

window = tk.Tk()
window.title("Rock Paper Scissors Game")
window.geometry("400x400")
window.config(bg="#f0f0f0")


user_score = 0
computer_score = 0


choices = ["Rock", "Paper", "Scissors"]


def determine_winner(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)
    result = ""

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    score_label.config(text=f"You: {user_score}  |  Computer: {computer_score}")


def on_choice(choice):
    determine_winner(choice)


title_label = tk.Label(window, text="Rock, Paper, Scissors", font=("Arial", 18, "bold"), bg="#f0f0f0")
title_label.pack(pady=20)


button_frame = tk.Frame(window, bg="#f0f0f0")
button_frame.pack()

rock_button = tk.Button(button_frame, text="Rock", width=12, height=2, command=lambda: on_choice("Rock"))
paper_button = tk.Button(button_frame, text="Paper", width=12, height=2, command=lambda: on_choice("Paper"))
scissors_button = tk.Button(button_frame, text="Scissors", width=12, height=2, command=lambda: on_choice("Scissors"))

rock_button.grid(row=0, column=0, padx=10, pady=10)
paper_button.grid(row=0, column=1, padx=10, pady=10)
scissors_button.grid(row=0, column=2, padx=10, pady=10)


result_label = tk.Label(window, text="", font=("Arial", 14), bg="#f0f0f0")
result_label.pack(pady=20)


score_label = tk.Label(window, text="You: 0  |  Computer: 0", font=("Arial", 12), bg="#f0f0f0")
score_label.pack()


window.mainloop()
