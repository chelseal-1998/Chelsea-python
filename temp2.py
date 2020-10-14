# Imports libraries
from tkinter import *
from tkinter import messagebox as mb

# Creates window
window = Tk()
window.title("Temperature Converter")


# Calculation for Celsius
def calculationc():
    temperature = (float(celsius_box.get()) * 9 / 5) + 32
    return mb.showinfo("title", temperature)


# Calculation for Fahrenheit
def calculationk():
    temperaturek = (float(k_box.get()) - 32) * 5 / 9

    return mb.showinfo("title", temperaturek)

celsius_box = Entry(window)

_buttonCelsius = Button(window, text="Fahrenheit", height=2, width=35, command=calculationc)

k_box = Entry(window)

_buttonK = Button(window, text="Celsius", height=2, width=35, command=calculationk)

label_a = Label(window, text="Celsius:")
label_b = Label(window, text="fahrenheit:")
_buttonClose = Button(window, text="Exit", height=2, width=35, command=window.destroy)

label_a.pack(anchor=NW)
k_box.pack(anchor=N)
_buttonK.pack(anchor=NE)
label_b.pack(anchor=NW)
celsius_box.pack(anchor=N)
_buttonCelsius.pack(anchor=NE)
_buttonClose.pack(anchor=N)
window.mainloop()
