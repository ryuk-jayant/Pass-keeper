# Importing required modules and files
from tkinter import *
from PIL import ImageTk, Image
import re
import pathlib
import os
import tkinter.ttk
import Modify_2

# Setting font styles to be used later upon call
BUTTON_FONT = ("Sans-Serif", 13, "bold")
LARGE_FONT = ("Verdana", 13)


# Toplevel or Root Window
class ModifyWindow(Toplevel):
    
    # Constructor
    def __init__(self, *args):
        Toplevel.__init__(self, *args, bg="black", pady=5,
                          highlightthicknes=2, highlightcolor="white")

        self.title("Modify")

        # Adding image as Window Heading
        img = Image.open("images/Modify1.png")
        img = img.resize((130, 55), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(img)
        l = Label(self, image=logo, bd=0)
        l.img = logo
        l.pack(pady=10)

        self.frame = Frame(self, pady=2, bd=3, bg="black")
        self.frame.pack()        

        # Show search button only when some data is stored
        if pathlib.Path(".data").exists():
            
            # Variable Tracing using Tk 's variable tracing
            self.namevar = StringVar()
            self.namevar.trace("w", self.onUpdate)
            search = tkinter.ttk.Entry(self.frame, textvariable=self.namevar,
                                       width=40)
            search.grid(row=0, column=1, columnspan=2, pady=3)
            search.focus_set()
            
            # Binding a <Return> pressed event
            search.bind("<Return>", lambda _:  self.onUpdate())

            # Setting Button Style
            s = tkinter.ttk.Style()
            s.configure("Submit.TButton", font=BUTTON_FONT)

            # Adding Search Button
            searchBtn = tkinter.ttk.Button(self.frame, text="Search",
                                   style="Submit.TButton",
                                   command=lambda:  self.onUpdate())
            searchBtn.grid(row=0, column=3, sticky="e", pady=5)

        # Hides search button when no data is present
        else:
            Search_Hide = Label(self.frame, bg="black", state=DISABLED)
            Search_Hide.grid(row=0, columnspan=3)

        # Awesomeness happens here
        # Using another file (Modify_2) in window 
        self.tree = Modify_2.getTreeFrame(self, bd=3)
        self.tree.pack()

    """*args = [name, index, mode]
        Returned by the variable tracing"""
    
    # Search as you Type (just like Google and others)
    def onUpdate(self, *args):

        # Search regex
        content = self.namevar.get()
        searchReg = re.compile(content, re.IGNORECASE)
        self.tree.updateList(searchReg)
        return True


# For Debugging Purposes
if __name__ == "__main__":
    root = Tk()
    Tk.iconbitmap(root, default="ICO/icon.ico")
    Tk.wm_title(root, "Test")
    Label(root, text="Root window").pack()
    new = ModifyWindow(root)
    root.mainloop()
