import tkinter as tk 
from tkinter import filedialog , messagebox

#creating main window
win = tk.Tk()
win.title("Ealisha's Text Editor")
win.geometry("800x600")   # use x not *

# creating text area
text = tk.Text(
    win ,
    wrap = tk.WORD ,
    font = ("Calibri (Body)", 11)

)

text.pack(expand=True , fill= tk.BOTH )
win.mainloop() # keeps the window open and stay  