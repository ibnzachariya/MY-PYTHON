from tkinter import *

window = Tk()
window.title("Place Example")
window.geometry("300x200")

label = Label(text="Timer", font=("Arial", 20))
label.place(x=100, y=20)   # exact coordinates

time_display = Label(text="25:00", font=("Arial", 40))
time_display.place(x=80, y=70)

start_button = Button(text="Start", width=10)
start_button.place(x=50, y=150)

reset_button = Button(text="Reset", width=10)
reset_button.place(x=160, y=150)

window.mainloop()
