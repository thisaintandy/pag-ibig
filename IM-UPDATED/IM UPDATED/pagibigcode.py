from tkinter import * # import everying in tkinter

# -------------------- LOG IN PAGE -------------------- #
def LoginPage():
    try:
        # check what window currently exist then destroy before opening new window
        if 'About_Page' in globals():
            About_Page.destroy()
        if 'Home_Page' in globals():
            Home_Page.destroy()
        
    finally:
        # create a window
        global Login_Page
        Login_Page = Tk()
        Login_Page.geometry("1200x675+365+130")
        Login_Page.resizable(width=False, height=False)
        Login_Page.title("Pag-IBIG Fund")

        # put background picture
        file_bg_login = PhotoImage(file="loginpage.png", master=Login_Page)
        bg_login = Label(Login_Page, image=file_bg_login, borderwidth=0)
        bg_login.place(x=0, y=0)

        # put textbox for username
        username_textbox = Text(Login_Page, text="username...", height=1, width=21)
        username_textbox.configure(font=("Arial", 20))
        username_textbox.place(x=70, y=280)

        # put textbox for password
        password_textbox = Text(Login_Page, height=1, width=21)
        password_textbox.configure(font=("Arial", 20))
        password_textbox.place(x=70, y=370)
                
        # put enter button
        file_enterbutton = PhotoImage(file="enterbutton.png", master=Login_Page)
        button_enter = Button(Login_Page, image=file_enterbutton, activebackground="black", height=41, width=120, borderwidth=0, bd=0, relief=FLAT)                      
        button_enter.place(x=165, y=417)

        # put create account button
        file_createaccountbutton = PhotoImage(file="createaccountbutton.png", master=Login_Page)
        button_createaccount = Button(Login_Page, image=file_createaccountbutton, activebackground="black", height=47, width=278, borderwidth=0, bd=0, relief=FLAT)                      
        button_createaccount.place(x=90, y=580)

        Login_Page.mainloop()


# -------------------- HOME PAGE -------------------- #
def HomePage():

    try: 
        if 'About_Page' in globals():
            About_Page.destroy()

    finally:

        # ----- create a window
        global Home_Page
        Home_Page = Tk()
        Home_Page.geometry("1200x675+365+130")
        Home_Page.resizable(width=False, height=False)
        Home_Page.title("Pag-IBIG Fund")

        # ----- add background picture
        file_bg_home1 = PhotoImage(file="bghomepage.png", master=Home_Page)
        bg_home1 = Label(Home_Page, image=file_bg_home1, borderwidth=0)
        bg_home1.place(x=0, y=0)

        # ----- add register button
        text_register = Label(Home_Page, text="Want to be a Pag-IBIG member?", font=("Arial", 9), bg="#E4E7E8", foreground="black")
        text_register.place(x=790, y=20)
        button_register = Button(Home_Page, text="Register Here", font=("Arial", 16), bg="yellow", activebackground="blue", 
                                 foreground="#242424", activeforeground="white", height=1, width=13, borderwidth=0, bd=0, relief=FLAT)                      
        button_register.place(x=980, y=9)
        
        # ----- add navigation buttons
        # home button
        button_home = Button(Home_Page, text="Home", font=("Arial", 12, 'bold'), bg="#E4E7E8", activebackground="#E4E7E8", 
                                    foreground="blue", activeforeground="blue", height=1, width=5, borderwidth=0, bd=0, relief=FLAT)                      
        button_home.place(x=95, y=15)

        # about us button
        button_about = Button(Home_Page, text="About Us", font=("Arial", 12, 'bold'), bg="#E4E7E8", activebackground="#E4E7E8", 
                                    foreground="#242424", activeforeground="blue", height=1, width=8, borderwidth=0, bd=0, relief=FLAT, 
                                    command=lambda: AboutPage())                      
        button_about.place(x=170, y=15)

        # log in button
        button_about = Button(Home_Page, text="Log In", font=("Arial", 12, 'bold'), bg="#E4E7E8", activebackground="#E4E7E8", 
                                    foreground="#242424" ,activeforeground="blue", height=1, width=8, borderwidth=0, bd=0, relief=FLAT,
                                    command=lambda: LoginPage())                      
        button_about.place(x=260, y=15)



        Home_Page.mainloop()


# -------------------- ABOUT US -------------------- #

