
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class singly_LL:
    # Inserting a word at beginning
    def insert_at_beg(self,word):
        temp = Node(word)
        temp.next= self.head
        self.head = temp

    # Undo → delete last nodeclass TextEditor:
    def __init__(self):
        self.head = None
       

    # Typing a word → insert at end
    def insert_at_end(self, word):
        new_node = Node(word)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # When we have nothing to undo 
    def undo(self):
        if self.head is None:
            print("Nothing to undo")
            return

        # If only one word exists
        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next

        temp.next = None

    # Display current text
    def display(self):
        temp = self.head
        text = []

        while temp:
            text.append(temp.data)
            temp = temp.next

        print(" ".join(text))

editor = singly_LL()

editor.insert_at_end("I am ")
editor.insert_at_end("Ealisha")
editor.insert_at_end("Narware")
editor.insert_at_beg("Hello")
editor.display()
# Output: Hello I am  Ealisha Narware

editor.undo()
editor.display()
# Output: Hello World

editor.undo()
editor.display()
# Output: Hello

editor.undo()
editor.display()
# Output: (empty)

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