from tkinter import *
import math

WORK_MIN = 1
timer_id = None
reps = 0

def reset_timer():
    global timer_id, reps
    if timer_id:
        window.after_cancel(timer_id)
    reps = 0
    my_label.config(text=f"{WORK_MIN}:00")
    timer.config(text="Focus Timer", fg="black")
    status_label.config(text="Status: Ready")
    session_label.config(text="Sessions Completed: 0")

def start_timer():
    work_sec = WORK_MIN * 60
    count_down(work_sec)
    timer.config(text="Counting Down...", fg="green")
    status_label.config(text="Status: Running")

def count_down(count):
    global timer_id, reps
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    my_label.config(text=f"{minutes}:{seconds}")
    if count > 0:
        timer_id = window.after(1000, count_down, count - 1)
    else:
        reps += 1
        session_label.config(text=f"Sessions Completed: {reps}")
        timer.config(text="Time's Up!", fg="red")
        status_label.config(text="Status: Finished")

def show_statistics():
    stats_window = Toplevel(window)
    stats_window.title("Statistics")
    Label(stats_window, text=f"Total Sessions Completed: {reps}", font=("Arial", 15)).pack(padx=20, pady=20)

# ---------------------------- UI ------------------------------- #
window = Tk()
window.title("Smart Study Tracker")
window.config(padx=20, pady=20)

timer = Label(window, text="Focus Timer", font=("Arial", 20))
timer.grid(row=0, column=0, columnspan=2, pady=10)

my_label = Label(text=f"{WORK_MIN}:00", font=("Arial", 50))
my_label.grid(row=1, column=0, columnspan=2, pady=20)

session_label = Label(text="Sessions Completed: 0", font=("Arial", 20))
session_label.grid(row=2, column=0, columnspan=2, pady=10)

status_label = Label(text="Status: Ready", font=("Arial", 15))
status_label.grid(row=3, column=0, columnspan=2, pady=10)

start_button = Button(text="Start", width=15, command=start_timer)
start_button.grid(row=4, column=0, pady=10)

reset_button = Button(text="Reset", width=15, command=reset_timer)
reset_button.grid(row=4, column=1, pady=10)

statistics_button = Button(text="Statistics", width=20, command=show_statistics)
statistics_button.grid(row=5, column=0, columnspan=2, pady=10)

window.mainloop()
