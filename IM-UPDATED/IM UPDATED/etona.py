from tkinter import * # import everying in tkinter
import mysql.connector

'''
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
        username_textbox = Text(Login_Page, height=1, width=21)
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
'''


My_Window = Tk()
My_Window.geometry("1200x675+365+130")
My_Window.resizable(width=False, height=False)
My_Window.title("Pag-IBIG Fund")

# ------------------------------ HOME ------------------------------#

def HomePage():

    # ----- ADD BACKGROUND PICTURE ----- #
    file_bg_window = PhotoImage(file="bghomepage.png", master=My_Window)
    bg_window = Label(My_Window, image=file_bg_window, borderwidth=0)
    bg_window.place(x=0, y=0)

    # ----- add register button
    text_register = Label(My_Window, text="Want to be a Pag-IBIG member?  | ", font=("Arial", 9), bg="#E4E7E8", foreground="black")
    text_register.place(x=860, y=20)
    button_register = Button(My_Window, text="Register Here", font=("Arial", 9), bg="yellow", activebackground="blue", 
                                 foreground="#242424", activeforeground="white", height=1, width=13, borderwidth=0, bd=0, relief=FLAT,
                                 command=lambda: RegisterPage())                      
    button_register.place(x=1070, y=19)
        
    # ----- ADD NAVIGATION BUTTONS ----- #
    # home button
    button_home = Button(My_Window, text="Home", font=("Arial", 12, 'bold'), bg="#E4E7E8", activebackground="#E4E7E8", 
                            foreground="blue", activeforeground="blue", height=1, width=5, borderwidth=0, bd=0, relief=FLAT)                      
    button_home.place(x=95, y=15)

    # about us button
    button_about = Button(My_Window, text="About Us", font=("Arial", 12, 'bold'), bg="#E4E7E8", activebackground="#E4E7E8", 
                            foreground="#242424", activeforeground="blue", height=1, width=8, borderwidth=0, bd=0, relief=FLAT,
                            command=lambda: AboutPage())                      
    button_about.place(x=170, y=15)

    # log in button
    button_about = Button(My_Window, text="Log In", font=("Arial", 12, 'bold'), bg="#E4E7E8", activebackground="#E4E7E8", 
                            foreground="#242424" ,activeforeground="blue", height=1, width=8, borderwidth=0, bd=0, relief=FLAT,
                            command=lambda: LoginPage())                      
    button_about.place(x=260, y=15)



    My_Window.mainloop()


# ------------------------------ ABOUT US ------------------------------#

# ABOUT US PAGE 1
def AboutPage():
    # ----- ADD BACKGROUND PICTURE ----- #
    file_bg_window = PhotoImage(file="bgabout1.png", master=My_Window)
    bg_window = Label(My_Window, image=file_bg_window, borderwidth=0)
    bg_window.place(x=0, y=0)


    # ----- ADD REGISTER BUTTON ----- #
    text_register = Label(My_Window, text="Want to be a Pag-IBIG member?", font=("Arial", 9), bg="#E4E7E8", foreground="black")
    text_register.place(x=790, y=20)
    button_register = Button(My_Window, text="Register Here", font=("Arial", 16), bg="yellow", activebackground="blue", 
                                 foreground="#242424", activeforeground="white", height=1, width=13, borderwidth=0, bd=0, relief=FLAT,
                                 command=lambda: RegisterPage())                      
    button_register.place(x=980, y=9)



    # ----- ADD NAVIGATION BUTTONS ----- #
    # home button
    button_home = Button(My_Window, text="Home", font=("Arial", 12, 'bold'), bg="#E4E7E8", activebackground="#E4E7E8", 
                            foreground="#242424", activeforeground="blue", height=1, width=5, borderwidth=0, bd=0, relief=FLAT,
                            command=lambda: HomePage())                      
    button_home.place(x=95, y=15)

    # about us button
    button_about = Button(My_Window, text="About Us", font=("Arial", 12, 'bold'), bg="#E4E7E8", activebackground="#E4E7E8", 
                            foreground="blue", activeforeground="blue", height=1, width=8, borderwidth=0, bd=0, relief=FLAT,
                            command=lambda: AboutPage())                      
    button_about.place(x=170, y=15)

    # log in button
    button_about = Button(My_Window, text="Log In", font=("Arial", 12, 'bold'), bg="#E4E7E8", activebackground="#E4E7E8", 
                            foreground="#242424" ,activeforeground="blue", height=1, width=8, borderwidth=0, bd=0, relief=FLAT,
                            command=lambda: LoginPage()
                            )                      
    button_about.place(x=260, y=15)



    # ----- ADD ABOUT US FEATURES BUTTONS ----- #
    # Chairman of the Board
    button_chairman = Button(My_Window, text="Chairman of the\nBoard", font=("Arial", 13), bg="yellow", activebackground="yellow",
                                foreground="#242424", activeforeground="#242424", height=2, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: AboutPage())
    button_chairman.place(x=45, y=150)

    # Mission / Vision
    button_mission = Button(My_Window, text="Mission / Vision", font=("Arial", 13), bg="white", activebackground="white",
                                foreground="#242424", activeforeground="#242424", height=2, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: AboutPage2())
    button_mission.place(x=45, y=220)

    # Others
    button_others = Button(My_Window, text="Others", font=("Arial", 13), bg="white", activebackground="white",
                                foreground="#242424", activeforeground="#242424", height=2, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: AboutPage3()
                                )
    button_others.place(x=45, y=285)

    My_Window.mainloop()

