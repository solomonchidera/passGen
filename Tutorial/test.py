import tkinter as tk # all logic we need
from tkinter import ttk # has all the widgets we need
import tkinter.font as tkFont

# window ie screen
window = tk.Tk()
# Create a font Object
fonnt = tkFont.Font(family="Aladin", size=16, weigth="bold", slant="italic")
window.title('Demo App')
window.geometry('800x400') # geometry.(widthxheight)
#label = tk.Label(master = window, text="Hello Moniaar", font=("Aladin", 16, "bold"))
label = tk.Label(window, text="Hell World", font=fonnt)
label.pack()

# Run not run but run ie start the app
window.mainloop()
