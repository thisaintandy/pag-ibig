from tkinter import *   #import everything in tkinter library

'''
root = Tk()#   create a window
root.geometry("1680x945+120+20")   #window size
root.title("Pag-Ibig Form")

root.mainloop()   #close program
'''


# Call when putting a navigation buttons
def NavigationButton(page):
    button_details = Button(page, text="MY DETAILS", font=("Arial", 12, 'bold'), fg="#383838",  bg="#EDEEEE", bd=0, activebackground="#EDEEEE", activeforeground="#FFFF00" )
    button_details.place(x=110, y=25)

    button_payment = Button(page, text="PAYMENT", font=("Arial", 12, 'bold'), fg="#383838",  bg="#EDEEEE", bd=0, activebackground="#EDEEEE", activeforeground="#FFFF00" )
    button_payment.place(x=250, y=25)

    button_about = Button(page, text="ABOUT US", font=("Arial", 12, 'bold'), fg="#383838",  bg="#EDEEEE", bd=0, activebackground="#EDEEEE", activeforeground="#FFFF00" )
    button_about.place(x=375, y=25)

##### LOGIN PAGE ######
def LoginPage():
    # ----- create a window
    global Login_Page
    Login_Page = Tk()
    Login_Page.geometry("1200x675+365+130")
    Login_Page.resizable(width=False, height=False)
    Login_Page.title("Pag-IBIG Fund")

    # ----- put background picture
    file_bg_login = PhotoImage(file="loginpage.png", master=Login_Page)
    bg_login = Label(Login_Page, image=file_bg_login, borderwidth=0)
    bg_login.place(x=0, y=0)

    # ----- put textbox for username
    username_textbox = Text(Login_Page, height=1, width=21)
    username_textbox.configure(font=("Arial", 20))
    username_textbox.place(x=70, y=280)

    # ----- put textbox for password
    password_textbox = Text(Login_Page, height=1, width=21)
    password_textbox.configure(font=("Arial", 20))
    password_textbox.place(x=70, y=370)
    
    # ----- put enter button
    file_enterbutton = PhotoImage(file="enterbutton.png", master=Login_Page)
    button_enter = Button(Login_Page, image=file_enterbutton, activebackground="black", height=41, width=120, borderwidth=0, bd=0, relief=FLAT, command=HomePage1)                      
    button_enter.place(x=165, y=417)

    # ----- put create account button
    file_createaccountbutton = PhotoImage(file="createaccountbutton.png", master=Login_Page)
    button_createaccount = Button(Login_Page, image=file_createaccountbutton, activebackground="black", height=47, width=278, borderwidth=0, bd=0, relief=FLAT)                      
    button_createaccount.place(x=90, y=580)

    Login_Page.mainloop()
    


##### REGISTRATION PAGE ######
def RegistrationPage1():
    # ----- create a window
    global RegistrationPage1
    Reg_Page1 = Tk()
    Reg_Page1.geometry("1200x675+365+130")
    Reg_Page1.resizable(width=False, height=False)
    Reg_Page1.title("Pag-IBIG Fund")

    # ----- put background picture
    file_bg_reg1 = PhotoImage(file="regpage1.png", master=Reg_Page1)
    bg_reg1 = Label(Reg_Page1, image=file_bg_reg1, borderwidth=0)
    bg_reg1.place(x=0, y=0)

    # ----- put textbox for name
    name_textbox = Text(Reg_Page1, height=1, width=28)
    name_textbox.configure(font=("Arial", 18))
    name_textbox.place(x=110, y=390)

    # ----- put textbox for birthday
    bday_textbox = Text(Reg_Page1, height=1, width=26, wrap=WORD)
    bday_textbox.configure(font=("Arial", 18))
    bday_textbox.place(x=535, y=390)

    # ----- put textbox for birthplace
    bplace_textbox = Text(Reg_Page1, height=1, width=26, wrap=WORD)
    bplace_textbox.configure(font=("Arial", 18))
    bplace_textbox.place(x=930, y=390)

    # ----- put textbox for sex
    sex_textbox = Text(Reg_Page1, height=1, width=11, wrap=WORD)
    sex_textbox.configure(font=("Arial", 18))
    sex_textbox.place(x=1353, y=390)

    # ----- put textbox for address
    address_textbox = Text(Reg_Page1, height=1, width=107, wrap=WORD)
    address_textbox.configure(font=("Arial", 18))
    address_textbox.place(x=110, y=555)

    NavigationButton(Reg_Page1)

    Reg_Page1.mainloop()


##### HOME PAGE #####
def HomePage1():

    try: 
        Login_Page.destroy()

    finally:

        # ----- create a window
        global Home_Page1
        Home_Page1 = Tk()
        Home_Page1.geometry("1200x675+365+130")
        Home_Page1.resizable(width=False, height=False)
        Home_Page1.title("Pag-IBIG Fund")

        # ----- put background picture
        file_bg_home1 = PhotoImage(file="bghome1.png", master=Home_Page1)
        bg_home1 = Label(Home_Page1, image=file_bg_home1, borderwidth=0)
        bg_home1.place(x=0, y=0)

        # ----- show arrow to page 2
        file_arrow_button_right = PhotoImage(file="arrowright.png", master=Home_Page1)
        button_arrow_right = Button(Home_Page1, bg="#040505", image=file_arrow_button_right, borderwidth=0, bd=0, width=28, activebackground="#040505", relief=FLAT, command=BG2)                      
        button_arrow_right.place(x=1105, y=280)

        # ----- show arrow to page 3
        file_arrow_button_left = PhotoImage(file="arrowleft.png", master=Home_Page1)
        button_arrow_left = Button(Home_Page1, bg="#030505", image=file_arrow_button_left, borderwidth=0, bd=0, width=28, activebackground="#030505", relief=FLAT, command=BG3)                      
        button_arrow_left.place(x=70, y=280)

        # ----- show logout button
        file_logout_button = PhotoImage(file="logoutbutton.png", master=Home_Page1)
        button_logout = Button(Home_Page1, image=file_logout_button, activebackground="black", height=55, width=135, borderwidth=0, bd=0, relief=FLAT)                      
        button_logout.place(x=1020, y=5)
        

        NavigationButton(Home_Page1)

        Home_Page1.mainloop()

    

