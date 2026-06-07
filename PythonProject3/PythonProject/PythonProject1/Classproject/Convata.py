import tkinter as tk

RATE = 1300  # 1 Dollar = 1300 Naira

def convert():
    dollar = float(dollar_input.get())
    naira = dollar * RATE
    result_label.config(text=f"is equal to {naira:.2f} Naira")

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Dollar to Naira Converter")
window.minsize(width= 500, height=500)

# Dollar entry
dollar_input = tk.Entry(width=10)
dollar_input.grid(column=1, row=0, pady=10)

# Dollar label
dollar_label = tk.Label(text="Dollar")
dollar_label.grid(column=2, row=0, pady=10)

# Result label
result_label = tk.Label(text="is equal to 0 Naira")
result_label.grid(column=1, row=1, columnspan=2, pady=10)

# Convert button
convert_button = tk.Button(text="Calculate", command=convert)
convert_button.grid(column=1, row=2, columnspan=2, pady=10)

window.mainloop()
