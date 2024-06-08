import tkinter as tk # all logic we need
from tkinter import ttk # has all the widgets we need

# window ie screen
window = tk.Tk()
window.title('Demo App')
window.geometry('800x400') # geometry.(widthxheight)
label = tk.Label(master = window, text="Hello Moniaar", font=("Aladin", 16, "bold"))
label.pack()

# Run not run but run ie start the app
window.mainloop()