# ---------- SHOW BACKGROUND 1
def BG1():

    # ----- put background picture
    file_bg_home1 = PhotoImage(file="bghome1.png", master=Home_Page1)
    bg_home1 = Label(Home_Page1, image=file_bg_home1, borderwidth=0)
    bg_home1.place(x=0, y=0)

    # ----- show arrow to page 2
    file_arrow_button_right = PhotoImage(file="arrowright.png", master=Home_Page1)
    button_arrow_right = Button(Home_Page1, bg="#040505", image=file_arrow_button_right, borderwidth=0, bd=0, width=38, activebackground="#040505", relief=FLAT, command=BG2)                      
    button_arrow_right.place(x=1100, y=280)

    # ----- show arrow to page 3
    file_arrow_button_left = PhotoImage(file="arrowleft.png", master=Home_Page1)
    button_arrow_left = Button(Home_Page1, bg="#030505", image=file_arrow_button_left, borderwidth=0, bd=0, width=38, activebackground="#030505", relief=FLAT, command=BG3)                      
    button_arrow_left.place(x=65, y=280)

    NavigationButton(Home_Page1)

    # ----- show logout button
    file_logout_button = PhotoImage(file="logoutbutton.png", master=Home_Page1)
    button_logout = Button(Home_Page1, image=file_logout_button, activebackground="black", height=55, width=135, borderwidth=0, bd=0, relief=FLAT)                      
    button_logout.place(x=1020, y=5)


    Home_Page1.mainloop()



# ---------- SHOW BACKGROUND 2
def BG2():
    
    # ----- set a new background
    file_bg_home1 = PhotoImage(file="bghome2.png", master=Home_Page1)
    bg_home1 = Label(Home_Page1, image=file_bg_home1, borderwidth=0)
    bg_home1.place(x=0, y=0)

    # ----- show arrow to page 3
    file_arrow_button_right = PhotoImage(file="arrowright.png", master=Home_Page1)
    button_arrow_right = Button(Home_Page1, bg="#040505", image=file_arrow_button_right, borderwidth=0, bd=0, width=38, activebackground="#040505", relief=FLAT, command=BG3)                      
    button_arrow_right.place(x=1100, y=280)

    # ----- show arrow to page 1
    file_arrow_button_left = PhotoImage(file="arrowleft.png", master=Home_Page1)
    button_arrow_left = Button(Home_Page1, bg="#030505", image=file_arrow_button_left, borderwidth=0, bd=0, width=38, activebackground="#030505", relief=FLAT, command=BG1)                      
    button_arrow_left.place(x=65, y=280)

    # ----- show logout button
    file_logout_button = PhotoImage(file="logoutbutton.png", master=Home_Page1)
    button_logout = Button(Home_Page1, image=file_logout_button, activebackground="black", height=55, width=135, borderwidth=0, bd=0, relief=FLAT)                      
    button_logout.place(x=1020, y=5)


    NavigationButton(Home_Page1)

    Home_Page1.mainloop()

# ---------- SHOW BACKGROUND 3
def BG3():
    
    # ----- set a new background
    file_bg_home1 = PhotoImage(file="bghome3.png", master=Home_Page1)
    bg_home1 = Label(Home_Page1, image=file_bg_home1, borderwidth=0)
    bg_home1.place(x=0, y=0)

    # ----- show arrow to page 1
    file_arrow_button_right = PhotoImage(file="arrowright.png", master=Home_Page1)
    button_arrow_right = Button(Home_Page1, bg="#040505", image=file_arrow_button_right, borderwidth=0, bd=0, width=38, activebackground="#040505", relief=FLAT, command=BG1)                      
    button_arrow_right.place(x=1100, y=280)

    # ----- show arrow to page 2
    file_arrow_button_left = PhotoImage(file="arrowleft.png", master=Home_Page1)
    button_arrow_left = Button(Home_Page1, bg="#030505", image=file_arrow_button_left, borderwidth=0, bd=0, width=38, activebackground="#030505", relief=FLAT, command=BG2)                      
    button_arrow_left.place(x=65, y=280)

    # ----- show logout button
    file_logout_button = PhotoImage(file="logoutbutton.png", master=Home_Page1)
    button_logout = Button(Home_Page1, image=file_logout_button, activebackground="black", height=55, width=135, borderwidth=0, bd=0, relief=FLAT)                      
    button_logout.place(x=1020, y=5)


    NavigationButton(Home_Page1)

    Home_Page1.mainloop()

LoginPage()
#RegistrationPage1()
#HomePage1()