def AboutPage():
    try:
        if 'Home_Page' in globals():
            Home_Page.destroy()
        
    finally:
        global About_Page
        About_Page = Tk()
        About_Page.geometry("1200x675+365+130")
        About_Page.resizable(width=False, height=False)
        About_Page.title("Pag-IBIG Fund")

        # ----- add background picture
        file_bg_about = PhotoImage(file="bgabout1.png", master=About_Page)
        bg_about = Label(About_Page, image=file_bg_about, borderwidth=0)
        bg_about.place(x=0, y=0)

        # ----- add register button
        text_register = Label(About_Page, text="Want to be a Pag-IBIG member?", font=("Arial", 9), bg="#E4E7E8", foreground="black")
        text_register.place(x=790, y=20)
        button_register = Button(About_Page, text="Register Here", font=("Arial", 16), bg="yellow", activebackground="blue", 
                                 foreground="#242424", activeforeground="white", height=1, width=13, borderwidth=0, bd=0, relief=FLAT)                      
        button_register.place(x=980, y=9)

        # ----- add navigation buttons
        # home button
        button_home = Button(About_Page, text="Home", font=("Arial", 12, 'bold'), bg="#E4E7E8", activebackground="#E4E7E8", 
                                    foreground="#242424", activeforeground="blue", height=1, width=5, borderwidth=0, bd=0, relief=FLAT, 
                                    command=lambda: HomePage())                      
        button_home.place(x=95, y=15)

        # about us button
        button_about = Button(About_Page, text="About Us", font=("Arial", 12, 'bold'), bg="#E4E7E8", activebackground="#E4E7E8", 
                                    foreground="blue", activeforeground="blue", height=1, width=8, borderwidth=0, bd=0, relief=FLAT)                      
        button_about.place(x=170, y=15)

        # log in button
        button_about = Button(About_Page, text="Log In", font=("Arial", 12, 'bold'), bg="#E4E7E8", activebackground="#E4E7E8", 
                                    foreground="#242424" ,activeforeground="blue", height=1, width=8, borderwidth=0, bd=0, relief=FLAT,
                                    command=lambda: LoginPage())                      
        button_about.place(x=260, y=15)

        # ----- about us choices button
        # chairman button
        button_chairman = Button(About_Page, text="Chairman of the\nBoard", font=("Arial", 12), bg="#BDC4BB", activebackground="#BDC4BB",
                                    foreground="#242424", activeforeground="#242424", height=2, width=15, borderwidth=0, bd=0, relief=FLAT,
                                    command=lambda: AboutPage())
        button_chairman.place(x=80, y=162)
        # vision button
        button_vision = Button(About_Page, text="Vision", font=("Arial", 13), bg="#FFFFFF", activebackground="#FFFFFF",
                               foreground="#242424", activeforeground="#242424", height=1, width=15, borderwidth=0, bd=0, relief=FLAT,
                               command=lambda: VisionPage())
        button_vision.place(x=80, y=225)

        # mission button
        button_mission = Button(About_Page, text="Mission", font=("Arial", 13), bg="#FFFFFF", activebackground="#FFFFFF",
                               foreground="#242424", activeforeground="#242424", height=1, width=15, borderwidth=0, bd=0, relief=FLAT,
                               command=lambda: MissionPage())
        button_mission.place(x=80, y=285)

        # other button
        button_others = Button(About_Page, text="Others", font=("Arial", 13), bg="#FFFFFF", activebackground="#FFFFFF",
                               foreground="#242424", activeforeground="#242424", height=1, width=15, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: OthersPage())
        button_others.place(x=80, y=345)


        About_Page.mainloop()