# ABOUT US PAGE 2
def AboutPage2():
    # ----- ADD BACKGROUND PICTURE ----- #
    file_bg_window = PhotoImage(file="bgabout2.png", master=My_Window)
    bg_window = Label(My_Window, image=file_bg_window, borderwidth=0)
    bg_window.place(x=0, y=0)


    # ----- ADD REGISTER BUTTON ----- #
    text_register = Label(My_Window, text="Want to be a Pag-IBIG member?", font=("Arial", 9), bg="#E4E7E8", foreground="black")
    text_register.place(x=790, y=20)
    button_register = Button(My_Window, text="Register Here", font=("Arial", 16), bg="yellow", activebackground="blue", 
                                 foreground="#242424", activeforeground="white", height=1, width=13, borderwidth=0, bd=0, relief=FLAT,
                                 command=lambda: RegisterPage())                      
    button_register.place(x=980, y=9)



    # ----- ADD NAVIGATION BUTTONS ----- #
    # home button
    button_home = Button(My_Window, text="Home", font=("Arial", 12, 'bold'), bg="#E4E7E8", activebackground="#E4E7E8", 
                            foreground="#242424", activeforeground="blue", height=1, width=5, borderwidth=0, bd=0, relief=FLAT,
                            command=lambda: HomePage())                      
    button_home.place(x=95, y=15)

    # about us button
    button_about = Button(My_Window, text="About Us", font=("Arial", 12, 'bold'), bg="#E4E7E8", activebackground="#E4E7E8", 
                            foreground="blue", activeforeground="blue", height=1, width=8, borderwidth=0, bd=0, relief=FLAT,
                            command=lambda: AboutPage())                      
    button_about.place(x=170, y=15)

    # log in button
    button_about = Button(My_Window, text="Log In", font=("Arial", 12, 'bold'), bg="#E4E7E8", activebackground="#E4E7E8", 
                            foreground="#242424" ,activeforeground="blue", height=1, width=8, borderwidth=0, bd=0, relief=FLAT,
                            command=lambda: LoginPage()
                            )                      
    button_about.place(x=260, y=15)



    # ----- ADD ABOUT US FEATURES BUTTONS ----- #
    # Chairman of the Board
    button_chairman = Button(My_Window, text="Chairman of the\nBoard", font=("Arial", 13), bg="white", activebackground="white",
                                foreground="#242424", activeforeground="#242424", height=2, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: AboutPage())
    button_chairman.place(x=45, y=150)

    # Mission / Vision
    button_mission = Button(My_Window, text="Mission / Vision", font=("Arial", 13), bg="yellow", activebackground="yellow",
                                foreground="#242424", activeforeground="#242424", height=2, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: AboutPage2())
    button_mission.place(x=45, y=220)

    # Others
    button_others = Button(My_Window, text="Others", font=("Arial", 13), bg="white", activebackground="white",
                                foreground="#242424", activeforeground="#242424", height=2, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: AboutPage3()
                                )
    button_others.place(x=45, y=285)

    My_Window.mainloop()

