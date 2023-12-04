# Importing required modules and files
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter.ttk
import os
import Add
import hashlib
import encode
import Use
import Modify

# Setting font styles to be used later upon call
LARGE_FONT = ("Verdana", 18, "bold")
PLABEL_FONT = ("Monospace", 12)
BUTTON_FONT = ("Sans-Serif", 15, "bold")
MADEIN_FONT = ("Helvetica", 15, "bold")


# Toplevel or Root Window
class Login(Tk):
    """docstring for Login"""
    # Constructor
    def __init__(self, *args):
        Tk.__init__(self, *args)
        Tk.iconbitmap(self, default="icon.ico")
        Tk.wm_title(self, "Pass-Keeper")
        self.option_add("*background", "black")
        self.option_add("*foreground", "white")
        self.option_add("*Entry*background", "white")
        self.option_add("*Entry*foreground", "black")
        self.option_add("*Button*background", "light grey")
        self.option_add("*Button*foreground", "black")
        self.option_add("*Label*font", PLABEL_FONT)
        self.state = {
            "text": "Login to access manager", "val": False
        }

        # Check whether registered user or not
        if encode.password:
            self.addLoginFrame()
        else:
            self.addRegisterFrame()

    # Defines how the Login window of the program will look like
    def addLoginFrame(self, *kwargs):
        login = Frame(self, padx=2, pady=2, bd=2, bg="black",
                      highlightthicknes=2, highlightcolor="white")
        login.pack()

        # Adding Info Button
        img = Image.open("info.png")
        img = img.resize((60, 60), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(img)
        logout = Button(login, image=logo, compound="top",
                      bg="black", fg="white", font=BUTTON_FONT,
                      bd=0, command=self.Info)
        logout.img = logo
        logout.place(x=5, y=2)

        # Adding image as Window Heading
        img = Image.open("login1.png")
        img = img.resize((140, 50), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(img)
        l = Label(login, image=logo, bd=0)
        l.img = logo
        l.grid(row=0, columnspan=3, pady=5)

        # Adding image to enhance UI
        img = Image.open("login.png")
        img = img.resize((150, 150), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(img)
        l = Label(login, image=logo, bd=0)
        l.img = logo
        l.grid(row=1, columnspan=3)

        # Dynamic label showing login status
        loginLabel = Label(login, text=self.state["text"],
                           bd=10, font=LARGE_FONT,
                           width=30, pady=17, bg="black", fg="white")
        loginLabel.grid(row=2, columnspan=3)

        # Row for recieving login password
        entrylabel = Label(login, text="Enter your Password", bd=3,
                           font=PLABEL_FONT, pady=5, bg="black", fg="white")
        entrylabel.grid(row=3, column=0, pady=3, sticky="ne")
        entry = tkinter.ttk.Entry(login, show="*", width=20,
                                  font=PLABEL_FONT)
        entry.grid(row=3, column=1, pady=3)
        
        # Binding event when enter is pressed in the Entry
        """ used for lambda compatibility, " _ " marks an unused variable """
        entry.bind("<Return>", lambda _: self.checkPwd(
            login, label=loginLabel, entry=entry, btn=submitBtn))
        entry.focus_set()

        # Setting Button Style
        s = tkinter.ttk.Style()
        s.configure("Submit.TButton", font=BUTTON_FONT)

        # Adding Submit Button
        submitBtn = tkinter.ttk.Button(login, text="Submit",
                                       style="Submit.TButton",
                                       command=lambda: self.checkPwd(
                                           login, label=loginLabel, entry=entry,
                                           btn=submitBtn))
        submitBtn.grid(row=4, columnspan=3, pady=20)

    # Function to check login password and proceed accordingly
    """Kwargs = loginLabel, password entry, and submit button"""
    def checkPwd(self, frame, **kwargs):
        chk = kwargs["entry"].get()
        
        # if passwords match
        if hashlib.md5(chk.encode("utf-8")).hexdigest() == encode.password:
            # Changing login status
            self.state["text"] = "Logged In"
            self.state["val"] = True
            
            # Using .config() to modify the args
            kwargs["label"].config(text=self.state["text"], fg="green")
            kwargs["entry"].config(state=DISABLED)
            kwargs["btn"].config(state=DISABLED)

            # adding buttons
            self.addConfigBtn(frame)

        # If passwords don't match
        else:
            messagebox.showerror("Error", "Incorrect Password\n\
                                 \n       Try Again!!!")
            
            # Removing previosly entered password to retry entry
            kwargs["entry"].delete(0, "end")

    # Function to add buttons once login is successful
    def addConfigBtn(self, login):

        # Adding Info Button
        img = Image.open("info.png")
        img = img.resize((60, 60), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(img)
        logout = Button(login, image=logo, compound="top",
                      bg="black", fg="white", font=BUTTON_FONT,
                      bd=0, command=self.Info)
        logout.img = logo
        logout.place(x=5, y=2)

        # Adding image to enhance UI
        img = Image.open("login2.png")
        img = img.resize((225, 225), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(img)
        l = Label(login, image=logo, bd=0)
        l.img = logo
        l.grid(row=0, rowspan=2, columnspan=3)

        # Adding Logout Button
        img = Image.open("logout.png")
        img = img.resize((45, 45), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(img)
        logout = Button(login, image=logo, text="Logout", compound="top",
                      bg="black", fg="white", font=BUTTON_FONT,
                      bd=0, command=self.LogOut)
        logout.img = logo
        logout.place(x=464, y=0)

        # Blank label to hide password row
        HideLabel = Label(login, text="", bd=10, font=LARGE_FONT,
                           width=30, bg="black", state=DISABLED)
        HideLabel.grid(row=3, columnspan=3)
        
        # Configured Buttons
        # btnList = (addBtn, listBtn, getBtn)

        # Creating temp references to images using temp1, 2, 3
        #      so as to disallow garbage collection problems
        btnList = ["Add", "Use", "Modify"]
        btnCmdList = [lambda: Add.AddWindow(self),
                      lambda: Use.UseWindow(self),
                      lambda: Modify.ModifyWindow(self)]
        f = []  # Frames array
        img = []  # Image array
        self.temp = []  # Temp array

        # Adding all 3 buttons
        for i in range(3):
            f.append(Frame(login, padx=20, bg="black"))
            f[i].grid(row=3, column=i, rowspan=2)
            img.append(PhotoImage(
                file=btnList[i] + ".png"))
            self.temp.append(img[i])
            tkinter.ttk.Button(f[i], image=img[i], text=btnList[i],
                               compound="top", style="Submit.TButton",
                               command=btnCmdList[i]).grid(pady=15)

    # Function to carry out Logout operation
    def LogOut(self, *arg):
        if messagebox.askyesno("Confirmation", "    Really Logout ?"):
            new.destroy()
            Login()

    # Function to show Info
    def Info(self, *args):
        messagebox.showinfo("Made By",
                            "This project is a bonafide creation of\n\
Divyansh Agrawal, Jayant Dubey & Pratyush Nair\n\
", parent=self)

    # Defines how the Registration window of the program will look like
    def addRegisterFrame(self, *arg):
        register = Frame(self, padx=2, pady=2, bd=2, bg="black",
                         highlightthicknes=2, highlightcolor="white")
        register.pack()

        # Adding Info Button
        img = Image.open("info.png")
        img = img.resize((60, 60), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(img)
        logout = Button(register, image=logo, compound="top",
                      bg="black", fg="white", font=BUTTON_FONT,
                      bd=0, command=self.Info)
        logout.img = logo
        logout.place(x=5, y=8)

        # Adding image as Window Heading
        img = Image.open("title.png")
        img = img.resize((350, 70), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(img)
        l = Label(register, image=logo, bd=0)
        l.img = logo
        l.grid(row=0, columnspan=3, pady=5)

        # Adding image to enhance UI
        img = Image.open("register.png")
        img = img.resize((140, 230), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(img)
        l = Label(register, image=logo, bd=0)
        l.img = logo
        l.grid(row=1, columnspan=3, pady=3)

        info = "Register with a password\nTo start using the manager"
        registerLabel = Label(register, text=info,
                              bd=10, font=LARGE_FONT, width=30, pady=12,
                              bg="black", fg="white")
        registerLabel.grid(row=2, columnspan=3)

        # Row for setting password
        entrylabel = Label(register, text="Set your Password", bd=3,
                           font=PLABEL_FONT, pady=5, bg="black", fg="white")
        entrylabel.grid(row=3, column=0, pady=3, sticky="ne")
        entry = tkinter.ttk.Entry(register, show="*", width=20,
                                  font=PLABEL_FONT)
        entry.grid(row=3, column=1, pady=3)
        entry.focus_set()

        # Row for re-entering password to confirm
        entryChklabel = Label(register, text="Confirm your Password",
                              bd=3, font=PLABEL_FONT, pady=5,
                              bg="black", fg="white")
        entryChklabel.grid(row=4, column=0, pady=3, sticky="ne")
        entryChk = tkinter.ttk.Entry(register, show="*", width=20,
                                     font=PLABEL_FONT)
        entryChk.grid(row=4, column=1, pady=3)

        # Binding event when enter is pressed in the Entry
        entryChk.bind("<Return>", lambda _: self.register(register,
                                                          entry, entryChk))

        # Setting Button Style
        s = tkinter.ttk.Style()
        s.configure("Submit.TButton", font=BUTTON_FONT)

        # Adding Register Button
        submitBtn = tkinter.ttk.Button(register, text="Register",
                               style="Submit.TButton",
                               command=lambda: self.register(register, entry,
                                                             entryChk))
        submitBtn.grid(row=5, columnspan=3, pady=15)

        # Adding "Made with love by Indians" Label
        MadeIn = Label(register, text="❤ भारतीयों द्वारा सप्रेम निर्मित ❤",
                       font=MADEIN_FONT, bd=3,
                       pady=5, bg="black", fg="cyan")
        MadeIn.grid(row=6, columnspan=3, pady=5)

    # Function to register the user
    def register(self, frame, *pwd):
        
        # Checking if "Password" and "Confirm Password" match or not
        # pwd is a list containing password inputs
        if pwd[0].get() == pwd[1].get() and pwd[0].get()!="":
            encode.password = hashlib.md5(pwd[0].get().
                                          encode("utf-8")).hexdigest()
            
            # Saving password for future use.
            open(".pwd", "w").write(encode.password)
            os.system("attrib +h .pwd") #To make password file hidden
            messagebox.showinfo("Success", "Registered Successfully !!!",
                                parent=self)

            # Ask if user wants to login or exit after being registered
            if messagebox.askyesno("Confirmation",
                                   "    Do you want to Login now ? "):
                frame.destroy()
                self.addLoginFrame()
            else:
                Login.destroy(self)

        # Show Error when no password is entered while registering
        elif pwd[0].get() == pwd[1].get() and pwd[0].get() == "":
            error = "   No Entry Detected !!!\n\nPlease Set-up a Password"
            messagebox.showerror("Error", error)

        # Show Error if "Password" and "Confirm Password" do not match
        else:
            error = "Passwords don't match !!!\n\n            Try again"
            messagebox.showerror("Error", error)

            # Removing previosly entered Passwords in both fields
            for i in pwd:
                i.delete(0, "end")


# Launches or Runs the complete program
if __name__ == "__main__":
    new = Login()
    new.mainloop()
