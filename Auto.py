# Importing required modules and files
from selenium import webdriver as D
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import time
import json
import encode

#-------------------------CHROME OPTIONS FOR DESIRED METHOD OF OPENING WINDOW---------------------------------#
options = D.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--start-maximized --incognito")
options.add_argument("no-sandbox")
options.add_argument("disable-default-apps")
#-------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---------------------------------#

# Setting font styles to be used later upon call
LARGE_FONT = ("Courier", 20, "bold")
NORM_FONT = ("Verdana", 9, "italic")


# Toplevel or Root Window
class AutoWin(Toplevel):

    # Constructor
    def __init__(self, *args):
        Toplevel.__init__(self, *args)

        self.title("Auto Login")
        self.setFrames()
        
    # Defines how the GUI of program will look like
    def setFrames(self, **kwargs):
        Auto = Frame(self, padx=10, bd=3, bg="black",
                    highlightthicknes=2)
        Auto.pack()

        # Disclaimer Part - 1
        d1 = Label(Auto, text="Click on any service and\n Sit Back !!!",
                   bd=2, font=LARGE_FONT, bg="orange", fg="black")
        d1.grid(row=0, columnspan=3, pady=20)

        # Adding Instagram Button
        img = Image.open("images/instagram.png")
        img = img.resize((110, 110), Image.LANCZOS)
        logo = ImageTk.PhotoImage(img)
        insta = Button(Auto, image=logo, compound="top",bg="black",
                    fg="white", bd=0, command=lambda: self.instagram())
        insta.img = logo
        insta.grid(row=1, column=0, padx=10, pady=10)

        # Adding Twitter Button
        img = Image.open("images/twitter.png")
        img = img.resize((110, 110), Image.LANCZOS)
        logo = ImageTk.PhotoImage(img)
        twtr = Button(Auto, image=logo, compound="top",bg="black",
                    fg="white", bd=0, command=lambda: self.twitter())
        twtr.img = logo
        twtr.grid(row=1, column=1, padx=10, pady=10)

        # Adding Amazon Button
        img = Image.open("images/amazon.png")
        img = img.resize((110, 110), Image.LANCZOS)
        logo = ImageTk.PhotoImage(img)
        amz = Button(Auto, image=logo, compound="top",bg="black",
                    fg="white", bd=0, command=lambda: self.amazon())
        amz.img = logo
        amz.grid(row=1, column=2, padx=10, pady=10)

        # Adding Netflix Button
        img = Image.open("images/netflix.png")
        img = img.resize((110, 110), Image.LANCZOS)
        logo = ImageTk.PhotoImage(img)
        nf = Button(Auto, image=logo, compound="top",bg="black",
                    fg="white", bd=0, command=lambda: self.netflix())
        nf.img = logo
        nf.grid(row=2, column=0, padx=10, pady=10)

        # Adding Amazon Prime Video Button
        img = Image.open("images/prime.png")
        img = img.resize((110, 110), Image.LANCZOS)
        logo = ImageTk.PhotoImage(img)
        apv = Button(Auto, image=logo, compound="top",bg="black",
                    fg="white", bd=0, command=lambda: self.prime_video())
        apv.img = logo
        apv.grid(row=2, column=1, padx=10, pady=10)

        # Adding Steam Button
        img = Image.open("images/steam.png")
        img = img.resize((110, 110), Image.LANCZOS)
        logo = ImageTk.PhotoImage(img)
        steam = Button(Auto, image=logo, compound="top",bg="black",
                    fg="white", bd=0, command=lambda: self.steam())
        steam.img = logo
        steam.grid(row=2, column=2, padx=10, pady=10)

        # Adding Label Space
        bl = Label(Auto, bg="black")
        bl.grid(row=3, columnspan=3)

        # Disclaimer Part - 2
        d2 = Label(Auto, text="....more sites coming soon !!!",
                   font=NORM_FONT, bg="black", fg="white")
        d2.grid(row=4, columnspan=3, sticky="se")


    # Automation for Instagram
    def instagram(self, *args):

        # Open database file to search for saved details
        with open(".data", "r") as outfile:
            data = outfile.read()
        data = json.loads(data)
        # 'e' acts as condition satisfier for showing error messages
        e = 0
        
        # Searches for details of Instagram
        for i in data.keys():
            if "instagram" == i.lower():
                e = 1
                uid = data[i][0]
                pwd = encode.decode(data[i][1])
                # Launching automation assistant and going to desired webpage
                d = D.Chrome("chromedriver.exe", options=options)          
                d.get("https://www.instagram.com/")
                time.sleep(2)
                # Finding and Filling Username element
                username_input = d.find_element(By.NAME, "username")
                username_input.send_keys(uid)
                # Finding and Filling Password element
                password_input = d.find_element(By.NAME, "password")
                password_input.send_keys(pwd)
                # Pressing Enter Key to Login
                password_input.send_keys(Keys.RETURN)
                time.sleep(10)

        # Raise an error if no details for Instagram is found        
        if e == 0:
            messagebox.showerror("Error", "No data for Instagram found !!!", parent=self)
        

    # Automation for Twitter
    def twitter(self, *args):

        # Open database file to search for saved details
        with open(".data", "r") as outfile:
            data = outfile.read()
        data = json.loads(data)
        # 'e' acts as condition satisfier for showing error messages
        e = 0
        
        # Searches for details of Twitter
        for i in data.keys():
            if "twitter" == i.lower():
                e = 1
                uid = data[i][0]
                pwd = encode.decode(data[i][1])
                # Launching automation assistant and going to desired webpage
                d = D.Chrome("chromedriver.exe", options=options)          
                d.get("https://twitter.com/login")
                time.sleep(2)
                # Finding and Filling Username element
                username_input = d.find_element(By.NAME, "session[username_or_email]")
                username_input.send_keys(uid)
                # Finding and Filling Password element
                password_input = d.find_element(By.NAME, "session[password]")
                password_input.send_keys(pwd)
                # Pressing Enter Key to Login
                password_input.send_keys(Keys.RETURN)
                time.sleep(10)

        # Raise an error if no details for Twitter is found        
        if e == 0:
            messagebox.showerror("Error", "No data for Twitter found !!!", parent=self)
        

    # Automation for Amazon 
    def amazon(self, *args):

        # Open database file to search for saved details
        with open(".data", "r") as outfile:
            data = outfile.read()
        data = json.loads(data)
        # 'e' acts as condition satisfier for showing error messages
        e = 0
        
        # Searches for details of Amazon
        for i in data.keys():
            if "amazon" == i.lower():
                e = 1
                uid = data[i][0]
                pwd = encode.decode(data[i][1])
                d = D.Chrome("chromedriver.exe", options=options)
                d.get("https://www.amazon.in")
                sign_in_button = d.find_element(By.CSS_SELECTOR, "#nav-link-accountList")
                sign_in_button.click()
                username_input = d.find_element(By.ID, "ap_email")
                username_input.send_keys(uid)
                username_input.send_keys(Keys.RETURN)
                time.sleep(2)
                password_input = d.find_element(By.ID, "ap_password")
                password_input.send_keys(pwd)
                password_input.send_keys(Keys.RETURN)
                time.sleep(10)
                
        # Raise an error if no details for Amazon is found        
        if e == 0:
            messagebox.showerror("Error", "No data for Amazon found !!!", parent=self)
        

    # Automation for Netflix
    def netflix(self, *args):

        # Open database file to search for saved details
        with open(".data", "r") as outfile:
            data = outfile.read()
        data = json.loads(data)
        # 'e' acts as condition satisfier for showing error messages
        e = 0

        # Searches for details of Netflix
        for i in data.keys():
            if "netflix" == i.lower():
                e = 1
                uid = data[i][0]
                pwd = encode.decode(data[i][1])
                # Launching automation assistant and going to desired webpage
                d = D.Chrome("chromedriver.exe", options=options)
                d.get("https://www.netflix.com/in/login")
                time.sleep(2)
                # Finding and Filling Username element
                username_input = d.find_element(By.ID, "id_userLoginId")
                username_input.send_keys(uid)
                # Finding and Filling Password element
                password_input = d.find_element(By.ID, "id_password")
                password_input.send_keys(pwd)
                # Pressing Enter Key to Login
                password_input.send_keys(Keys.RETURN)
                time.sleep(10)

        # Raise an error if no details for Netflix is found        
        if e == 0:
            messagebox.showerror("Error", "No data for Netflix found !!!", parent=self)
        

    # Automation for Amazon Prime Video
    def prime_video(self, *args):

        # Open database file to search for saved details
        with open(".data", "r") as outfile:
            data = outfile.read()
        data = json.loads(data)
        # 'e' acts as condition satisfier for showing error messages
        e = 0

        # Searches for details of Amazon Prime Video
        for i in data.keys():
            if "prime video" == i.lower():
                e = 1
                uid = data[i][0]
                pwd = encode.decode(data[i][1])
                # Launching automation assistant and going to desired webpage
                d = D.Chrome("chromedriver.exe", options=options)        
                d.get("https://www.primevideo.com")
                time.sleep(2)
                sign_in_button = d.find_element(By.XPATH, "//span[contains(text(), 'Sign in')]") 
                sign_in_button.click()
                username_input = d.find_element(By.ID, "ap_email")
                username_input.send_keys(uid)
                password_input = d.find_element(By.ID, "ap_password")
                password_input.send_keys(pwd)
                password_input.send_keys(Keys.RETURN)
                time.sleep(10)

        # Raise an error if no details for Amazon Prime Video is found        
        if e == 0:
            messagebox.showerror("Error", "No data for Amazon Prime Video found !!!", parent=self)

    
    # Automation for Steam
    def steam(self, *args):

        # Open database file to search for saved details
        with open(".data", "r") as outfile:
            data = outfile.read()
        data = json.loads(data)
        # 'e' acts as condition satisfier for showing error messages
        e = 0

        # Searches for Steam details
        for i in data.keys():
            if "steam" == i.lower():
                e = 1
                uid = data[i][0]
                pwd = encode.decode(data[i][1])
                # Launching automation assistant and going to desired webpage
                d = D.Chrome("chromedriver.exe", options=options)          
                d.get("https://store.steampowered.com/login/")
                time.sleep(2)
                username_input = d.find_element(By.ID, "input_username")
                username_input.send_keys(uid)
                password_input = d.find_element(By.ID, "input_password")
                password_input.send_keys(pwd)
                password_input.send_keys(Keys.RETURN)
                time.sleep(10)

        # Raise an error if no details for Steam is found        
        if e == 0:
            messagebox.showerror("Error", "No data for Steam found !!!", parent=self)


# For Debugging Purposes
if __name__ == "__main__":
    root = Tk()
    Tk.iconbitmap(root, default="ICO/icon.ico")
    Tk.wm_title(root, "Test")
    Label(root, text="Root window").pack()
    new = AutoWin()
    root.mainloop()