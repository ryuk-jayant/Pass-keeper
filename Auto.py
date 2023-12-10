# Importing required modules and files
from selenium import webdriver as D
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import time
import json
import encode

#-------------------------CHROME OPTIONS FOR DESIRED METHOD OF OPENING WINDOW---------------------------------#
options = D.ChromeOptions()
#options.add_argument("--user-data-dir=C:\\Users\\d_agr\\AppData\\Local\\Google\\Chrome\\User Data\\")
options.add_experimental_option("excludeSwitches", ["enable-automation"]);
options.add_argument("--start-maximized --incognito")
options.add_argument("no-sandbox")
options.add_argument("disable-default-apps");
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

        # Adding Facebook Button
        img = Image.open("images/facebook.png")
        img = img.resize((110, 110), Image.LANCZOS)
        logo = ImageTk.PhotoImage(img)
        fb = Button(Auto, image=logo, compound="top",bg="black",
                    fg="white", bd=0, command=lambda: self.facebook())
        fb.img = logo
        fb.grid(row=1, column=0, padx=10, pady=10)

        # Adding Instagram Button
        img = Image.open("images/instagram.png")
        img = img.resize((110, 110), Image.LANCZOS)
        logo = ImageTk.PhotoImage(img)
        insta = Button(Auto, image=logo, compound="top",bg="black",
                    fg="white", bd=0, command=lambda: self.instagram())
        insta.img = logo
        insta.grid(row=1, column=1, padx=10, pady=10)

        # Adding Twitter Button
        img = Image.open("images/twitter.png")
        img = img.resize((110, 110), Image.LANCZOS)
        logo = ImageTk.PhotoImage(img)
        twtr = Button(Auto, image=logo, compound="top",bg="black",
                    fg="white", bd=0, command=lambda: self.twitter())
        twtr.img = logo
        twtr.grid(row=1, column=2, padx=10, pady=10)

        # Adding Amazon Button
        img = Image.open("images/amazon.png")
        img = img.resize((110, 110), Image.LANCZOS)
        logo = ImageTk.PhotoImage(img)
        amz = Button(Auto, image=logo, compound="top",bg="black",
                    fg="white", bd=0, command=lambda: self.amazon())
        amz.img = logo
        amz.grid(row=2, column=0, padx=10, pady=10)

        # Adding Flipkart Button
        img = Image.open("images/flipkart.png")
        img = img.resize((110, 110), Image.LANCZOS)
        logo = ImageTk.PhotoImage(img)
        flk = Button(Auto, image=logo, compound="top",bg="black",
                    fg="white", bd=0, command=lambda: self.flipkart())
        flk.img = logo
        flk.grid(row=2, column=1, padx=10, pady=10)

        # Adding TATA CliQ Button
        img = Image.open("images/cliq.png")
        img = img.resize((110, 110), Image.LANCZOS)
        logo = ImageTk.PhotoImage(img)
        cliq = Button(Auto, image=logo, compound="top",bg="black",
                    fg="white", bd=0, command=lambda: self.tata_cliq())
        cliq.img = logo
        cliq.grid(row=2, column=2, padx=10, pady=10)

        # Adding Netflix Button
        img = Image.open("images/netflix.png")
        img = img.resize((110, 110), Image.LANCZOS)
        logo = ImageTk.PhotoImage(img)
        nf = Button(Auto, image=logo, compound="top",bg="black",
                    fg="white", bd=0, command=lambda: self.netflix())
        nf.img = logo
        nf.grid(row=3, column=0, padx=10, pady=10)

        # Adding Amazon Prime Video Button
        img = Image.open("images/prime.png")
        img = img.resize((110, 110), Image.LANCZOS)
        logo = ImageTk.PhotoImage(img)
        apv = Button(Auto, image=logo, compound="top",bg="black",
                    fg="white", bd=0, command=lambda: self.prime_video())
        apv.img = logo
        apv.grid(row=3, column=1, padx=10, pady=10)

        # Adding Steam Button
        img = Image.open("images/steam.png")
        img = img.resize((110, 110), Image.LANCZOS)
        logo = ImageTk.PhotoImage(img)
        steam = Button(Auto, image=logo, compound="top",bg="black",
                    fg="white", bd=0, command=lambda: self.steam())
        steam.img = logo
        steam.grid(row=3, column=2, padx=10, pady=10)

        # Adding Label Space
        bl = Label(Auto, bg="black")
        bl.grid(row=4, columnspan=3)

        # Disclaimer Part - 2
        d2 = Label(Auto, text="....more sites coming soon !!!",
                   font=NORM_FONT, bg="black", fg="white")
        d2.grid(row=5, columnspan=3, sticky="se")
        
        
    # Automation for Facebook
    def facebook(self, *args):
        
        # Open database file to search for saved details
        with open(".data", "r") as outfile:
            data = outfile.read()
        data = json.loads(data)
        # 'e' acts as condition satisfier for showing error messages
        e = 0
        
        # Searches for details of Facebook
        for i in data.keys():
            if "facebook" == i.lower():
                e = 1
                uid = data[i][0]
                pwd = encode.decode(data[i][1])
                # Launching automation assistant and going to desired webpage
                d = D.Chrome("chromedriver.exe", options=options)        
                d.get("https://m.facebook.com/")
                # Finding and Filling Username element
                element_1 = d.find_element_by_name("email");
                element_1.send_keys((str(uid)))
                # Finding and Filling Password element
                element_3 = d.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[3]/form/div[4]/div[3]/div/div/div/div[1]/div/input");
                element_3.send_keys((str(pwd)))
                # Finding and Clicking Login Button 
                element_2 = d.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[3]/form/div[5]/div[1]/button");
                element_2.send_keys(Keys.RETURN);
                
        # Raise an error if no details for Facebook is found
        if e == 0:
            messagebox.showerror("Error", "         No data for Facebook found !!!\n\
                \n  Try renaming service name to 'Facebook'\
                \n(If you remember adding it to the database)", parent=self)


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
                d.get("https://www.instagram.com/accounts/login/?hl=en")
                time.sleep(2)
                # Finding and Filling Username element
                element_1 = d.find_element_by_name("username")
                element_1.click()
                element_1.send_keys((str(uid)))
                # Finding and Filling Password element
                element_2 = d.find_element_by_name("password");
                element_2.click()
                element_2.send_keys((str(pwd)))
                # Pressing Enter Key to Login
                element_2.send_keys(Keys.RETURN);

        # Raise an error if no details for Instagram is found        
        if e == 0:
            messagebox.showerror("Error", "         No data for Instagram found !!!\n\
                \n  Try renaming service name to 'Instagram'\
                \n(If you remember adding it to the database)", parent=self)
        

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
                element_1 = d.find_element_by_name("session[username_or_email]")
                element_1.click()
                element_1.send_keys((str(uid)))
                # Finding and Filling Password element
                element_2 = d.find_element_by_name("session[password]");
                element_2.click()
                element_2.send_keys((str(pwd)))
                # Pressing Enter Key to Login
                element_2.send_keys(Keys.RETURN);

        # Raise an error if no details for Twitter is found        
        if e == 0:
            messagebox.showerror("Error", "           No data for Twitter found !!!\n\
                \n    Try renaming service name to 'Twitter'\
                \n(If you remember adding it to the database)", parent=self)
        

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
                # Launching automation assistant and going to desired webpage
                d = D.Chrome("chromedriver.exe", options=options)          
                d.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fext_vrnc%3Dhi%26tag%3Dgooghydrabk-21%26ascsubtag%3D_k_EAIaIQobChMIq6qZ4eSQ7AIV2qiWCh2y4A4sEAAYASAAEgJF-_D_BwE_k_%26ext_vrnc%3Dhi%26gclid%3DEAIaIQobChMIq6qZ4eSQ7AIV2qiWCh2y4A4sEAAYASAAEgJF-_D_BwE%26network%3Dg%26ref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
                time.sleep(2)
                # Finding and Filling Username element
                element_1 = d.find_element_by_name("email")
                element_1.click()
                element_1.send_keys((str(uid)))
                # Pressing Enter Key to go to Password Entry Page
                element_1.send_keys(Keys.RETURN);    
                time.sleep(2)
                # Selecting option of 'Remember Me'
                element_2a = d.find_element_by_name("rememberMe");
                element_2a.click()
                # Finding and Filling Password element
                element_2 = d.find_element_by_name("password");
                element_2.click()
                element_2.send_keys((str(pwd)))
                # Pressing Enter Key to Login
                element_2.send_keys(Keys.RETURN);

        # Raise an error if no details for Amazon is found        
        if e == 0:
            messagebox.showerror("Error", "         No data for Amazon found !!!\n\
                \n  Try renaming service name to 'Amazon'\
                \n(If you remember adding it to the database)", parent=self)
        

    # Automation for Flipkart
    def flipkart(self, *args):

        # Open database file to search for saved details
        with open(".data", "r") as outfile:
            data = outfile.read()
        data = json.loads(data)
        # 'e' acts as condition satisfier for showing error messages
        e = 0
        
        # Searches for details of Flipkart
        for i in data.keys():
            if "flipkart" == i.lower():
                e = 1
                uid = data[i][0]
                pwd = encode.decode(data[i][1])
                # Launching automation assistant and going to desired webpage
                d = D.Chrome("chromedriver.exe", options=options)
                d.get("https://www.flipkart.com/account/login?ret=/")
                time.sleep(2)
                # Finding and Filling Username element
                element_1 = d.find_element_by_xpath("/html/body/div/div/div[3]/div/div[2]/div/form/div[1]/input")
                element_1.click()  
                element_1.send_keys((str(uid)))
                # Finding and Filling Password element
                element_2 = d.find_element_by_xpath("/html/body/div/div/div[3]/div/div[2]/div/form/div[2]/input");
                element_2.click()
                element_2.send_keys((str(pwd)))
                # Pressing Enter Key to Login
                element_2.send_keys(Keys.RETURN);

        # Raise an error if no details for Flipkart is found        
        if e == 0:
            messagebox.showerror("Error", "         No data for Flipkart found !!!\n\
                \n  Try renaming service name to 'Flipkart'\
                \n(If you remember adding it to the database)", parent=self)
        

    # Automation for TATA CliQ
    def tata_cliq(self, *args):

        # Open database file to search for saved details
        with open(".data", "r") as outfile:
            data = outfile.read()
        data = json.loads(data)
        # 'e' acts as condition satisfier for showing error messages
        e = 0

        # Searches for details of TATA CliQ
        for i in data.keys():
            if "tata_cliq" == i.lower():
                e = 1
                uid = data[i][0]
                pwd = encode.decode(data[i][1])
                # Launching automation assistant and going to desired webpage
                d = D.Chrome("chromedriver.exe", options=options)        
                d.get("https://www.tatacliq.com/login")
                time.sleep(4)
                # Handling occasional ad pop-up
                try:
                    element_ask = d.find_element_by_xpath("/html/body/div[5]/div[2]/div[3]/button[1]")
                    element_ask.click()
                except:
                    pass
                # Finding and Filling Username element
                element_1 = d.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div/div[1]/div[2]/div/div[1]/div[1]/div/div/input");
                element_1.send_keys((str(uid)))
                # Finding and Filling Password element
                element_2 = d.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div/div[1]/div[2]/div/div[1]/div[2]/div/input");
                element_2.send_keys((str(pwd)))
                # Pressing Enter Key to Login
                element_2.send_keys(Keys.RETURN);

        # Raise an error if no details for TATA CliQ is found        
        if e == 0:
            messagebox.showerror("Error", "         No data for TATA CliQ found !!!\n\
                \n  Try renaming service name to 'TATA_CliQ'\
                \n(If you remember adding it to the database)", parent=self)
        

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
                d.get("https://www.netflix.com/in/Login")
                time.sleep(2)
                # Finding and Filling Username element
                element_1 = d.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div[1]/div/label/input")
                element_1.send_keys((str(uid)))
                # Finding and Filling Password element
                element_2 = d.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[2]/div/div/label/input");
                element_2.send_keys((str(pwd)))
                # Pressing Enter Key to Login
                element_2.send_keys(Keys.RETURN);

        # Raise an error if no details for Netflix is found        
        if e == 0:
            messagebox.showerror("Error", "           No data for Netflix found !!!\n\
                \n    Try renaming service name to 'Netflix'\
                \n(If you remember adding it to the database)", parent=self)
        

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
            if "prime_video" == i.lower():
                e = 1
                uid = data[i][0]
                pwd = encode.decode(data[i][1])
                # Launching automation assistant and going to desired webpage
                d = D.Chrome("chromedriver.exe", options=options)        
                d.get("https://www.amazon.com/ap/signin?accountStatusPolicy=P1&clientContext=258-2378267-9953321&language=en_US&openid.assoc_handle=amzn_prime_video_desktop_us&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.primevideo.com%2Fauth%2Freturn%2Fref%3Dav_auth_ap%3F_encoding%3DUTF8%26location%3D%252Fref%253Dav_nav_sign_in")
                # Finding and Filling Username element
                element_1 = d.find_element_by_name("email");
                element_1.send_keys((str(uid)))
                # Finding and Filling Password element
                element_3 = d.find_element_by_name("password");
                element_3.send_keys((str(pwd)))
                 # Selecting option of 'Remember Me'
                element_r = d.find_element_by_name("rememberMe")
                element_r.click()
                # Pressing Enter Key to Login
                element_3.send_keys(Keys.RETURN);

        # Raise an error if no details for Amazon Prime Video is found        
        if e == 0:
            messagebox.showerror("Error", "No data for Amazon Prime Video found !!!\n\
                \nTry renaming service name to 'Prime_Video'\
                \n(If you remember adding it to the database)", parent=self)

    
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
                d.get("https://store.steampowered.com/login/?redir=login%2F&redir_ssl=1")
                time.sleep(2)
                # Finding and Filling Username element
                element_1 = d.find_element_by_name("username")
                element_1.send_keys((str(uid)))
                # Finding and Filling Password element
                element_2 = d.find_element_by_name("password");
                element_2.send_keys((str(pwd)))
                # Pressing Enter Key to Login
                element_2.send_keys(Keys.RETURN);

        # Raise an error if no details for Steam is found        
        if e == 0:
            messagebox.showerror("Error", "          No data for Steam found !!!\n\
                \n     Try renaming service name to 'Steam'\
                \n(If you remember adding it to the database)", parent=self)


# For Debugging Purposes
if __name__ == "__main__":
    root = Tk()
    Tk.iconbitmap(root, default="ICO/icon.ico")
    Tk.wm_title(root, "Test")
    Label(root, text="Root window").pack()
    new = AutoWin()
    root.mainloop()