# ABOUT US PAGE 3
def AboutPage3():
    # ----- ADD BACKGROUND PICTURE ----- #
    file_bg_window = PhotoImage(file="bgabout3.png", master=My_Window)
    bg_window = Label(My_Window, image=file_bg_window, borderwidth=0)
    bg_window.place(x=0, y=0)


    # ----- ADD REGISTER BUTTON ----- #
    text_register = Label(My_Window, text="Want to be a Pag-IBIG member?", font=("Arial", 9), bg="#E4E7E8", foreground="black")
    text_register.place(x=790, y=20)
    button_register = Button(My_Window, text="Register Here", font=("Arial", 16), bg="yellow", activebackground="blue", 
                                 foreground="#242424", activeforeground="white", height=1, width=13, borderwidth=0, bd=0, relief=FLAT,
                                 command=lambda: RegisterPage())                      
    button_register.place(x=980, y=9)



    # ----- ADD NAVIGATION BUTTONS ----- #
    # home button
    button_home = Button(My_Window, text="Home", font=("Arial", 12, 'bold'), bg="#E4E7E8", activebackground="#E4E7E8", 
                            foreground="#242424", activeforeground="blue", height=1, width=5, borderwidth=0, bd=0, relief=FLAT,
                            command=lambda: HomePage())                      
    button_home.place(x=95, y=15)

    # about us button
    button_about = Button(My_Window, text="About Us", font=("Arial", 12, 'bold'), bg="#E4E7E8", activebackground="#E4E7E8", 
                            foreground="blue", activeforeground="blue", height=1, width=8, borderwidth=0, bd=0, relief=FLAT,
                            command=lambda: AboutPage())                      
    button_about.place(x=170, y=15)

    # log in button
    button_about = Button(My_Window, text="Log In", font=("Arial", 12, 'bold'), bg="#E4E7E8", activebackground="#E4E7E8", 
                            foreground="#242424" ,activeforeground="blue", height=1, width=8, borderwidth=0, bd=0, relief=FLAT,
                            command=lambda: LoginPage()
                            )                      
    button_about.place(x=260, y=15)



    # ----- ADD ABOUT US FEATURES BUTTONS ----- #
    # Chairman of the Board
    button_chairman = Button(My_Window, text="Chairman of the\nBoard", font=("Arial", 13), bg="white", activebackground="white",
                                foreground="#242424", activeforeground="#242424", height=2, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: AboutPage())
    button_chairman.place(x=45, y=150)

    # Mission / Vision
    button_mission = Button(My_Window, text="Mission / Vision", font=("Arial", 13), bg="white", activebackground="white",
                                foreground="#242424", activeforeground="#242424", height=2, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: AboutPage2())
    button_mission.place(x=45, y=220)

    # Others
    button_others = Button(My_Window, text="Others", font=("Arial", 13), bg="yellow", activebackground="yellow",
                                foreground="#242424", activeforeground="#242424", height=2, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: AboutPage3())
    button_others.place(x=45, y=285)

    My_Window.mainloop()


# ------------------------------ LOG IN ------------------------------#

# LOG IN PAGE 
import tkinter as tk
import mysql.connector
from tkinter import *

My_Window = tk.Tk()
My_Window.title("Pag-IBIG Fund")
def check_credentials(MIDCode, password):
    cnx = mysql.connector.connect(
        host='localhost',
        user='andy',
        password='Andydy212003*',
        database='project_database'
    )
    cursor = cnx.cursor()

    query = "SELECT MIDCode, password FROM login WHERE MIDCode = %s"
    cursor.execute(query, (MIDCode,))
    user = cursor.fetchone()

    if user:
        login, stored_password = user
        if stored_password == password:
            return login

    return None

def retrieve_details(login):
    cnx = mysql.connector.connect(
        host='localhost',
        user='andy',
        password='Andydy212003*',
        database='project_database'
    )
    cursor = cnx.cursor()

    query = "SELECT * FROM memberdetails WHERE MIDNumber = %s"
    cursor.execute(query, (login,))
    rows = cursor.fetchall()

    # Print the column headers
    columns = [desc[0] for desc in cursor.description]
    print(', '.join(columns))

    # Print the rows
    for row in rows:
        print(', '.join(str(col) for col in row))

def login_action():
    MIDCode = MIDCode_textbox.get("1.0", tk.END).strip()
    password = password_textbox.get("1.0", tk.END).strip()
    login = check_credentials(MIDCode, password)


    if login:
        caption = tk.Label(My_Window, text="Login successful.", font=("Arial", 10), fg='green', bg="white")
        caption.place(x=775, y=480)
        print("Login successful. User ID:", login)
        retrieve_details(login)
    else:
        caption = tk.Label(My_Window, text="Invalid username or password.", font=("Arial", 10), fg='red', bg="white")
        caption.place(x=722, y=480)


