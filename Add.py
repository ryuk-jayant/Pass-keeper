# Importing required modules and files
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.ttk
import json
import encode
from firebase import add_to_database
# Setting font styles to be used later upon call
LABEL_FONT = ("Monospace", 12)
BUTTON_FONT = ("Sans-Serif", 15, "bold")
INFO_FONT = ("Helvetica", 14, "bold")


# Toplevel or Root Window
class AddWindow(Toplevel):
    
    # Constructor
    def __init__(self, *args):
        Toplevel.__init__(self, *args)

        self.title("Add Credentials")
        self.setFrames()

    # Defines how the GUI of program will look like
    def setFrames(self, **kwargs):
        add = Frame(self, padx=10, pady=10, bd=3, bg="black",
                    highlightthicknes=2)
        add.pack()

        # Adding image as Window Heading
        img = Image.open("images/Add1.png")
        img = img.resize((90, 50), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(img)
        l = Label(add, image=logo, bd=0)
        l.img = logo
        l.grid(row=0, columnspan=3, pady=10)

        # Row for Service Name entry
        SLabel = Label(add, text="Service*", width=10, bd=3,
                    font=LABEL_FONT, pady=5, bg="black", fg="white")
        SLabel.grid(row=1, column=0, pady=3, sticky="ns")
        service = tkinter.ttk.Entry(add, width=20, font=LABEL_FONT)
        service.grid(row=1, column=1, pady=3)

        # Row for Username entry
        ULabel = Label(add, text="Username", width=10, bd=3,
                     font=LABEL_FONT, pady=5, bg="black", fg="white")
        ULabel.grid(row=2, column=0, pady=3, sticky="ns")
        username = tkinter.ttk.Entry(add, width=20, font=LABEL_FONT)
        username.grid(row=2, column=1, pady=3)

        # Row for Password entry
        PLabel = Label(add, text="Password*", width=10, bd=3,
                     font=LABEL_FONT, pady=5, bg="black", fg="white")
        PLabel.grid(row=3, column=0, pady=3, sticky="ns")
        password = tkinter.ttk.Entry(add, show="*", width=20,
                                     font=LABEL_FONT)
        password.grid(row=3, column=1, pady=3)

        # Adding special bind tag for binding events
        tag = "Submit"
        for entry in (username, password, service):
            entry.bindtags((tag,) + entry.bindtags())
     
        # Label for adding space 
        info = Label(add, width=30, bd=3, pady=7, bg="black",
                     font=INFO_FONT)
        info.grid(row=4, columnspan=2, pady=3)

        # Setting Button Style
        s = tkinter.ttk.Style()
        s.configure("Submit.TButton", font=BUTTON_FONT, sticky="s")

        # Adding Submit Button
        addBtn = tkinter.ttk.Button(add, text="Add to Manager",
                                    style="Submit.TButton",
                                    command=lambda: self.addClicked(
                                        info=info, username=username,
                                        password=password, service=service))
        addBtn.grid(row=5, columnspan=2, pady=3)

    # Function for what to do when Submit button is clicked
    def addClicked(self, **kwargs):   
        fileName = ".data"
        
        # Writing encoded data to file
        if(kwargs["password"].get() != "" and kwargs["service"].get() != ""):
            data = None
            details = [kwargs["username"].get(),
                       encode.encode(kwargs["password"].get())]

            data_to_firebase=dict({
                "password":encode.encode(kwargs["password"].get())
            })
            # Reading initally present data
            try:
                with open(fileName, "r") as outfile:
                    data = outfile.read()
            except IOError:
                # Create a file if it doesn't exits
                open(fileName, "a").close()

            # Load newly entered data
            if data:
                data = json.loads(data)
                if kwargs["service"].get() in data.keys():
                    k = kwargs["service"].get()
                    i = 2
                    while (k+" - "+str(i)) in data.keys():
                        i+=1 
                    k = k+" - "+str(i)
                    data[k] = details
                else:
                    data[kwargs["service"].get()] = details
            else:
                data = {}
                data[kwargs["service"].get()] = details

            print(data_to_firebase)
            add_to_database(data_to_firebase, kwargs["service"].get(),kwargs["username"].get())

            # Writing and Saving data to file
            with open(".data", "w") as outfile:
                outfile.write(json.dumps(data, sort_keys=True, indent=4))

            # Delete given entries from window after successful adding 
            for widg in ("username", "service", "password"):
                kwargs[widg].delete(0, "end")

            # Show Confirmation
            kwargs["info"].config(text="Added ✔", fg="green")
            
        # Raise an error for not filling necessary fields
        else:
            messagebox.showerror("Error",
                                 "Service or Password can't be empty !!!", parent=self)


# Used for Debugging
if __name__ == "__main__":
    root = Tk()
    Tk.iconbitmap(root, default="ICO/icon.ico")
    Tk.wm_title(root, "Test")
    Label(root, text="Root window").pack()
    new = AddWindow()
    root.mainloop()