# -------------------- VISION PAGE -------------------- #
def VisionPage():
     # ----- add background picture
    file_bg_about = PhotoImage(file="bgabout2.png", master=About_Page)
    bg_about = Label(About_Page, image=file_bg_about, borderwidth=0)
    bg_about.place(x=0, y=0)

    # ----- add register button
    text_register = Label(About_Page, text="Want to be a Pag-IBIG member?", font=("Arial", 9), bg="#E4E7E8", foreground="black")
    text_register.place(x=790, y=20)
    button_register = Button(About_Page, text="Register Here", font=("Arial", 16), bg="yellow", activebackground="blue", 
                                foreground="#242424", activeforeground="white", height=1, width=13, borderwidth=0, bd=0, relief=FLAT)                      
    button_register.place(x=980, y=9)

    # home button
    button_home = Button(About_Page, text="Home", font=("Arial", 12, 'bold'), bg="#E4E7E8", activebackground="#E4E7E8", 
                            foreground="#242424", activeforeground="blue", height=1, width=5, borderwidth=0, bd=0, relief=FLAT, 
                            command=lambda: HomePage())                      
    button_home.place(x=95, y=15)

    # about us button
    button_about = Button(About_Page, text="About Us", font=("Arial", 12, 'bold'), bg="#E4E7E8", activebackground="#E4E7E8", 
                                foreground="blue", activeforeground="blue", height=1, width=8, borderwidth=0, bd=0, relief=FLAT)                      
    button_about.place(x=170, y=15)

    # log in button
    button_about = Button(About_Page, text="Log In", font=("Arial", 12, 'bold'), bg="#E4E7E8", activebackground="#E4E7E8", 
                                foreground="#242424" ,activeforeground="blue", height=1, width=8, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: LoginPage())                      
    button_about.place(x=260, y=15)


    # ----- about us choices button
    # chairman button
    button_chairman = Button(About_Page, text="Chairman of the\nBoard", font=("Arial", 12), bg="#FFFFFF", activebackground="#FFFFFF",
                                foreground="#242424", activeforeground="#242424", height=2, width=15, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: AboutPage())
    button_chairman.place(x=80, y=162)
    # vision button
    button_vision = Button(About_Page, text="Vision", font=("Arial", 13), bg="#BDC4BB", activebackground="#BDC4BB",
                                foreground="#242424", activeforeground="#242424", height=1, width=15, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: VisionPage())
    button_vision.place(x=80, y=225)

    # mission button
    button_mission = Button(About_Page, text="Mission", font=("Arial", 13), bg="#FFFFFF", activebackground="#FFFFFF",
                                foreground="#242424", activeforeground="#242424", height=1, width=15, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: MissionPage())
    button_mission.place(x=80, y=285)

    # other button
    button_others = Button(About_Page, text="Others", font=("Arial", 13), bg="#FFFFFF", activebackground="#FFFFFF",
                               foreground="#242424", activeforeground="#242424", height=1, width=15, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: OthersPage())
    button_others.place(x=80, y=345)


    About_Page.mainloop()


# -------------------- MISSION PAGE -------------------- #
def MissionPage():
     # ----- add background picture
    file_bg_about = PhotoImage(file="bgabout3.png", master=About_Page)
    bg_about = Label(About_Page, image=file_bg_about, borderwidth=0)
    bg_about.place(x=0, y=0)

    # ----- add register button
    text_register = Label(About_Page, text="Want to be a Pag-IBIG member?", font=("Arial", 9), bg="#E4E7E8", foreground="black")
    text_register.place(x=790, y=20)
    button_register = Button(About_Page, text="Register Here", font=("Arial", 16), bg="yellow", activebackground="blue", 
                                foreground="#242424", activeforeground="white", height=1, width=13, borderwidth=0, bd=0, relief=FLAT)                      
    button_register.place(x=980, y=9)

    # home button
    button_home = Button(About_Page, text="Home", font=("Arial", 12, 'bold'), bg="#E4E7E8", activebackground="#E4E7E8", 
                            foreground="#242424", activeforeground="blue", height=1, width=5, borderwidth=0, bd=0, relief=FLAT, 
                            command=lambda: HomePage())                      
    button_home.place(x=95, y=15)

    # about us button
    button_about = Button(About_Page, text="About Us", font=("Arial", 12, 'bold'), bg="#E4E7E8", activebackground="#E4E7E8", 
                                foreground="blue", activeforeground="blue", height=1, width=8, borderwidth=0, bd=0, relief=FLAT)                      
    button_about.place(x=170, y=15)

    # log in button
    button_about = Button(About_Page, text="Log In", font=("Arial", 12, 'bold'), bg="#E4E7E8", activebackground="#E4E7E8", 
                                foreground="#242424" ,activeforeground="blue", height=1, width=8, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: LoginPage())                      
    button_about.place(x=260, y=15)


    # ----- about us choices button
    # chairman button
    button_chairman = Button(About_Page, text="Chairman of the\nBoard", font=("Arial", 12), bg="#FFFFFF", activebackground="#FFFFFF",
                                foreground="#242424", activeforeground="#242424", height=2, width=15, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: AboutPage())
    button_chairman.place(x=80, y=162)
    # vision button
    button_vision = Button(About_Page, text="Vision", font=("Arial", 13), bg="#FFFFFF", activebackground="#FFFFFF",
                                foreground="#242424", activeforeground="#242424", height=1, width=15, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: VisionPage())
    button_vision.place(x=80, y=225)

    # mission button
    button_mission = Button(About_Page, text="Mission", font=("Arial", 13), bg="#BDC4BB", activebackground="#BDC4BB",
                                foreground="#242424", activeforeground="#242424", height=1, width=15, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: MissionPage())
    button_mission.place(x=80, y=285)

    # other button
    button_others = Button(About_Page, text="Others", font=("Arial", 13), bg="#FFFFFF", activebackground="#FFFFFF",
                               foreground="#242424", activeforeground="#242424", height=1, width=15, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: OthersPage())
    button_others.place(x=80, y=345)


    About_Page.mainloop()