def LoginPage():
    global MIDCode_textbox, password_textbox

    # Set the window size and position
    window_width = 1200
    window_height = 675
    screen_width = My_Window.winfo_screenwidth()
    screen_height = My_Window.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    My_Window.geometry("1200x675")
    # Disable window resizing
    My_Window.resizable(False, False)

    # put background picture
    file_bg_login = tk.PhotoImage(file="login.png")
    bg_login = tk.Label(My_Window, image=file_bg_login)
    bg_login.place(x=0, y=0)

    # put textbox for MIDCode
    MIDCode_textbox = tk.Text(My_Window, height=1, width=25)
    MIDCode_textbox.configure(font=("Comic Sans MS", 15))
    MIDCode_textbox.configure(borderwidth=2, relief="raised", bg='light gray')
    MIDCode_textbox.place(x=665, y=305)
    caption = tk.Label(My_Window, text="MIDCode", font=("Arial", 8), bg="white")
    caption.place(x=665, y=285)


    # put textbox for password
    password_textbox = tk.Text(My_Window, height=1, width=25)
    password_textbox.configure(font=("Comic Sans MS", 15))
    password_textbox.configure(borderwidth=2, relief="raised", bg='light gray')
    password_textbox.place(x=665, y=370)
    caption = tk.Label(My_Window, text="Password", font=("Arial", 8), bg="white")
    caption.place(x=665, y=350)

    # put enter button
    button = Button(My_Window,text="SIGN IN", font=("Arial", 13, 'bold'), width=30, bg="light blue", command=login_action)
    button.place(x=664, y=430)

    # put create account button
    button_member_reg = tk.Button(My_Window, text="Not yet a member?", font=("Arial", 10, 'italic','bold'), bg="White", fg="gray", bd=0,
                                  activebackground="white")
    button_member_reg.place(x=760, y=560)
    My_Window.mainloop()

# ------------------------------ REGISTER ------------------------------#

# REGISTRATION PAGE 1
def RegisterPage():
        
        # change bg picture
        file_bg_window = PhotoImage(file="bgreg1.png", master=My_Window)
        bg_window = Label(My_Window, image=file_bg_window, borderwidth=0)
        bg_window.place(x=0, y=0)


        # ----- inputs ----- # 

        # text box for name
        name_textbox = Text(My_Window, height=1, width=27)
        name_textbox.configure(font=("Arial", 15))
        name_textbox.place(x=338, y=230)
        
        # text box for bdate
        bdate_textbox = Text(My_Window, height=1, width=19)
        bdate_textbox.configure(font=("Arial", 15))
        bdate_textbox.place(x=665, y=230)

        # textbox for bplace
        bplace_textbox = Text(My_Window, height=1, width=17)
        bplace_textbox.configure(font=("Arial", 15))
        bplace_textbox.place(x=908, y=230)

        # textbox for address
        address_textbox = Text(My_Window, height=1, width=50)
        address_textbox.configure(font=("Arial", 15))
        address_textbox.place(x=338, y=340)

        # radiobuttons for sex
        sex = StringVar()
        male_button = Radiobutton(My_Window, text = "Male", font=("Arial", 12), bg="white", activebackground="white", foreground="#060606", 
                                    activeforeground="#060606", height=1, width=8, bd=0, borderwidth=0, relief=FLAT,
                                    variable=sex, value='Male')
        male_button.place(x=910, y=341)
        female_button = Radiobutton(My_Window, text = "Female", font=("Arial", 12), bg="white", activebackground="white", foreground="#060606", 
                                    activeforeground="#060606", height=1, width=8, bd=0, borderwidth=0, relief=FLAT,
                                    variable=sex, value='Female')
        female_button.place(x=1000, y=341)

        # textbox for spouse
        spouse_textbox = Text(My_Window, height=1, width=27)
        spouse_textbox.configure(font=("Arial", 15))
        spouse_textbox.place(x=338, y=450)

        # textbox for status
        status_textbox = Text(My_Window, height=1, width=19)
        status_textbox.configure(font=("Arial", 15))
        status_textbox.place(x=665, y=450)

        # textbox for citizenship
        citizenship_textbox = Text(My_Window, height=1, width=17)
        citizenship_textbox.configure(font=("Arial", 15))
        citizenship_textbox.place(x=908, y=450)

        # textbox for father's name
        father_textbox = Text(My_Window, height=1, width=27)
        father_textbox.configure(font=("Arial", 15))
        father_textbox.place(x=338, y=565)

        # textbox for mother's 
        mother_texbox = Text(My_Window, height=1, width=27)
        mother_texbox.configure(font=("Arial", 15))
        mother_texbox.place(x=665, y=565)


        # ----- buttons for other pages ----- #"

        # personal information
        button_personal = Button(My_Window, text="Personal Information", font=("Arial", 13), bg="yellow", activebackground="yellow",
                                foreground="#242424", activeforeground="#242424", height=1, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: RegisterPage())
        button_personal.place(x=40, y=192)

        # account
        button_account = Button(My_Window, text="Account", font=("Arial", 13), bg="white", activebackground="white",
                                foreground="#242424", activeforeground="#242424", height=1, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: AccountPage())
        button_account.place(x=40, y=252)

        # current work
        button_currentwork = Button(My_Window, text="Current Work", font=("Arial", 13), bg="white", activebackground="white",
                                foreground="#242424", activeforeground="#242424", height=1, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: CurrentWorkPage())
        button_currentwork.place(x=40, y=312)

        # previous work
        button_previouswork = Button(My_Window, text="Previous Work", font=("Arial", 13), bg="white", activebackground="white",
                                foreground="#242424", activeforeground="#242424", height=1, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: PreviousWorkPage())
        button_previouswork.place(x=40, y=372)

        # other information
        button_otherinfo = Button(My_Window, text="Other Information", font=("Arial", 13), bg="white", activebackground="white",
                                foreground="#242424", activeforeground="#242424", height=1, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: OtherInfoPage())
        button_otherinfo.place(x=40, y=432)

        
        # ----- SAVE BUTTON ----- #
        save_button = Button(My_Window, text="Save", font=("Arial", 11, 'bold'), bg="yellow", activebackground="yellow",
                                foreground="#242424", activeforeground="#242424", height=1, width=9, borderwidth=0, bd=0, relief=FLAT)
        save_button.place(x=1040, y=595)


        My_Window.mainloop()

