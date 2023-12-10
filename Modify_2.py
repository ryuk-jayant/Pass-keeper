# Importing required modules and files
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
import os
import re
import tkinter.ttk
import hashlib
import encode
import json
from firebase import update_selected_pass,delete_database,delete_selected_pass

# Setting font styles to be used later upon call
NORM_FONT = ("Verdana", 12,"bold", "italic")
LARGE_FONT = ("Verdana", 13)
BUTTON_FONT = ("Sans-Serif", 13, "bold")


# Toplevel or Root Window
class ListWindow(Toplevel):

    # Constructor
    def __init__(self, *args):
        Toplevel.__init__(self, *args)
        self.title("List Database")

        self.frame = getTreeFrame(self, bd=3)
        self.frame.pack()


# Defines how the GUI of program will look like
class getTreeFrame(Frame):

    # Constructor
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs, bg="black", padx=20)

        # Setting Button Style
        s = tkinter.ttk.Style()
        s.configure("Submit.TButton", font=BUTTON_FONT)

        # Adding Update Button
        UpdateBtn = tkinter.ttk.Button(self, text="Update",
                               style="Submit.TButton",
                               command=lambda:  self.Update())
        UpdateBtn.grid(row=0, column=0, pady=15)

        # Adding Delete Button
        DelBtn = tkinter.ttk.Button(self, text="Delete",
                               style="Submit.TButton",
                               command=lambda:  self.Delete())
        DelBtn.grid(row=0, column=1, pady=15)

        # Adding "Delete All" Button
        DelAllBtn = tkinter.ttk.Button(self, text="Delete All",
                               style="Submit.TButton",
                               command=lambda:  self.DeleteAll())
        DelAllBtn.grid(row=0, column=2, pady=15)

        # Adding List containing credentials
        self.addLists()

    # Function to add list containing credentials
    def addLists(self, *arg):
        dataList = self.getData()
        headings = ["Service", "Username"]

        if dataList:
            # Adding the Treeview (List and Scrollbar)
            scroll = tkinter.ttk.Scrollbar(self, orient=VERTICAL,
                                           takefocus=True)
            self.tree = tkinter.ttk.Treeview(self, columns=headings,
                                             show="headings")
            scroll.config(command=self.tree.yview)
            self.tree.configure(yscroll=scroll.set)

            scroll.grid(row=1, column=3, sticky="ns")
            self.tree.grid(row=1, column=0, columnspan=3)

            # Adding heading to the columns
            for heading in headings:
                self.tree.heading(
                    heading, text=heading,
                    command=lambda c=heading: self.sortby(self.tree, c, 0))
                self.tree.column(heading, width=200)

            # Adding data in list
            for data in dataList:
                self.tree.insert("", "end", values=data)

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

        # If there is no data in the file
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
        label.grid(row=0, rowspan=2, columnspan=4, sticky="ns", pady=10)
        # Adding Okay Button
        B1 = tkinter.ttk.Button(self, text="Okay",
                                style="Submit.TButton",
                                command=self.master.destroy)
        B1.grid(row=2, column=1, pady=10, sticky="ew")

    # Function for what to do when Update button is clicked
    def Update(self, *args):
        item = self.tree.focus()

        if messagebox.askokcancel("Confirmation", "Proceed to updating password?", parent=self):              
            npwd = simpledialog.askstring("New Password",
                                        "Enter a new password for selected entry.\n",
                                        show="*", parent=self)
            # Set new password for account
            if npwd is not None:
                npwd_enc = encode.encode(npwd)
                service = self.tree.item(item, "values")[0]
                self.data[service][1] = npwd_enc
                username=self.tree.item(item,"values")[1]
                service=str(re.split("\s-", service)[0])
                print(service)
                print(npwd_enc)
                update_selected_pass(service, username, npwd_enc)
                with open(".data", "w") as f:
                    json.dump(self.data, f, indent=4, sort_keys=True)
                self.addLists()
                messagebox.showinfo("Success",
                                    "Password Updated Successfully", parent=self)
  

    # Function for what to do when Delete button is clicked
    def Delete(self, *args):
        item = self.tree.focus()

        if messagebox.askokcancel("Confirmation", "Proceed to deleting entry?", parent=self):                
            service = self.tree.item(item, "values")[0]
            username=self.tree.item(item,"values")[1]
            # Delete Account
            print(username+" is deleted from database...")
            delete_selected_pass(service, username)
            del self.data[service]
            with open(".data", "w") as f:
                json.dump(self.data, f, indent=4, sort_keys=True)
            self.addLists()
            messagebox.showinfo("Success",
                                    "Account Deleted Successfully", parent=self)


    # Function for what to do when "Delete All" button is clicked
    def DeleteAll(self, *args):

        # Asks for authentication before allowing to Delete all accounts
        pwd = simpledialog.askstring("Verify",
                                     "Enter your manager's password to confirm.\n\
                                     \n   Warning : This action can not be undone.\n",
                                     show="*", parent=self)
        if pwd is not None:
            # Authentication Succeeds
            if hashlib.md5(pwd.encode("utf-8")).hexdigest() == encode.password:
                # Delete all accounts
                os.remove(".data")
                for x in self.tree.get_children(""):
                    self.tree.delete(x)
                delete_database()
                messagebox.showinfo("Success",
                                        "Database Deleted Successfully", parent=self)
            # Authentication Fails
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


# Used for Debugging
if __name__ == "__main__":
    root = Tk()
    Tk.iconbitmap(root, default="ICO/icon.ico")
    Tk.wm_title(root, "Test")
    Label(root, text="Root window").pack()
    new = ListWindow(root)
    root.mainloop()
