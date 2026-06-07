from tkinter import *

window = Tk()
window.title("Grid Example")

label = Label(text="Timer", font=("Arial", 20))
label.grid(row=0, column=0, columnspan=2, pady=10)

time_display = Label(text="25:00", font=("Arial", 40))
time_display.grid(row=1, column=0, columnspan=2, pady=20)

start_button = Button(text="Start", width=10)
start_button.grid(row=2, column=0, padx=5, pady=10)

reset_button = Button(text="Reset", width=10)
reset_button.grid(row=2, column=1, padx=5, pady=10)

window.mainloop()
