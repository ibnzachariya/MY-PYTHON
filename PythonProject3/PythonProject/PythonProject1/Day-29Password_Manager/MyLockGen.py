import tkinter as tk
from tkinter import messagebox
import random
import string

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%^&*()"
    all_chars = letters + digits + symbols
    password = "".join(random.choice(all_chars) for _ in range(12))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website == "" or username == "" or password == "":
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        with open("data.txt", "a") as file:
            file.write(f"{website} | {username} | {password}\n")
        messagebox.showinfo(title="Saved", message="Your details have been saved successfully!")
        website_entry.delete(0, tk.END)
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")

# Logo image
logo_img = tk.PhotoImage(file="logo.png")
logo_label = tk.Label(image=logo_img)
logo_label.grid(column=1, row=0)

# Labels
tk.Label(text="Website:").grid(column=0, row=1)
tk.Label(text="Username/Email:").grid(column=0, row=2)
tk.Label(text="Password:").grid(column=0, row=3)

# Entries
website_entry = tk.Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)

username_entry = tk.Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = tk.Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
generate_button = tk.Button(text="Generate", width=10, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
