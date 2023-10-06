import tkinter.messagebox
from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

title_label = Label(text="Miles to Km Converter", font=("Arial", 20, "bold"))
title_label.grid(row=0, column=0, columnspan=3)

mile_label = Label(text="Miles: ", font=("Arial", 10, "normal"))
mile_label.grid(row=1, column=0)
mile_entry = Entry(width=20, justify="center")
mile_entry.grid(row=1, column=1)

km_label = Label(text="KM: ", font=("Arial", 10, "normal"), justify="center")
km_label.grid(row=2, column=0)
km_entry = Label(text="")
km_entry.grid(row=2, column=1)


def calculate():
    mile = mile_entry.get()
    if mile.isnumeric():
        km = (float(mile) * 1.609)
        km_entry["text"] = format(km, ".2f")
    else:
        tkinter.messagebox.showerror(title="Value Error", message="Please enter a number.")


button = Button(text="Calculate", command=calculate)
button.grid(row=3, column=1)
window.mainloop()