# REGISTRATION PAGE 2
def AccountPage():
        
        # change bg picture
        file_bg_window = PhotoImage(file="bgreg2.png", master=My_Window)
        bg_window = Label(My_Window, image=file_bg_window, borderwidth=0)
        bg_window.place(x=0, y=0)


        # ----- inputs ----- # 

        # textbox for sss
        sss_textbox = Text(My_Window, height=1, width=27)
        sss_textbox.configure(font=("Arial", 15))
        sss_textbox.place(x=338, y=230)

        # textbox for tine
        tin_textbox = Text(My_Window, height=1, width=27)
        tin_textbox.configure(font=("Arial", 15))
        tin_textbox.place(x=693, y=230)

        # textbox for email address
        email_textbox = Text(My_Window, height=1, width=27)
        email_textbox.configure(font=("Arial", 15))
        email_textbox.place(x=338, y=340)

        # textbox for phone number
        phonenumber_textbox = Text(My_Window, height=1, width=27)
        phonenumber_textbox.configure(font=("Arial", 15))
        phonenumber_textbox.place(x=693, y=340)

        # textbox for password
        password_textbox = Text(My_Window, height=1, width=27)
        password_textbox.configure(font=("Arial", 15))
        password_textbox.place(x=338, y=450)

        # texbox for confirm password
        confirmpassword_texbox = Text(My_Window, height=1, width=27)
        confirmpassword_texbox.configure(font=("Arial", 15))
        confirmpassword_texbox.place(x=693, y=450)

        # ----- buttons for other pages ----- #"

        # personal information
        button_personal = Button(My_Window, text="Personal Information", font=("Arial", 13), bg="white", activebackground="white",
                                foreground="#242424", activeforeground="#242424", height=1, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: RegisterPage())
        button_personal.place(x=40, y=192)

        # account
        button_account = Button(My_Window, text="Account", font=("Arial", 13), bg="yellow", activebackground="yellow",
                                foreground="#242424", activeforeground="#242424", height=1, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: AccountPage())
        button_account.place(x=40, y=252)

        # current work
        button_currentwork = Button(My_Window, text="Current Work", font=("Arial", 13), bg="white", activebackground="white",
                                foreground="#242424", activeforeground="#242424", height=1, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: CurrentWorkPage())
        button_currentwork.place(x=40, y=312)

        # previous work
        button_previouswork = Button(My_Window, text="Previous Work", font=("Arial", 13), bg="white", activebackground="white",
                                foreground="#242424", activeforeground="#242424", height=1, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: PreviousWorkPage())
        button_previouswork.place(x=40, y=372)

        # other information
        button_otherinfo = Button(My_Window, text="Other Information", font=("Arial", 13), bg="white", activebackground="white",
                                foreground="#242424", activeforeground="#242424", height=1, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: OtherInfoPage())
        button_otherinfo.place(x=40, y=432)


        # ----- SAVE BUTTON ----- #
        save_button = Button(My_Window, text="Save", font=("Arial", 11, 'bold'), bg="yellow", activebackground="yellow",
                                foreground="#242424", activeforeground="#242424", height=1, width=9, borderwidth=0, bd=0, relief=FLAT)
        save_button.place(x=1040, y=595)


        My_Window.mainloop()

