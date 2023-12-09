# Importing required modules and files
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import simpledialog
import hashlib
import tkinter.ttk
import encode
import json
import pyperclip
import Add
import Auto
import sys

# Setting font styles to be used later upon call
NORM_FONT = ("Verdana", 12,"bold", "italic")
LARGE_FONT = ("Courier", 13)
OUT_FONT = ("Lucida Console", 13)
BUTTON_FONT = ("Sans-Serif", 15, "bold")


# Toplevel or Root Window
class UseWindow(Toplevel):
    
    # Constructor
    def __init__(self, *args):
        Toplevel.__init__(self, *args, pady=5, bg="black",
                          highlightthicknes=2, highlightcolor="white")
        self.title("Use Database")
        
        self.frame = getTreeFrame(self, bd=3)
        self.frame.pack()


# Window for Show Password
class PassWindow(Toplevel):
    
    # Constructor
    def __init__(self, master=None):
        super().__init__(bg="black", pady=10,
                         highlightthicknes=2, highlightcolor="white")
        msg = "The Password is :"
        label = Label(self, text=msg, font=NORM_FONT, width=18,
                      bg="black", fg="red")
        label.grid(row=0, column=0, pady=30, sticky="n")
        l = Label(self, text="", bg="black", width=15)
        l.grid(row=0, column=1, pady=30)
        OutBox = Text(self, font=OUT_FONT,
                      bg="black", fg="white", width=14,
                      height=2, bd=0, state=DISABLED)
        OutBox.place(x=185, y=34)
        # Redirecting console output to OutBox 
        sys.stdout = StdRedirector(OutBox)
        

# Lots of Awesomeness
# Redirecting console output to Show Password window 
class StdRedirector():

    # Constructor
    def __init__(self, text_widget):
        self.text_space = text_widget

    # Redirecting output location
    def write(self, string):
        self.text_space.config(state=NORMAL)
        self.text_space.insert("end", string)
        self.text_space.see("end")
        self.text_space.config(state=DISABLED)
        

