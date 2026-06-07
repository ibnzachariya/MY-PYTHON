from tkinter import *

window = Tk()
window.title("Pack Example")

label = Label(text="Timer", font=("Arial", 20))
label.pack(pady=10)

time_display = Label(text="25:00", font=("Arial", 40))
time_display.pack(pady=20)

frame = Frame(window)
frame.pack(pady=10)

start_button = Button(frame, text="Start", width=10)
start_button.pack(side="left", padx=5)

reset_button = Button(frame, text="Reset", width=10)
reset_button.pack(side="left", padx=5)

window.mainloop()
