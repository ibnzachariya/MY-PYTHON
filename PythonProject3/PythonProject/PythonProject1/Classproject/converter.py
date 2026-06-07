from tkinter import *

def dollar_to_naira():
    dollar = float(dollar_input.get())
    naira = dollar * 1600
    naira_result_label.config(text=f"{naira}")


window = Tk()
window.title("Dollar Converter")
window.config(padx=50, pady=50)

dollar_input = Entry(width=7)
dollar_input.grid(column=1, row=0)

dollar_label = Label(text="Dollar")
dollar_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to ")
is_equal_label.grid(column=0, row=1)

naira_result_label = Label(text="0")
naira_result_label.grid(column=1, row=1)

naira_label = Label(text="Naira")
naira_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=dollar_to_naira)
calculate_button.grid(column=1, row=2)









window.mainloop()