# Defines how the GUI of program will look like
class getTreeFrame(Frame):

    # Constructor
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs, bg="black", padx=20)
        self.addLists()

    # Function to add list containing credentials
    def addLists(self, *arg):
        dataList = self.getData()
        headings = ["Service", "Username"]

        if dataList:
            # Adding the Treeview

            # Adding image as Window Heading
            img = Image.open("images/Use1.png")
            img = img.resize((100, 50), Image.LANCZOS)
            logo = ImageTk.PhotoImage(img)
            l = Label(self, image=logo, bd=0)
            l.img = logo
            l.pack(pady=7)

            # Setting Button Style  
            s = tkinter.ttk.Style()
            s.configure("Submit.TButton", font=BUTTON_FONT)
            
            # Adding Labels
            rc = Label(self, text="-> Select and Right Click to show password",
                  bd=2, font=LARGE_FONT, bg="orange", fg="black")
            rc.pack(side="top", fill=X)

            dc = Label(self, text="-> Double Click to copy password",
                  bd=2, font=LARGE_FONT, bg="orange", fg="black")
            dc.pack(side="top", fill=X)

            info = Label(self, text="-> Click table field headings to sort data",
                  bd=2, font=LARGE_FONT, bg="orange", fg="black")
            info.pack(side="top", fill=X)
            
            # Adding Auto-Login Button
            auto = tkinter.ttk.Button(self, text="Auto-Login", 
                               style="Submit.TButton",
                               command=lambda:self.AutoLogin())
            auto.pack(side="top", pady=25)
                   
            # Adding List and Scrollbar
            scroll = tkinter.ttk.Scrollbar(self, orient=VERTICAL,
                                           takefocus=True)
            self.tree = tkinter.ttk.Treeview(self, columns=headings,
                                             show="headings")
            scroll.config(command=self.tree.yview)
            self.tree.configure(yscroll=scroll.set)

            scroll.pack(side=RIGHT, fill=Y)
            self.tree.pack(side=LEFT, fill="both", expand=1)

            # Adding heading to the columns
            for heading in headings:
                self.tree.heading(
                    heading, text=heading,
                    command=lambda c=heading: self.sortby(self.tree, c, 0))
                self.tree.column(heading, width=200)

            # Adding data in list
            for data in dataList:
                self.tree.insert("", "end", values=data)

            # Binding Double click and Right Click to resp. functions
            self.tree.bind("<Double-1>", self.OnDoubleClick)
            self.tree.bind("<Button-3>", self.OnRightClick)

        # Raises error if no data present
        else:
            self.errorMsg()

    # Function to load data into the list
    def getData(self, *arg):
        fileName = ".data"
        self.data = None
        try:
            with open(fileName, "r") as outfile:
                self.data = outfile.read()
        except IOError:
            return ""

        # If there is no data in file
        if not self.data:
            return ""

        self.data = json.loads(self.data)
        dataList = []

        # Handles the case when no username is found
        for service, details in list(self.data.items()):
            usr = details[0] if details[0] else "NO ENTRY"
            dataList.append((service, usr))

        return dataList

    # Function to show error when no data is found
    def errorMsg(self, *args):
        msg = "There is no data yet!!"
        label = Label(self, text=msg, font=NORM_FONT, bd=3,
                      width=30, bg="black", fg="red")
        label.pack(side="top", fill="x", pady=10)
        # Adding Okay Button
        B1 = tkinter.ttk.Button(self, style="Submit.TButton",
                                text="Okay", command=self.master.destroy)
        B1.pack(pady=10, side="left", padx=15)
        # Adding "Add Data" Button
        B2 = tkinter.ttk.Button(self, style="Submit.TButton",
                                text="Add Data",
                                command=lambda:Add.AddWindow(self))
        B2.pack(pady=10)

    # Function to automatically Sign-In in some websites
    def AutoLogin(self, *args):

        # Asks for authentication before allowing automatic Login
        pwd = simpledialog.askstring("Verify",
                                     "           Is it really you trying to Login ?\n\
                                     \nEnter your manager's password to Verify\n",
                                     show="*", parent=self)
        if pwd is not None:
            # Authentication Succeeds
            if hashlib.md5(pwd.encode("utf-8")).hexdigest() == encode.password:
                Auto.AutoWin(self)
            # Authentication Fails
            else:
                messagebox.showerror("Error", "Incorrect Password !!!\n\
                                     \n      Try Again", parent=self)

    # Function to Copy Password... Reacts on Double Mouse Click
    def OnDoubleClick(self, event):

        # Asks for authentication before allowing to Copy password
        pwd = simpledialog.askstring("Verify",
                                     "Is it really you trying to Copy Password ?\n\
                                     \nEnter your manager's password to Verify\n",
                                     show="*", parent=self)
        if pwd is not None:
            # Authentication Succeeds
            if hashlib.md5(pwd.encode("utf-8")).hexdigest() == encode.password:
                item = self.tree.focus()
                service = self.tree.item(item, "values")[0]
                var = self.data[service][1]
                var = encode.decode(var)
                # Copy password to clipboard
                pyperclip.copy(var)
                messagebox.showinfo("Success", "Password Copied to Clipboard"
                                    , parent=self)
            # Authentication Fails
            else:
                messagebox.showerror("Error", "Incorrect Password !!!\n\
                                     \n      Try Again", parent=self)

    # Function to Show Password... Reacts on Right Mouse Click
    def OnRightClick(self, event):

        # Asks for authentication before revealing password
        pwd = simpledialog.askstring("Verify",
                                     "Is it really you trying to Reveal Password ?\n\
                                     \nEnter your manager's password to Verify\n",
                                     show="*", parent=self)
        if pwd is not None:
            # When authentication succeeds
            if hashlib.md5(pwd.encode("utf-8")).hexdigest() == encode.password:
                # Opens PassWindow() and print password into it
                Window = PassWindow()
                Window.title("Show Password")
                Window.geometry("350x100")
                item = self.tree.focus()
                service = self.tree.item(item, "values")[0]
                var = self.data[service][1]
                var = encode.decode(var)
                print(var)
            # When authentication fails
            else:
                messagebox.showerror("Error", "Incorrect Password !!!\n\
                                     \n      Try Again", parent=self)
                
        
    """No *args"""
    # Function to update list with data provided by getData()
    def updateList(self, regStr, *args):
        for x in self.tree.get_children(""):
            self.tree.delete(x)
        for data in self.getData():
            if re.search(regStr, data[0]) or re.search(regStr, data[1]):
                self.tree.insert("", "end", values=data)

    # Function to sort the list when column headings are clicked
    def sortby(self, tree, col, descending):
        """sort tree contents when a column header is clicked on"""
        # Grab values to sort
        data = [(tree.set(child, col), child)
                for child in tree.get_children("")]

        # Sort the data in place
        data.sort(reverse=descending)
        for ix, item in enumerate(data):
            tree.move(item[1], "", ix)
        # Sort in the opposite direction when clicked again
        tree.heading(col,
                     command=lambda col=col: self.sortby(tree, col,
                                                         int(not descending)))


# For  Debugging Purposes
if __name__ == "__main__":
    root = Tk()
    Tk.iconbitmap(root, default="ICO/icon.ico")
    Tk.wm_title(root, "Test")
    Label(root, text="Root window").pack()
    new = UseWindow(root)
    root.mainloop()