# REGISTRATION PAGE 3
def CurrentWorkPage():
        
        # change bg picture
        file_bg_window = PhotoImage(file="bgreg3.png", master=My_Window)
        bg_window = Label(My_Window, image=file_bg_window, borderwidth=0)
        bg_window.place(x=0, y=0)


        # ----- inputs ----- # 

        # textbox for employee number
        cur_employeenum_textbox = Text(My_Window, height=1, width=24)
        cur_employeenum_textbox.configure(font=("Arial", 15))
        cur_employeenum_textbox.place(x=338, y=230)

        # textbox for occupation
        cur_occupation_textbox = Text(My_Window, height=1, width=20)
        cur_occupation_textbox.configure(font=("Arial", 15))
        cur_occupation_textbox.place(x=638, y=230)

        # radiobutton for employment status
        cur_employmentstatus = StringVar()
        fulltime_button = Radiobutton(My_Window, text = "Full-Time", font=("Arial", 11), bg="white", activebackground="white", foreground="#060606", 
                                    activeforeground="#060606", height=1, width=8, variable=cur_employmentstatus, value='Full-Time')
        fulltime_button.place(x=895, y=230)
        parttime_button = Radiobutton(My_Window, text = "Part-Time", font=("Arial", 11), bg="white", activebackground="white", foreground="#060606", 
                                    activeforeground="#060606", height=1, width=8, variable=cur_employmentstatus, value='Part-Time')
        parttime_button.place(x=995, y=230)

        # textbox for employer id
        cur_employerid_textbox = Text(My_Window, height=1, width=26)
        cur_employerid_textbox.configure(font=("Arial", 15))
        cur_employerid_textbox.place(x=338, y=340)


        # textbox for employer name
        cur_employername_texbox = Text(My_Window, height=1, width=39)
        cur_employername_texbox.configure(font=("Arial", 15))
        cur_employername_texbox.place(x=660, y=340)
        
        # textbox for employer address
        cur_employeraddress_textbox = Text(My_Window, height=1, width=69)
        cur_employeraddress_textbox.configure(font=("Arial", 15))
        cur_employeraddress_textbox.place(x=338, y=455)

        # textbox for date employed
        cur_dateemployed_texbox = Text(My_Window, height=1, width=28)
        cur_dateemployed_texbox.configure(font=("Arial", 15))
        cur_dateemployed_texbox.place(x=338, y=570)

        # textbox for monthly income
        cur_monthlyincome_textbox = Text(My_Window, height=1, width=30)
        cur_monthlyincome_textbox.configure(font=("Arial", 15))
        cur_monthlyincome_textbox.place(x=680, y=570)


        # ----- buttons for other pages ----- #"

        # personal information
        button_personal = Button(My_Window, text="Personal Information", font=("Arial", 13), bg="white", activebackground="white",
                                foreground="#242424", activeforeground="#242424", height=1, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: RegisterPage())
        button_personal.place(x=40, y=192)

        # account
        button_account = Button(My_Window, text="Account", font=("Arial", 13), bg="white", activebackground="white",
                                foreground="#242424", activeforeground="#242424", height=1, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: AccountPage())
        button_account.place(x=40, y=252)

        # current work
        button_currentwork = Button(My_Window, text="Current Work", font=("Arial", 13), bg="yellow", activebackground="yellow",
                                foreground="#242424", activeforeground="#242424", height=1, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: CurrentWorkPage())
        button_currentwork.place(x=40, y=312)

        # previous work
        button_previouswork = Button(My_Window, text="Previous Work", font=("Arial", 13), bg="white", activebackground="white",
                                foreground="#242424", activeforeground="#242424", height=1, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: PreviousWorkPage())
        button_previouswork.place(x=40, y=372)

        # other information
        button_otherinfo = Button(My_Window, text="Other Information", font=("Arial", 13), bg="white", activebackground="white",
                                foreground="#242424", activeforeground="#242424", height=1, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: OtherInfoPage())
        button_otherinfo.place(x=40, y=432)


        # ----- SAVE BUTTON ----- #
        save_button = Button(My_Window, text="Save", font=("Arial", 11, 'bold'), bg="yellow", activebackground="yellow",
                                foreground="#242424", activeforeground="#242424", height=1, width=9, borderwidth=0, bd=0, relief=FLAT)
        save_button.place(x=1040, y=595)

        My_Window.mainloop()

