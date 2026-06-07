import tkinter as tk
import time

class FocusKeeperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Focus Keeper")

        # Timer variables
        self.running = False
        self.remaining = 25 * 60  # default 25 minutes

        # Top bar
        top_frame = tk.Frame(root)
        top_frame.pack(pady=10)

        tk.Button(top_frame, text="Timer Option").pack(side="left", padx=5)
        tk.Button(top_frame, text="Report").pack(side="left", padx=5)
        tk.Button(top_frame, text="Login").pack(side="right", padx=5)

        # Timer label
        self.timer_label = tk.Label(root, text=self.format_time(self.remaining), font=("Helvetica", 48))
        self.timer_label.pack(pady=20)

        # Subtitle
        tk.Label(root, text="Focus Timer", font=("Helvetica", 16)).pack()

        # Mode buttons
        mode_frame = tk.Frame(root)
        mode_frame.pack(pady=20)

        tk.Button(mode_frame, text="Focus 25 min", command=lambda: self.set_timer(25*60)).pack(side="left", padx=10)
        tk.Button(mode_frame, text="Short Break 5 min", command=lambda: self.set_timer(5*60)).pack(side="left", padx=10)
        tk.Button(mode_frame, text="Long Break 30 min", command=lambda: self.set_timer(30*60)).pack(side="left", padx=10)

        # Control buttons
        control_frame = tk.Frame(root)
        control_frame.pack(pady=10)

        tk.Button(control_frame, text="Start", command=self.start_timer).pack(side="left", padx=10)
        tk.Button(control_frame, text="Pause", fg="red", command=self.pause_timer).pack(side="left", padx=10)
        tk.Button(control_frame, text="Reset", command=self.reset_timer).pack(side="left", padx=10)

    def format_time(self, seconds):
        mins = seconds // 60
        secs = seconds % 60
        return f"{mins:02}:{secs:02}"

    def update_timer(self):
        if self.running and self.remaining > 0:
            self.remaining -= 1
            self.timer_label.config(text=self.format_time(self.remaining))
            self.root.after(1000, self.update_timer)
        elif self.remaining == 0:
            self.timer_label.config(text="Time's up!")

    def start_timer(self):
        if not self.running:
            self.running = True
            self.update_timer()

    def pause_timer(self):
        self.running = False

    def reset_timer(self):
        self.running = False
        self.timer_label.config(text=self.format_time(self.remaining))

    def set_timer(self, seconds):
        self.running = False
        self.remaining = seconds
        self.timer_label.config(text=self.format_time(self.remaining))

if __name__ == "__main__":
    root = tk.Tk()
    app = FocusKeeperApp(root)
    root.mainloop()
