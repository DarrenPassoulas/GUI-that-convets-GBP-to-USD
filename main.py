import tkinter
from tkinter import *
from forex_python.converter import CurrencyRates

window=Tk()

c = CurrencyRates()


def button_clicked():
	entered_text = entry1.get()
	
	output = c.convert('GBP', 'USD', float(entered_text))
	converted_string=(str(output))
	
	manipulated_text= "your converted money = " + converted_string
	output_text.delete(0.0,END)
	output_text.insert(END, manipulated_text)

Button(window, text="GBP-USD", width=5, command=button_clicked).grid(row=3, column=0, sticky=W)
Button(window, text="Currency", width=5, command="function").grid(row=3, column=2, sticky=W)

entry1 = Entry(window, width=15, bg="light blue")
entry1.grid(row=2, column=0, columnspan=2, sticky=W)
output_text= Text(window, width=20, height=6, wrap=WORD, background="lightblue")
output_text.grid(row=4, column=0, columnspan=2, sticky=W)


window.mainloop()