# -------------------- OTHERS PAGE -------------------- #
def OthersPage():
     # ----- add background picture
    file_bg_about = PhotoImage(file="bgabout4.png", master=About_Page)
    bg_about = Label(About_Page, image=file_bg_about, borderwidth=0)
    bg_about.place(x=0, y=0)

    # ----- add register button
    text_register = Label(About_Page, text="Want to be a Pag-IBIG member?", font=("Arial", 9), bg="#E4E7E8", foreground="black")
    text_register.place(x=790, y=20)
    button_register = Button(About_Page, text="Register Here", font=("Arial", 16), bg="yellow", activebackground="blue", 
                                foreground="#242424", activeforeground="white", height=1, width=13, borderwidth=0, bd=0, relief=FLAT)                      
    button_register.place(x=980, y=9)

    # home button
    button_home = Button(About_Page, text="Home", font=("Arial", 12, 'bold'), bg="#E4E7E8", activebackground="#E4E7E8", 
                            foreground="#242424", activeforeground="blue", height=1, width=5, borderwidth=0, bd=0, relief=FLAT, 
                            command=lambda: HomePage())                      
    button_home.place(x=95, y=15)

    # about us button
    button_about = Button(About_Page, text="About Us", font=("Arial", 12, 'bold'), bg="#E4E7E8", activebackground="#E4E7E8", 
                                foreground="blue", activeforeground="blue", height=1, width=8, borderwidth=0, bd=0, relief=FLAT)                      
    button_about.place(x=170, y=15)

    # log in button
    button_about = Button(About_Page, text="Log In", font=("Arial", 12, 'bold'), bg="#E4E7E8", activebackground="#E4E7E8", 
                                foreground="#242424" ,activeforeground="blue", height=1, width=8, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: LoginPage())                      
    button_about.place(x=260, y=15)


    # ----- about us choices button
    # chairman button
    button_chairman = Button(About_Page, text="Chairman of the\nBoard", font=("Arial", 12), bg="#FFFFFF", activebackground="#FFFFFF",
                                foreground="#242424", activeforeground="#242424", height=2, width=15, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: AboutPage())
    button_chairman.place(x=80, y=162)
    # vision button
    button_vision = Button(About_Page, text="Vision", font=("Arial", 13), bg="#FFFFFF", activebackground="#FFFFFF",
                                foreground="#242424", activeforeground="#242424", height=1, width=15, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: VisionPage())
    button_vision.place(x=80, y=225)

    # mission button
    button_mission = Button(About_Page, text="Mission", font=("Arial", 13), bg="#FFFFFF", activebackground="#FFFFFF",
                                foreground="#242424", activeforeground="#242424", height=1, width=15, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: MissionPage())
    button_mission.place(x=80, y=285)

    # other button
    button_others = Button(About_Page, text="Others", font=("Arial", 13), bg="#BDC4BB", activebackground="#BDC4BB",
                               foreground="#242424", activeforeground="#242424", height=1, width=15, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: OthersPage())
    button_others.place(x=80, y=345)


    About_Page.mainloop()


# -------------------- REGISTER PAGE -------------------- #
def RegisterPage():
    try:
        # check what window currently exist then destroy before opening new window
        if 'About_Page' in globals():
            About_Page.destroy()
        if 'Home_Page' in globals():
            Home_Page.destroy()

    finally:
        # ----- create a window
        global Register_Page
        Register_Page = Tk()
        Register_Page.geometry("1200x675+365+130")
        Register_Page.resizable(width=False, height=False)
        Register_Page.title("Pag-IBIG Fund")


HomePage()

