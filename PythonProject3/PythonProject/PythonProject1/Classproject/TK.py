from tkinter import *

window = Tk()
window.title("GUI Program Practice")
window.minsize(width=500, height=500)

# the label
the_label = Label(text="The Practice", font=("Arial", 24, "italic"))
the_label.pack() #without formatting the text to the left or right, default is center

the_label["text"] = "Practice" #this is to change something in the label like the text
the_label.config(text="Practice") # Or like this

# Button

def button_clicked():
    print("button_clicked")
    the_label.config(text="button_clicked") #now the Practice gets changed to button_clicked the click button is clicked


button = Button(text="Click", command=button_clicked)
button.pack()

#Entry
input = Entry(width=10)
input.pack()


window.mainloop()






window.mainloop()