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

#




root = tk.Tk()
root.title("Tools checker")
root.geometry("500x500")



title = tk.Label(root, text="Tools Checker", font=("Arial", 25), fg="Black", bg="white")
title.pack()

entry = tk.Entry(root, font=("Arial", 25), width=45)
entry.pack()

button = tk.Button(text="Check", fg="Black", bg="White", font=("Arial", 25))
button.pack()

bg_image = ImageTk.PhotoImage(Image.open("machines.jpg"))
bg_photo = tk.PhotoImage("bg_image")
tk.Label(root, image=bg_image).pack()

















root.mainloop()