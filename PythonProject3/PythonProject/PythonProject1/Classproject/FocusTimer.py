from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer_id = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, timer_id
    if timer_id:
        window.after_cancel(timer_id)
    reps = 0
    my_label.config(text="25:00")
    timer.config(text="Focus Timer")
    status_label.config(text="Status: Ready")
    session_label.config(text="Sessions Completed: 0")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Long Break", fg="red")
        status_label.config(text="Status: Relax")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Short Break", fg="orange")
        status_label.config(text="Status: Rest")
    else:
        count_down(work_sec)
        timer.config(text="Focus Timer", fg="green")
        status_label.config(text="Status: Working")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer_id
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    my_label.config(text=f"{minutes}:{seconds}")
    if count > 0:
        timer_id = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        completed_sessions = math.floor(reps / 2)
        session_label.config(text=f"Sessions Completed: {completed_sessions}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Smart Study Tracker")
window.config(padx=20, pady=20)

timer = Label(window, text="Focus Timer", font=("Arial", 20))
timer.grid(row=0, column=0, columnspan=2, pady=10)

my_label = Label(text="25:00", font=("Arial", 50))
my_label.grid(row=1, column=0, columnspan=2, pady=20)

status_label = Label(text="Status: Ready", font=("Arial", 15))
status_label.grid(row=2, column=0, columnspan=2, pady=10)

session_label = Label(text="Sessions Completed: 0", font=("Arial", 15))
session_label.grid(row=3, column=0, columnspan=2, pady=10)

start_button = Button(text="Start", width=15, command=start_timer)
start_button.grid(row=4, column=0, pady=10)

reset_button = Button(text="Reset", width=15, command=reset_timer)
reset_button.grid(row=4, column=1, pady=10)

statistics_button = Button(text="Statistics", width=20)
statistics_button.grid(row=5, column=0, columnspan=2, pady=10)

window.mainloop()
