import tkinter as tk
import random

# ---------------------------- DATA ------------------------------- #
# Simple word list (front: English, back: French)
flashcards = [
    {"English": "Apple", "French": "Pomme"},
    {"English": "Book", "French": "Livre"},
    {"English": "Car", "French": "Voiture"},
    {"English": "House", "French": "Maison"},
    {"English": "Dog", "French": "Chien"},
]

current_card = {}
flip_timer = None

# ---------------------------- FUNCTIONS ------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # cancel previous flip
    current_card = random.choice(flashcards)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["English"], fill="black")
    canvas.itemconfig(card_bg, fill="white")
    flip_timer = window.after(3000, flip_card)  # flip after 3 seconds

def flip_card():
    canvas.itemconfig(card_title, text="French", fill="red")
    canvas.itemconfig(card_word, text=current_card["French"], fill="red")
    canvas.itemconfig(card_bg, fill="lightyellow")

def known_card():
    flashcards.remove(current_card)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg="lightblue")

flip_timer = window.after(3000, flip_card)

canvas = tk.Canvas(width=400, height=250, bg="white", highlightthickness=0)
card_bg = canvas.create_rectangle(0, 0, 400, 250, fill="white")
card_title = canvas.create_text(200, 50, text="", font=("Arial", 20, "italic"))
card_word = canvas.create_text(200, 125, text="", font=("Arial", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_button = tk.Button(text="❌ Wrong", command=next_card)
wrong_button.grid(row=1, column=0)

right_button = tk.Button(text="✅ Right", command=known_card)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()

