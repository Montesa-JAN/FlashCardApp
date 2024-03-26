from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
french_words_dict = {}
current_card = {}

try:
    data = pd.read_csv("./data/words_to_learn.csv.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    french_words_dict = original_data.to_dict(orient="records")
else:
    french_words_dict = data.to_dict(orient="records")


# Functions


def is_known():
    french_words_dict.remove(current_card)
    next_card()
    data = pd.DataFrame(french_words_dict)
    data.to_csv("./data/words_to_learn.csv", index=False)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(front, image=card_back_img)
    window.after(5000, func=flip_card)


def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(french_words_dict)
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(front, image=card_front_img)
    timer = window.after(5000, func=flip_card)


# Window
window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(5000, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
front = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

# Button
x_img = PhotoImage(file="./images/wrong.png")
x_button = Button(image=x_img, highlightthickness=0, command=next_card)
x_button.grid(row=1, column=0)

r_img = PhotoImage(file="./images/right.png")
r_button = Button(image=r_img, highlightthickness=0, command=is_known)
r_button.grid(row=1, column=1)

next_card()

window.mainloop()
