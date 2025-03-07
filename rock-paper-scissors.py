from tkinter import *
from PIL import Image, ImageTk
import random

# Initialize the main window
root = Tk()
root.title("Rock Paper Scissors")
root.geometry("500x600")
root.configure(background="blue")

# Load images for Rock, Paper, and Scissors
rock_img = ImageTk.PhotoImage(Image.open("rock.png").resize((100, 100)))
paper_img = ImageTk.PhotoImage(Image.open("paper.png").resize((100, 100)))
scissors_img = ImageTk.PhotoImage(Image.open("scissors.png").resize((100, 100)))

# Choices
choices = ["rock", "paper", "scissors"]


def play(choice):
    user_choice.set(choice)
    computer_choice.set(random.choice(choices))

    if user_choice.get() == computer_choice.get():
        result.set("It's a tie!")
    elif (
        (user_choice.get() == "rock" and computer_choice.get() == "scissors") or
        (user_choice.get() == "paper" and computer_choice.get() == "rock") or
        (user_choice.get() == "scissors" and computer_choice.get() == "paper")
    ):
        result.set("You Win!")
    else:
        result.set("You Lose!")


user_choice = StringVar()
computer_choice = StringVar()
result = StringVar()


Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"), bg="blue", fg="white").pack(pady=10)


Label(root, text="Your Choice:", font=("Arial", 14), bg="blue", fg="white").pack(pady=5)
Label(root, textvariable=user_choice, font=("Arial", 16), bg="blue", fg="yellow").pack()

Label(root, text="Computer's Choice:", font=("Arial", 14), bg="blue", fg="white").pack(pady=5)
Label(root, textvariable=computer_choice, font=("Arial", 16), bg="blue", fg="yellow").pack()


Label(root, text="Choose:", font=("Arial", 14), bg="blue", fg="white").pack(pady=5)
frame = Frame(root, bg="blue")
frame.pack(pady=10)

Button(frame, image=rock_img, command=lambda: play("rock")).grid(row=0, column=0, padx=10)
Button(frame, image=paper_img, command=lambda: play("paper")).grid(row=0, column=1, padx=10)
Button(frame, image=scissors_img, command=lambda: play("scissors")).grid(row=0, column=2, padx=10)


Label(root, text="Result:", font=("Arial", 14), bg="blue", fg="white").pack(pady=5)
Label(root, textvariable=result, font=("Arial", 18), bg="blue", fg="green").pack(pady=10)


root.mainloop()