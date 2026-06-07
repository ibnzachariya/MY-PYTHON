import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk   # Pillow library for image handling

def evaluate_status(status):
    return status.lower() in ["working", "ok", "good"]

class EquipmentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Equipment Monitoring System v3")
        self.root.geometry("600x450")

        # Variables
        self.total_equipment = 0
        self.current_index = 0
        self.faulty_count = 0
        self.working_count = 0
        self.equipment_data = []

        # Background image
        bg_image = Image.open("foto.png")
        bg_image = bg_image.resize((500, 350))  # smaller than window
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        bg_label = tk.Label(root, image=self.bg_photo)
        bg_label.place(relx=0.5, rely=0.5, anchor="center")  # centered
        bg_label.lower()  # send background behind widgets

        # Main frame
        self.frame = tk.Frame(root, bg="#34495e", bd=5)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        self.label = tk.Label(self.frame, text="Enter number of equipment to check:",
                              font=("Arial", 12), fg="white", bg="#34495e")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.frame, font=("Arial", 12), bg="#ecf0f1")
        self.entry.pack(pady=5)

        self.start_button = tk.Button(self.frame, text="Start Inspection",
                                      font=("Arial", 12, "bold"),
                                      bg="#27ae60", fg="white",
                                      command=self.start_inspection)
        self.start_button.pack(pady=10)

    def start_inspection(self):
        try:
            self.total_equipment = int(self.entry.get())
            if self.total_equipment <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive number.")
            return

        self.label.config(text=f"Enter name of equipment {self.current_index + 1}:")
        self.entry.delete(0, tk.END)
        self.start_button.config(text="Next", bg="#2980b9", command=self.next_equipment)

    def next_equipment(self):
        if self.current_index < self.total_equipment:
            name = self.entry.get().strip()
            if not name:
                messagebox.showerror("Error", "Please enter a valid equipment name.")
                return

            self.equipment_data.append({"name": name})
            self.label.config(text=f"Enter status of {name} (working/faulty):")
            self.entry.delete(0, tk.END)
            self.start_button.config(text="Save Status", bg="#8e44ad", command=self.save_status)
        else:
            self.show_summary()

    def save_status(self):
        status = self.entry.get().strip()
        if not status:
            messagebox.showerror("Error", "Please enter a valid status.")
            return

        if evaluate_status(status):
            self.working_count += 1
        else:
            self.faulty_count += 1

        self.equipment_data[self.current_index]["status"] = status
        self.current_index += 1

        if self.current_index < self.total_equipment:
            self.label.config(text=f"Enter name of equipment {self.current_index + 1}:")
            self.entry.delete(0, tk.END)
            self.start_button.config(text="Next", bg="#2980b9", command=self.next_equipment)
        else:
            self.show_summary()

    def show_summary(self):
        # Clear frame
        for widget in self.frame.winfo_children():
            widget.destroy()

        summary = f"Inspection complete:\n{self.faulty_count} faulty, {self.working_count} working"
        tk.Label(self.frame, text=summary, font=("Arial", 14, "bold"),
                 fg="yellow", bg="#34495e").pack(pady=10)

        # Search bar for status check
        tk.Label(self.frame, text="Check equipment status:",
                 font=("Arial", 12), fg="white", bg="#34495e").pack(pady=5)

        self.search_entry = tk.Entry(self.frame, font=("Arial", 12), bg="#ecf0f1")
        self.search_entry.pack(pady=5)

        search_button = tk.Button(self.frame, text="Check Status", font=("Arial", 12, "bold"),
                                  bg="#3498db", fg="white", command=self.check_status)
        search_button.pack(pady=5)

        exit_button = tk.Button(self.frame, text="Exit", font=("Arial", 12, "bold"),
                                bg="#c0392b", fg="white", command=self.root.quit)
        exit_button.pack(pady=10)

    def check_status(self):
        name = self.search_entry.get().strip()
        for eq in self.equipment_data:
            if eq["name"].lower() == name.lower():
                status = eq["status"]
                color = "green" if evaluate_status(status) else "red"
                messagebox.showinfo("Status Check", f"{eq['name']} is {status.upper()}")
                return
        messagebox.showwarning("Not Found", "Equipment not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = EquipmentApp(root)
    root.mainloop()