# REGISTRATION PAGE 4
def PreviousWorkPage():
        
        # change bg picture
        file_bg_window = PhotoImage(file="bgreg4.png", master=My_Window)
        bg_window = Label(My_Window, image=file_bg_window, borderwidth=0)
        bg_window.place(x=0, y=0)


        # ----- inputs ----- # 

        # textbox for employee number
        prev_employeenum_textbox = Text(My_Window, height=1, width=24)
        prev_employeenum_textbox.configure(font=("Arial", 15))
        prev_employeenum_textbox.place(x=338, y=230)

        # textbox for occupation
        prev_occupation_textbox = Text(My_Window, height=1, width=20)
        prev_occupation_textbox.configure(font=("Arial", 15))
        prev_occupation_textbox.place(x=638, y=230)

        # radiobutton for employment status
        prev_employmentstatus = StringVar()
        fulltime_button = Radiobutton(My_Window, text = "Full-Time", font=("Arial", 11), bg="white", activebackground="white", foreground="#060606", 
                                    activeforeground="#060606", height=1, width=8, variable=prev_employmentstatus, value='Full-Time')
        fulltime_button.place(x=895, y=230)
        parttime_button = Radiobutton(My_Window, text = "Part-Time", font=("Arial", 11), bg="white", activebackground="white", foreground="#060606", 
                                    activeforeground="#060606", height=1, width=8, variable=prev_employmentstatus, value='Part-Time')
        parttime_button.place(x=995, y=230)

        # textbox for employer id
        prev_employerid_textbox = Text(My_Window, height=1, width=26)
        prev_employerid_textbox.configure(font=("Arial", 15))
        prev_employerid_textbox.place(x=338, y=340)


        # textbox for employer name
        prev_employername_texbox = Text(My_Window, height=1, width=39)
        prev_employername_texbox.configure(font=("Arial", 15))
        prev_employername_texbox.place(x=660, y=340)
        
        # textbox for employer address
        prev_employeraddress_textbox = Text(My_Window, height=1, width=69)
        prev_employeraddress_textbox.configure(font=("Arial", 15))
        prev_employeraddress_textbox.place(x=338, y=455)

        # textbox for date employed
        prev_dateemployed_texbox = Text(My_Window, height=1, width=28)
        prev_dateemployed_texbox.configure(font=("Arial", 15))
        prev_dateemployed_texbox.place(x=338, y=570)

        # textbox for monthly income
        prev_monthlyincome_textbox = Text(My_Window, height=1, width=30)
        prev_monthlyincome_textbox.configure(font=("Arial", 15))
        prev_monthlyincome_textbox.place(x=680, y=570)

        
        # ----- buttons for other pages ----- #"

        # personal information
        button_personal = Button(My_Window, text="Personal Information", font=("Arial", 13), bg="white", activebackground="white",
                                foreground="#242424", activeforeground="#242424", height=1, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: RegisterPage())
        button_personal.place(x=40, y=192)

        # account
        button_account = Button(My_Window, text="Account", font=("Arial", 13), bg="white", activebackground="white",
                                foreground="#242424", activeforeground="#242424", height=1, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: AccountPage())
        button_account.place(x=40, y=252)

        # current work
        button_currentwork = Button(My_Window, text="Current Work", font=("Arial", 13), bg="white", activebackground="white",
                                foreground="#242424", activeforeground="#242424", height=1, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: CurrentWorkPage())
        button_currentwork.place(x=40, y=312)


        # previous work
        button_previouswork = Button(My_Window, text="Previous Work", font=("Arial", 13), bg="yellow", activebackground="yellow",
                                foreground="#242424", activeforeground="#242424", height=1, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: PreviousWorkPage())
        button_previouswork.place(x=40, y=372)

        # other information
        button_otherinfo = Button(My_Window, text="Other Information", font=("Arial", 13), bg="white", activebackground="white",
                                foreground="#242424", activeforeground="#242424", height=1, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: OtherInfoPage())
        button_otherinfo.place(x=40, y=432)


        # ----- SAVE BUTTON ----- #
        save_button = Button(My_Window, text="Save", font=("Arial", 11, 'bold'), bg="yellow", activebackground="yellow",
                                foreground="#242424", activeforeground="#242424", height=1, width=9, borderwidth=0, bd=0, relief=FLAT)
        save_button.place(x=1040, y=595)

        My_Window.mainloop()

