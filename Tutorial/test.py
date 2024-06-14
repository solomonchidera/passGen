import tkinter as tk # all logic we need
from tkinter import ttk # has all the widgets we need
import tkinter.font as tkFont

# window ie screen
window = tk.Tk()
# Create a custom font Object
#fonnt = tkFont.Font(family="Helvetica", size=16, weigth="bold", slant="italic")
# Add title to your app
window.title('Password Generator')
# Window size/ Screen size
window.geometry('800x400') # geometry.(widthxheight)
label = tk.Label(master = window, text="Password Generator", font=("calibri", 16, "bold"))
#label = tk.Label(window, text="Hell World", font=fonnt)
label.pack()

# Run not run but run ie start the app
window.mainloop()
