"""
Machine Data Checker
Author: Abdulfatai
Description:
Enter an oil & gas machine name, see its use and maintenance.
"""

import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"

machines = {
    "drill": {"emoji": "🛠️", "use": "Drills boreholes for oil extraction.", "maintenance": "Lubricate regularly, check drill bits."},
    "pump": {"emoji": "⛽", "use": "Pumps crude oil and gas.", "maintenance": "Inspect seals, clean filters."},
    "valve": {"emoji": "🚪", "use": "Controls flow of oil/gas.", "maintenance": "Test pressure, replace worn parts."},
    "compressor": {"emoji": "💨", "use": "Compresses gas for transport.", "maintenance": "Check bearings, monitor vibration."},
    "generator": {"emoji": "⚡", "use": "Provides electrical power for rigs.", "maintenance": "Check fuel, clean spark plugs."},
    "pipeline": {"emoji": "🛤️", "use": "Transports oil and gas over long distances.", "maintenance": "Inspect leaks, monitor pressure."},
    "separator": {"emoji": "⚙️", "use": "Separates oil, gas, and water.", "maintenance": "Clean filters, check corrosion."},
    "storage tank": {"emoji": "🛢️", "use": "Stores crude oil safely.", "maintenance": "Inspect walls, monitor temperature."}
}

def check_machine():
    name = entry.get().lower()
    if name in machines:
        result = machines[name]

        # Create popup
        popup = tk.Toplevel(root)
        popup.title(f"{result['emoji']} {name.capitalize()} Info")
        popup.geometry("400x250")
        popup.configure(bg="#eef2f7")

        # Show info
        tk.Label(
            popup,
            text=f"{result['emoji']} {name.capitalize()}\n\n"
                 f"✅ Use: {result['use']}\n"
                 f"🛠️ Maintenance: {result['maintenance']}",
            font=text_font,
            wraplength=350,
            justify="left",
            bg="#eef2f7"
        ).pack(pady=20)

        # Close popup on any key press
        popup.bind("<Key>", lambda e: popup.destroy())

        # Send data to API
        payload = {"title": f"Machine: {name}", "body": result["use"], "userId": 1}
        requests.post(API_URL, json=payload)
    else:
        popup = tk.Toplevel(root)
        popup.title("Error")
        popup.geometry("300x150")
        popup.configure(bg="#f8d7da")

        tk.Label(
            popup,
            text="❌ Machine not found.\nTry another name.",
            font=text_font,
            fg="#721c24",
            bg="#f8d7da"
        ).pack(pady=20)

        # Close popup on any key press
        popup.bind("<Key>", lambda e: popup.destroy())


root = tk.Tk()
root.title("⚙️ Machine Data Checker 🛢️")
root.geometry("650x450")

# Background image (you already saved machines.jpg in the folder)
bg_image = Image.open("machines.jpg").resize((650, 450))
bg_photo = ImageTk.PhotoImage(bg_image)
tk.Label(root, image=bg_photo).place(x=0, y=0, relwidth=1, relheight=1)

title_font = font.Font(family="Helvetica", size=22, weight="bold")
text_font = font.Font(family="Arial", size=12)

tk.Label(root, text="⚙️ Oil & Gas Machine Data Checker 🛢️", font=title_font,
         fg="#004080", bg="#eef2f7").pack(pady=15)
entry = tk.Entry(root, width=35, font=text_font)
entry.pack(pady=10)

tk.Button(root, text="🔍 Check Machine", command=check_machine, bg="#007BFF",
          fg="white", font=text_font).pack(pady=10)
output = tk.Label(root, text="", font=text_font, wraplength=550, justify="left", bg="#eef2f7")
output.pack(pady=20)

root.mainloop()