# REGISTRATION PAGE 5
def OtherInfoPage():
        
        # change bg picture
        file_bg_window = PhotoImage(file="bgreg5.png", master=My_Window)
        bg_window = Label(My_Window, image=file_bg_window, borderwidth=0)
        bg_window.place(x=0, y=0)


        # ----- inputs ----- # 

        # textbox for heirname
        heirname_textbox = Text(My_Window, height=1, width=31)
        heirname_textbox.configure(font=("Arial", 15))
        heirname_textbox.place(x=338, y=230)

        # textbox for heirname bdate
        heirname_bdate_textbox = Text(My_Window, height=1, width=31)
        heirname_bdate_textbox.configure(font=("Arial", 15))
        heirname_bdate_textbox.place(x=728, y=230)

        # radiobutton for membership category
        membershipcategory = StringVar()
        mandatory_button = Radiobutton(My_Window, text = "Mandatory", font=("Arial", 13), bg="white", activebackground="white", foreground="#060606", 
                                        activeforeground="#060606", height=1, width=12, bd=0, borderwidth=0, relief=FLAT,
                                        variable=membershipcategory, value='Male')
        mandatory_button.place(x=338, y=341)
        voluntary_button = Radiobutton(My_Window, text = "Voluntary", font=("Arial", 13), bg="white", activebackground="white", foreground="#060606", 
                                        activeforeground="#060606", height=1, width=12, bd=0, borderwidth=0, relief=FLAT,
                                        variable=membershipcategory, value='Female')
        voluntary_button.place(x=470, y=341)

        # radiobutton for membership savings payment
        membershippayment = StringVar()
        monthly_button = Radiobutton(My_Window, text = "Monthly", font=("Arial", 13), bg="white", activebackground="white", foreground="#060606", 
                                        activeforeground="#060606", height=1, width=12, bd=0, borderwidth=0, relief=FLAT,
                                        variable=membershippayment, value='Male')
        monthly_button.place(x=730, y=341)
        yearly_button = Radiobutton(My_Window, text = "Yearly", font=("Arial", 13), bg="white", activebackground="white", foreground="#060606", 
                                        activeforeground="#060606", height=1, width=12, bd=0, borderwidth=0, relief=FLAT,
                                        variable=membershippayment, value='Female')
        yearly_button.place(x=860, y=341)
        

        # ----- buttons for other pages ----- #"

        # personal information
        button_personal = Button(My_Window, text="Personal Information", font=("Arial", 13), bg="white", activebackground="white",
                                foreground="#242424", activeforeground="#242424", height=1, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: RegisterPage())
        button_personal.place(x=40, y=192)

        # account
        button_account = Button(My_Window, text="Account", font=("Arial", 13), bg="white", activebackground="white",
                                foreground="#242424", activeforeground="#242424", height=1, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: AccountPage())
        button_account.place(x=40, y=252)

        # current work
        button_currentwork = Button(My_Window, text="Current Work", font=("Arial", 13), bg="white", activebackground="white",
                                foreground="#242424", activeforeground="#242424", height=1, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: CurrentWorkPage())
        button_currentwork.place(x=40, y=312)


        # previous work
        button_previouswork = Button(My_Window, text="Previous Work", font=("Arial", 13), bg="white", activebackground="white",
                                foreground="#242424", activeforeground="#242424", height=1, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: PreviousWorkPage())
        button_previouswork.place(x=40, y=372)

        # other information
        button_otherinfo = Button(My_Window, text="Other Information", font=("Arial", 13), bg="yellow", activebackground="yellow",
                                foreground="#242424", activeforeground="#242424", height=1, width=19, borderwidth=0, bd=0, relief=FLAT,
                                command=lambda: OtherInfoPage())
        button_otherinfo.place(x=40, y=432)


        # ----- SUBMIT BUTTON ----- #
        submit_button = Button(My_Window, text="Submit", font=("Arial", 11, 'bold'), bg="yellow", activebackground="yellow",
                                foreground="#242424", activeforeground="#242424", height=1, width=9, borderwidth=0, bd=0, relief=FLAT)
        submit_button.place(x=1040, y=595)

        My_Window.mainloop()


LoginPage()
