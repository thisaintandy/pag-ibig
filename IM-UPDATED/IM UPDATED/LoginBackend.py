import tkinter as tk
import mysql.connector
from tkinter import *
from PIL import Image, ImageTk
import random
from datetime import datetime
import customtkinter as ctk
from tkinter import ttk
from tkinter import Text, Entry, Button, Label
from tkinter import messagebox

cnx = mysql.connector.connect(
    host='localhost',
    user='andy',
    password='Andydy212003*',
    database='project_database'
)
cursor = cnx.cursor()

My_Window = Tk()
My_Window.geometry("1200x675+365+130")
My_Window.resizable(width=False, height=False)
My_Window.title("Pag-IBIG Fund")

def LoginPage():
    global MIDCode_textbox, password_textbox
    # put background picture
    file_bg_login = tk.PhotoImage(file="login1.png")
    bg_login = tk.Label(My_Window, image=file_bg_login)
    bg_login.place(x=-2, y=0)
    # logo



    # put textbox for MIDCode
    MIDCode_textbox = tk.Text(My_Window, height=1, width=25,highlightbackground="#CDFFD8", highlightthickness=1)
    MIDCode_textbox.configure(font=("Comic Sans MS", 15))
    MIDCode_textbox.configure(borderwidth=0, relief="ridge", bg='LightSteelBlue1')
    MIDCode_textbox.place(x=80, y=280)

    # put textbox for password
    password_textbox = Entry(My_Window, show='*')
    password_textbox.configure(font=("Comic Sans MS", 15), width=25,highlightbackground="#CDFFD8", highlightthickness=1)
    password_textbox.configure(borderwidth=0, relief="ridge", bg='LightSteelBlue1')
    password_textbox.place(x=80, y=370)

    # Back to Home
    back_button = Button(My_Window, text="Back To Home", font=("Arial", 13, 'bold'), width=30, relief=tk.FLAT,
                         bg="#BCE0B6",
                         command=HomePage)
    back_button.place(x=80, y=570)

    button = Button(My_Window, text="LOG IN", font=("Zing Rust Base", 13, 'bold'), relief="flat", height=1, width=15,
                    bg="#CDFFD8",
                    activebackground="#CDFFD8", command=login_action)
    button.place(x=150, y=440)

    My_Window.mainloop()


def check_credentials(MIDCode, password):
    cnx = mysql.connector.connect(
        host='localhost',
        user='andy',
        password='Andydy212003*',
        database='project_database'
    )
    cursor = cnx.cursor()

    query = "SELECT MIDCode, password FROM admin WHERE MIDCode = %s AND password =%s"
    cursor.execute(query, (MIDCode,password))
    user = cursor.fetchone()

    if user:
        login, stored_password = user
        if stored_password == password:
            return login

    return None

def remove_invalid(frame):
    global invalid

    # Remove the red border (invalid image) after 3 seconds
    if invalid is not None:
        frame.destroy()
        invalid = None
def login_action():
    global invalid,bg_frame  # Need to use the global variable here as well

    MIDCode = MIDCode_textbox.get("1.0", tk.END).strip()
    password = password_textbox.get().strip()
    login = check_credentials(MIDCode, password)


    if login:
        print("Login successful. User ID:", login)
        Easy()
    else:
        invalid = tk.PhotoImage(file="invalid.png")
        bg_frame = tk.Label(My_Window, image=invalid)
        bg_frame = Label(My_Window, image=invalid, bg="red", bd=2, highlightbackground="red")
        bg_frame.place(x=120, y=500)
        My_Window.after(3000, remove_invalid, bg_frame)

def HomePage():
    # ----- ADD BACKGROUND PICTURE ----- #
    file_bg_window = PhotoImage(file="bghomepage.png", master=My_Window)
    bg_window = Label(My_Window, image=file_bg_window, borderwidth=0)
    bg_window.place(x=0, y=0)

    # ----- add register button
    text_register = Label(My_Window, text="Want to be a Pag-IBIG member?  | ", font=("Arial", 9), bg="#E4E7E8",
                          foreground="black")
    text_register.place(x=860, y=20)
    button_register = Button(My_Window, text="Register Here", font=("Arial", 9), bg="yellow", activebackground="blue",
                             foreground="#242424", activeforeground="white", height=1, width=13, borderwidth=0, bd=0,
                             relief=FLAT, command=Register1)
    button_register.place(x=1070, y=19)

    # ----- ADD NAVIGATION BUTTONS ----- #
    # home button
    button_home = Button(My_Window, text="Home", font=("Arial", 12, 'bold'), bg="#E4E7E8", activebackground="#E4E7E8",
                         foreground="blue", activeforeground="blue", height=1, width=5, borderwidth=0, bd=0,
                         relief=FLAT)
    button_home.place(x=95, y=15)

    # about us button
    button_about = Button(My_Window, text="About Us", font=("Arial", 12, 'bold'), bg="#E4E7E8",
                          activebackground="#E4E7E8",
                          foreground="#242424", activeforeground="blue", height=1, width=8, borderwidth=0, bd=0,
                          relief=FLAT,
                          command=lambda: AboutPage())
    button_about.place(x=170, y=15)

    # log in button
    button_about = Button(My_Window, text="Log In", font=("Arial", 12, 'bold'), bg="#E4E7E8",
                          activebackground="#E4E7E8",
                          foreground="#242424", activeforeground="blue", height=1, width=8, borderwidth=0, bd=0,
                          relief=FLAT,
                          command=lambda: LoginPage())
    button_about.place(x=260, y=15)

    sqlbutton = Button(My_Window, text="?", font=("Arial", 10, 'bold'), bg="yellow",
                          activebackground="yellow",
                          foreground="#242424", activeforeground="blue", height=0, width=1, borderwidth=0, bd=0,
                          relief=FLAT,
                          command=lambda: Easy())
    sqlbutton.place(x=1165, y=635)
    My_Window.mainloop()
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
                                 command=lambda: Register1())
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
                                 command=lambda: Register1())
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
                                 command=lambda: Register1())
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


#--------------------Register Page----------------#
def generate_random_numbers(length):
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(length))
    return random_numbers


def display_output():
    random_numbers = generate_random_numbers(10)  # Generate random numbers
    MIDCode_textbox.delete('1.0', tk.END)  # Clear previous content
    MIDCode_textbox.insert('1.0', random_numbers)  # Insert new numbers


def Register1():
    global My_Window, MIDCode_textbox, password_textbox
    # put background picture
    file_bg_login = tk.PhotoImage(file="login.png")
    bg_login = tk.Label(My_Window, image=file_bg_login)
    bg_login.place(x=-2, y=0)

    random_numbers = generate_random_numbers(10)  # Generate random numbers


    # put textbox for MIDCode
    MIDCode_textbox = tk.Text(My_Window,height=1, width=10, highlightbackground="#97DBF1", highlightthickness=1)
    MIDCode_textbox.configure(font=("Comic Sans MS", 15))
    MIDCode_textbox.configure(borderwidth=0, relief="ridge", bd= 0, bg='#97DBF1')
    MIDCode_textbox.place(x=540, y=380)



    display_button = tk.Button(My_Window, text="Generate", command=display_output)
    display_button.configure(font=("Zing Rust Base", 13, 'bold'), width=8, highlightbackground="#004AAD",fg= "white",activeforeground= "yellow",
                             highlightthickness=1, activebackground="#004AAD")
    display_button.configure(borderwidth=0, relief="ridge", bg='#004AAD')
    display_button.place(x=473, y=460)

    # put textbox for password

    def save_login():
        MIDCode = MIDCode_textbox.get('1.0', tk.END).strip()

        query = "INSERT INTO login (MIDCode) VALUES (%s)"
        cursor.execute(query, (MIDCode,))
        cnx.commit()
        RegisterPage()

    button = Button(My_Window, text="Next", font=("Zing Rust Base", 13, 'bold'), relief="flat", height=1, width=5,
                    bg="#004AAD",bd=0,borderwidth=0, foreground= "white",
                    activebackground="#004AAD",activeforeground="yellow", command=save_login)
    button.place(x=655, y=460)

    My_Window.mainloop()


def RegisterPage():
    global My_Window, MIDCode_textbox, name_textbox, bdate_textbox, bplace_textbox, address_textbox, sex, spouse_textbox
    global status_textbox, citizenship_textbox, father_textbox, mother_textbox, sss_textbox, tin_textbox, email_textbox
    global phone_textbox, heirname_textbox, heirbday_textbox

    # change bg picture
    file_bg_window = ImageTk.PhotoImage(file="bgreg1.png")
    bg_window = Label(My_Window, image=file_bg_window, borderwidth=0)
    bg_window.place(x=0, y=0)

    # ------ pages button ------#
    personaldetails = Label(My_Window, text="Personal Details", font=("Arial", 13), bg="yellow", fg="black",
                            cursor="hand2")
    personaldetails.place(x=50, y=195)


    workdetails = Label(My_Window, text="Work Details", font=("Arial", 13), bg="white", fg="black",
                        cursor="hand2")
    workdetails.place(x=50, y=255)


    employer = Label(My_Window, text="Employer Details", font=("Arial", 13), bg="white", fg="black",
                     cursor="hand2")
    employer.place(x=50, y=315)


    payment = Label(My_Window, text="Payment Details", font=("Arial", 13), bg="white", fg="black",
                    cursor="hand2")
    payment.place(x=50, y=375)


    Home = Label(My_Window, text="Back to Home Page", font=("Arial", 13), bg="white", fg="black",
                 cursor="hand2")
    Home.place(x=50, y=435)
    Home.bind("<Button-1>", lambda event: HomePage())
    # ----- inputs ----- #

    # text box for name
    name_textbox = Text(My_Window, height=1, width=27)
    name_textbox.configure(font=("Arial", 15))
    name_textbox.place(x=338, y=150)

    # text box for bdate
    bdate_textbox = Text(My_Window, height=1, width=19)
    bdate_textbox.configure(font=("Arial", 15))
    bdate_textbox.place(x=665, y=150)

    # textbox for bplace
    bplace_textbox = Text(My_Window, height=1, width=17)
    bplace_textbox.configure(font=("Arial", 15))
    bplace_textbox.place(x=908, y=150)

    # textbox for address
    address_textbox = Text(My_Window, height=1, width=50)
    address_textbox.configure(font=("Arial", 15))
    address_textbox.place(x=338, y=235)

    # radiobuttons for sex
    sex = tk.StringVar()
    male_button = ctk.CTkRadioButton(My_Window, text="Male ", font=("Arial", 15, 'bold'), text_color="white",
                                          bg_color="#060606",
                                          fg_color="yellow", height=1, width=8, variable=sex,
                                          value='Male')
    male_button.place(x=910, y=320)
    female_button = ctk.CTkRadioButton(My_Window, text="Female ", font=("Arial", 15, 'bold'), text_color="white",
                                          bg_color="#060606",
                                          fg_color="yellow", height=1, width=5, variable=sex,
                                          value='Female')
    female_button.place(x=1000, y=320)

    # textbox for spouse
    spouse_textbox = Text(My_Window, height=1, width=27)
    spouse_textbox.configure(font=("Arial", 15))
    spouse_textbox.place(x=338, y=320)

    # textbox for status
    status_textbox = Text(My_Window, height=1, width=19)
    status_textbox.configure(font=("Arial", 15))
    status_textbox.place(x=665, y=320)

    # textbox for citizenship
    citizenship_textbox = Text(My_Window, height=1, width=17)
    citizenship_textbox.configure(font=("Arial", 15))
    citizenship_textbox.place(x=908, y=400)

    # textbox for father's name
    father_textbox = Text(My_Window, height=1, width=22)
    father_textbox.configure(font=("Arial", 15))
    father_textbox.place(x=338, y=400)

    # textbox for mother's
    mother_textbox = Text(My_Window, height=1, width=22)
    mother_textbox.configure(font=("Arial", 15))
    mother_textbox.place(x=620, y=400)

    # textbox for SSS
    sss_textbox = Text(My_Window, height=1, width=10)
    sss_textbox.configure(font=("Arial", 15))
    sss_textbox.place(x=338, y=483)

    # textbox for TIN
    tin_textbox = Text(My_Window, height=1, width=15)
    tin_textbox.configure(font=("Arial", 15))
    tin_textbox.place(x=475, y=483)

    # textbox for email address
    email_textbox = Text(My_Window, height=1, width=20)
    email_textbox.configure(font=("Arial", 15))
    email_textbox.place(x=665, y=483)

    # textbox for phone
    phone_textbox = Text(My_Window, height=1, width=15)
    phone_textbox.configure(font=("Arial", 15))
    phone_textbox.place(x=910, y=483)

    # textbox for heirname
    heirname_textbox = Text(My_Window, height=1, width=15)
    heirname_textbox.configure(font=("Arial", 15))
    heirname_textbox.place(x=338, y=570)

    # textbox for heir birthday
    heirbday_textbox = Text(My_Window, height=1, width=15)
    heirbday_textbox.configure(font=("Arial", 15))
    heirbday_textbox.place(x=665, y=570)

    def save_details():
        # Retrieve the values from the textboxes
        birthdate = bdate_textbox.get("1.0", "end-1c")
        heirbday = heirbday_textbox.get("1.0", "end-1c")

        # Check if all required fields are filled in
        if not (MIDCode_textbox.get("1.0", "end-1c").strip() and
                name_textbox.get("1.0", "end-1c").strip() and
                birthdate.strip() and
                bplace_textbox.get("1.0", "end-1c").strip() and
                address_textbox.get("1.0", "end-1c").strip() and
                sex.get() and
                status_textbox.get("1.0", "end-1c").strip() and
                citizenship_textbox.get("1.0", "end-1c").strip() and
                father_textbox.get("1.0", "end-1c").strip() and
                mother_textbox.get("1.0", "end-1c").strip() and
                email_textbox.get("1.0", "end-1c").strip() and
                phone_textbox.get("1.0", "end-1c").strip() and
                heirname_textbox.get("1.0", "end-1c").strip() and
                heirbday.strip() and
                sss_textbox.get("1.0", "end-1c").strip() and
                tin_textbox.get("1.0", "end-1c").strip()):

            messagebox.showerror("Error", "Please fill in all required fields.")
        else:
            query = "INSERT INTO memberdetails (MIDNumber, Name, Birthdate, Birthplace, HomeAddress, Sex, Spouse, Status, Citizenship, Father, Mother, SSS, TIN, EmailAddress, PhoneNumber, HeirsName, HeirsBirthdate) VALUES (%s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s)"
            values = (MIDCode_textbox.get("1.0", "end-1c"),
                      name_textbox.get("1.0", "end-1c"),
                      birthdate,
                      bplace_textbox.get("1.0", "end-1c"),
                      address_textbox.get("1.0", "end-1c"),
                      sex.get(),
                      spouse_textbox.get("1.0", "end-1c"),
                      status_textbox.get("1.0", "end-1c"),
                      citizenship_textbox.get("1.0", "end-1c"),
                      father_textbox.get("1.0", "end-1c"),
                      mother_textbox.get("1.0", "end-1c"),
                      sss_textbox.get("1.0", "end-1c"),
                      tin_textbox.get("1.0", "end-1c"),
                      email_textbox.get("1.0", "end-1c"),
                      phone_textbox.get("1.0", "end-1c"),
                      heirname_textbox.get("1.0", "end-1c"),
                      heirbday)

            cursor.execute(query, values)
            cnx.commit()
            RegisterPage2()

    save_button = Button(My_Window, text="Next", command=save_details)
    save_button.place(x=1100, y=600)

    My_Window.mainloop()

def RegisterPage2():
    global My_Window, emplno_textbox, occ_textbox, empstat_textbox, dateemp_textbox, income_textbox, empid_textbox

    # change bg picture
    file_bg_window = ImageTk.PhotoImage(file="bgreg2.png")
    bg_window = Label(My_Window, image=file_bg_window, borderwidth=0)
    bg_window.place(x=0, y=0)

    # ------ pages button ------#
    personaldetails = Label(My_Window, text="Personal Details", font=("Arial", 13), bg="#EFEFEF", fg="black",
                            cursor="hand2")
    personaldetails.place(x=50, y=195)


    workdetails = Label(My_Window, text="Work Details", font=("Arial", 13), bg="yellow", fg="black",
                        cursor="hand2")
    workdetails.place(x=50, y=255)


    employer = Label(My_Window, text="Employer Details", font=("Arial", 13), bg="#EFEFEF", fg="black",
                     cursor="hand2")
    employer.place(x=50, y=315)


    payment = Label(My_Window, text="Payment Details", font=("Arial", 13), bg="#EFEFEF", fg="black",
                    cursor="hand2")
    payment.place(x=50, y=375)


    Home = Label(My_Window, text="Back to Home Page", font=("Arial", 13), bg="#EFEFEF", fg="black",
                 cursor="hand2")
    Home.place(x=50, y=435)
    Home.bind("<Button-1>", lambda event: HomePage())
    # ----- inputs ----- #

    # text box for Employer ID
    emplno_textbox = Text(My_Window, height=1, width=27)
    emplno_textbox.configure(font=("Arial", 15))
    emplno_textbox.place(x=338, y=150)

    # text box for Employer Name
    occ_textbox = Text(My_Window, height=1, width=27)
    occ_textbox.configure(font=("Arial", 15))
    occ_textbox.place(x=338, y=235)

    # text box for EmployerAddress
    empstat_textbox = Text(My_Window, height=1, width=27)
    empstat_textbox.configure(font=("Arial", 15))
    empstat_textbox.place(x=338, y=320)

    # text box for EmployerAddress
    dateemp_textbox = Text(My_Window, height=1, width=27)
    dateemp_textbox.configure(font=("Arial", 15))
    dateemp_textbox.place(x=665, y=320)

    # text box for EmployerAddress
    income_textbox = Text(My_Window, height=1, width=27)
    income_textbox.configure(font=("Arial", 15))
    income_textbox.place(x=338, y=405)

    # text box for EmployerID
    empid_textbox = Text(My_Window, height=1, width=27)
    empid_textbox.configure(font=("Arial", 15))
    empid_textbox.place(x=665, y=405)


    def save_details():
        query = "INSERT INTO workdetails(EmployeeNumber,Occupation,EmploymentStatus,DateEmployed,MonthlyIncome, EmployerID) VALUES (%s,%s,%s,%s,%s,%s)"
        values = (emplno_textbox.get("1.0", "end-1c"),
                  occ_textbox.get("1.0", "end-1c"),
                  empstat_textbox.get("1.0", "end-1c"),
                  dateemp_textbox.get("1.0", "end-1c"),
                  income_textbox.get("1.0", "end-1c"),
                  empid_textbox.get("1.0", "end-1c")
                  )
        cursor.execute(query, values)
        cnx.commit()


        RegisterPage3(empid_textbox.get("1.0", "end-1c"))


    save_button = Button(My_Window, text="Next", command=save_details)
    save_button.place(x=1100, y=600)

    My_Window.mainloop()




def RegisterPage3(emp_id):
    global My_Window, empid_textbox, emp_textbox, empad_textbox

    # change bg picture
    file_bg_window = ImageTk.PhotoImage(file="bgreg3.png")
    bg_window = Label(My_Window, image=file_bg_window, borderwidth=0)
    bg_window.place(x=0, y=0)

    # ------ pages button ------#
    personaldetails = Label(My_Window, text="Personal Details", font=("Arial", 13), bg="#EFEFEF", fg="black",
                            cursor="hand2")
    personaldetails.place(x=50, y=195)


    workdetails = Label(My_Window, text="Work Details", font=("Arial", 13), bg="#EFEFEF", fg="black",
                        cursor="hand2")
    workdetails.place(x=50, y=255)


    employer = Label(My_Window, text="Employer Details", font=("Arial", 13), bg="yellow", fg="black",
                     cursor="hand2")
    employer.place(x=50, y=315)


    payment = Label(My_Window, text="Payment Details", font=("Arial", 13), bg="#EFEFEF", fg="black",
                    cursor="hand2")
    payment.place(x=50, y=375)


    Home = Label(My_Window, text="Back to Home Page", font=("Arial", 13), bg="#EFEFEF", fg="black",
                 cursor="hand2")
    Home.place(x=50, y=435)
    Home.bind("<Button-1>", lambda event: HomePage())
    # ----- inputs ----- #
    # Set the value of emp_id to the empid_textbox
    empid_textbox = Text(My_Window, height=1, width=27)
    empid_textbox.configure(font=("Arial", 15))
    empid_textbox.place(x=338, y=150)
    empid_textbox.insert(tk.END, emp_id)

    # text box for Employer Name
    emp_textbox = Text(My_Window, height=1, width=27)
    emp_textbox.configure(font=("Arial", 15))
    emp_textbox.place(x=338, y=235)

    # text box for EmployerAddress
    empad_textbox = Text(My_Window, height=1, width=27)
    empad_textbox.configure(font=("Arial", 15))
    empad_textbox.place(x=338, y=320)

    def save_details():
        query = "INSERT INTO employer (EmployerID, Employer,EmployerAddress) VALUES (%s,%s,%s)"
        values = (empid_textbox.get("1.0", "end-1c"),
                  emp_textbox.get("1.0", "end-1c"),
                  empad_textbox.get("1.0", "end-1c"),
                  )

        cursor.execute(query, values)
        cnx.commit()
        RegisterPage4()

    save_button = Button(My_Window, text="Next", command=save_details)
    save_button.place(x=1100, y=600)

    My_Window.mainloop()


def RegisterPage4():
    global My_Window, empno_textbox, membershipcat, membershippay

    # change bg picture
    file_bg_window = ImageTk.PhotoImage(file="bgreg4.png")
    bg_window = Label(My_Window, image=file_bg_window, borderwidth=0)
    bg_window.place(x=0, y=0)

    # ------ pages button ------#
    personaldetails = Label(My_Window, text="Personal Details", font=("Arial", 13), bg="#EFEFEF", fg="black",
                            cursor="hand2")
    personaldetails.place(x=50, y=195)


    workdetails = Label(My_Window, text="Work Details", font=("Arial", 13), bg="#EFEFEF", fg="black",
                        cursor="hand2")
    workdetails.place(x=50, y=255)


    employer = Label(My_Window, text="Employer Details", font=("Arial", 13), bg="#EFEFEF", fg="black",
                     cursor="hand2")
    employer.place(x=50, y=315)


    payment = Label(My_Window, text="Payment Details", font=("Arial", 13), bg="#FEFC02", fg="black",
                    cursor="hand2")
    payment.place(x=50, y=375)


    Home = Label(My_Window, text="Back to Home Page", font=("Arial", 13), bg="#EFEFEF", fg="black",
                 cursor="hand2")
    Home.place(x=50, y=435)
    Home.bind("<Button-1>", lambda event: HomePage())
    # ----- inputs ----- #

    # radiobuttons for Membership Category
    membershipcat = tk.StringVar()
    Mandatory_button = ctk.CTkRadioButton(My_Window, text="Mandatory ", font=("Arial", 15, 'bold'), text_color="white",
                                          bg_color="#060606",
                                          fg_color="yellow", height=1, width=8, variable=membershipcat,
                                          value='Mandatory')
    Mandatory_button.place(x=338, y=160)
    Voluntary_button = ctk.CTkRadioButton(My_Window, text="Voluntary ", font=("Arial", 15, 'bold'), text_color="white",
                                          bg_color="#060606",
                                          fg_color="yellow", height=1, width=5, variable=membershipcat,
                                          value='Voluntary')
    Voluntary_button.place(x=513, y=160)

    # radiobuttons for MS Payment
    membershippay = tk.StringVar()
    Monthly_button = ctk.CTkRadioButton(My_Window, text="Monthly ", font=("Arial", 15, 'bold'), text_color="white",
                                        bg_color="#060606",
                                        fg_color="yellow", height=1, width=8, variable=membershippay,
                                        value='Monthly')
    Monthly_button.place(x=340, y=250)
    Yearly_button = ctk.CTkRadioButton(My_Window, text="Yearly ", font=("Arial", 15, 'bold'), text_color="white",
                                       bg_color="#060606",
                                       fg_color="yellow", height=1, width=5, variable=membershippay,
                                       value='Yearly')
    Yearly_button.place(x=513, y=250)

    def save_details():
        def Afterlogin():
            # put background picture
            file_bg_login = tk.PhotoImage(file="afterlogin.png")
            bg_login = tk.Label(My_Window, image=file_bg_login)
            bg_login.place(x=-2, y=0)

            # log in button
            button_about = Button(My_Window, text="Back to Home", font=("Arial", 12, 'bold'), bg="#E4E7E8",
                                  activebackground="#E4E7E8",
                                  foreground="#242424", activeforeground="blue", height=1, width=8, borderwidth=0, bd=0,
                                  command=lambda: HomePage())
            button_about.place(x=260, y=15)

        query = "INSERT INTO payment (MIDNumber, EmployeeNumber, MembershipCategory, MSPayment) VALUES (%s, %s, %s, %s)"
        values = (MIDCode_textbox.get("1.0", "end-1c"),
                  emplno_textbox.get("1.0", "end-1c"), membershipcat.get(), membershippay.get())
        cursor.execute(query, values)
        cnx.commit()
        afterlogin()  # HomePage

    save_button = Button(My_Window, text="Save", command=save_details)
    save_button.place(x=1100, y=600)

    My_Window.mainloop()

def generate_random_numbers(length):
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(length))
    return random_numbers


def display_output():
    random_numbers = generate_random_numbers(10)  # Generate random numbers
    MIDCode_textbox.delete('1.0', tk.END)  # Clear previous content
    MIDCode_textbox.insert('1.0', random_numbers)  # Insert new numbers

def afterlogin():
    # put background picture
    file_bg_login = tk.PhotoImage(file="afterlogin.png")
    bg_login = tk.Label(My_Window, image=file_bg_login)
    bg_login.place(x=-2, y=0)


    # log in button
    button_about = Button(My_Window, text="Go Back", font=("Arial", 12, 'bold'), bg="#00BF63",
                          activebackground="#00BF63",
                          foreground="#242424", activeforeground="blue", height=1, width=8, borderwidth=0, bd=0,
                          command=lambda: HomePage())
    button_about.place(x=65, y=625)
    My_Window.mainloop()

def Easy():
    # put background picture
    file_bg_login = tk.PhotoImage(file="Easy.png")
    bg_login = tk.Label(My_Window, image=file_bg_login)
    bg_login.place(x=-2, y=0)

    easybutton = Button(My_Window, text="EASY", font=("Arial", 12, 'bold'), bg="yellow",
                        activebackground="yellow",
                        foreground="#242424", activeforeground="blue", height=0, width=5, borderwidth=0, bd=0,
                        relief=FLAT,
                        command=lambda: Easy())
    easybutton.place(x=190, y=120)

    mediumbutton = Button(My_Window, text="MODERATE", font=("Arial", 12, 'bold'), bg="#E4E7E8",
                          activebackground="#E4E7E8",
                          foreground="#242424", activeforeground="blue", height=0, width=10, borderwidth=0, bd=0,
                          relief=FLAT,
                          command=lambda: Moderate())
    mediumbutton.place(x=556, y=120)

    hardbutton = Button(My_Window, text="HARD", font=("Arial", 12, 'bold'), bg="#E4E7E8",
                        activebackground="#E4E7E8",
                        foreground="#242424", activeforeground="blue", height=0, width=10, borderwidth=0, bd=0,
                        relief=FLAT,
                        command=lambda: Hard())
    hardbutton.place(x=960, y=120)

    # logo
    image = Image.open('logo.png')
    img = image.resize((50, 50))
    my_img = ImageTk.PhotoImage(img)
    label = Button(My_Window, image=my_img, bg="#0F102B", activebackground="#0F102B", relief="flat",
                       command=HomePage)
    label.pack()
    label.place(x=30, y=30)

    number1 = Button(My_Window, text="SHOW", font=("Arial", 12, 'bold'), bg="#00BF63",
                   activebackground="#00BF63",
                   foreground="#242424", activeforeground="blue", height=0, width=5, borderwidth=0, bd=0,
                   relief=FLAT,
                   command=lambda: easybuttons(1))
    number1.place(x=1045, y=227)

    number2 = Button(My_Window, text="SHOW", font=("Arial", 12, 'bold'), bg="#00BF63",
                     activebackground="#00BF63",
                     foreground="#242424", activeforeground="blue", height=0, width=5, borderwidth=0, bd=0,
                     relief=FLAT,
                     command=lambda: easybuttons(2))
    number2.place(x=1045, y=312)

    number3 = Button(My_Window, text="SHOW", font=("Arial", 12, 'bold'), bg="#00BF63",
                     activebackground="#00BF63",
                     foreground="#242424", activeforeground="blue", height=0, width=5, borderwidth=0, bd=0,
                     relief=FLAT,
                     command=lambda: easybuttons(3))
    number3.place(x=1045, y=397)

    number4 = Button(My_Window, text="SHOW", font=("Arial", 12, 'bold'), bg="#00BF63",
                     activebackground="#00BF63",
                     foreground="#242424", activeforeground="blue", height=0, width=5, borderwidth=0, bd=0,
                     relief=FLAT,
                     command=lambda: easybuttons(4))
    number4.place(x=1045, y=482)

    number5 = Button(My_Window, text="SHOW", font=("Arial", 12, 'bold'), bg="#00BF63",
                     activebackground="#00BF63",
                     foreground="#242424", activeforeground="blue", height=0, width=5, borderwidth=0, bd=0,
                     relief=FLAT,
                     command=lambda: easybuttons(5))
    number5.place(x=1045, y=567)

    def easybuttons(buttons):
        # Retrieve data from the first table
        root = Tk()

        # Create a Treeview widget for the first table
        tree1 = ttk.Treeview(root)
        tree1.pack(fill=BOTH, expand=True)

        cursor1 = cnx.cursor()
        cursor1.execute("SELECT * FROM memberdetails")  # Replace with your first table name
        rows1 = cursor1.fetchall()

        # Retrieve data from the second table
        cursor2 = cnx.cursor()
        cursor2.execute("SELECT * FROM workdetails")  # Replace with your second table name
        rows2 = cursor2.fetchall()

        # Retrieve data from the third table
        cursor3 = cnx.cursor()
        cursor3.execute("SELECT * FROM employer")  # Replace with your third table name
        rows3 = cursor3.fetchall()

        # Retrieve data from the fourth table
        cursor4 = cnx.cursor()
        cursor4.execute("SELECT * FROM payment")  # Replace with your fourth table name
        rows4 = cursor4.fetchall()

        if buttons == 1:
            # Define the column names for the first table
            column_names1 = ["MIDNumber", "Name", "Sex", "Father", "Mother", "Spouse", "Birthdate", "Birthplace",
                             "Status",
                             "Citizenship", "SSS", "TIN", "HomeAddress", "EmailAddress", "PhoneNumber", "HeirsName",
                             "HeirsBirthdate"]

            # Determine the number of columns for the first table
            num_columns1 = len(column_names1)

            # Set the columns for the first table in the Treeview widget
            tree1["columns"] = tuple(f"column{i + 1}" for i in range(num_columns1))
            tree1.heading("#0", text=column_names1[0])
            for i, column_name in enumerate(column_names1[1:]):
                tree1.heading(f"column{i + 1}", text=column_name)
                tree1.column("#0", width=90, minwidth=85)
                # Adjust the column width based on the content
                tree1.column(f"column{i + 1}", width=82, minwidth=80, stretch=True)
                tree1.heading(f"column{i + 1}", text=column_name, anchor=CENTER)

            # Insert data from the first table into the Treeview widget
            for row in rows1:
                tree1.insert("", "end", text=row[0], values=row[1:num_columns1 + 1])
            # Create a Treeview widget for the first table
            tree2 = ttk.Treeview(root)
            tree2.pack(fill=BOTH, expand=True)
            # Define the column names for the first table
            column_names2 = ["EmployeeNumber", "Occupation", "EmploymentStatus", "DateEmployed", "MonthlyIncome",
                                 "EmployerID"]

            # Determine the number of columns for the first table
            num_columns2 = len(column_names2)

            # Set the columns for the first table in the Treeview widget
            tree2["columns"] = tuple(f"column{i + 1}" for i in range(num_columns2))
            tree2.heading("#0", text=column_names2[0])
            for i, column_name in enumerate(column_names2[1:]):
                tree2.heading(f"column{i + 1}", text=column_name)
                tree2.column("#0", width=90, minwidth=85)
                # Adjust the column width based on the content
                tree2.column(f"column{i + 1}", width=82, minwidth=80, stretch=True)
                tree2.heading(f"column{i + 1}", text=column_name, anchor=CENTER)

            # Insert data from the first table into the Treeview widget
            for row in rows2:
                tree2.insert("", "end", text=row[0], values=row[1:num_columns2 + 1])

            # Create a Treeview widget for the first table
            tree3 = ttk.Treeview(root)
            tree3.pack(fill=BOTH, expand=True)

            # Define the column names for the first table
            column_names3 = ["EmployerID", "Employer", "EmployerAddress"]

            # Determine the number of columns for the first table
            num_columns3 = len(column_names3)

            # Set the columns for the first table in the Treeview widget
            tree3["columns"] = tuple(f"column{i + 1}" for i in range(num_columns3))
            tree3.heading("#0", text=column_names3[0])
            for i, column_name in enumerate(column_names3[1:]):
                tree3.heading(f"column{i + 1}", text=column_name)
                tree3.column("#0", width=90, minwidth=85)
                # Adjust the column width based on the content
                tree3.column(f"column{i + 1}", width=82, minwidth=80, stretch=True)
                tree3.heading(f"column{i + 1}", text=column_name, anchor=CENTER)

            # Insert data from the first table into the Treeview widget
            for row in rows3:
                tree3.insert("", "end", text=row[0], values=row[1:num_columns3 + 1])

            # Create a Treeview widget for the first table
            tree4 = ttk.Treeview(root)
            tree4.pack(fill=BOTH, expand=True)

            # Define the column names for the first table
            column_names4 = ["MIDNumber","Employee Number","Membership Category","MS Payment"]

            # Determine the number of columns for the first table
            num_columns4 = len(column_names4)
        
            # Set the columns for the first table in the Treeview widget
            tree4["columns"] = tuple(f"column{i + 1}" for i in range(num_columns4))
            tree4.heading("#0", text=column_names4[0])
            for i, column_name in enumerate(column_names4[1:]):
                tree4.heading(f"column{i + 1}", text=column_name)
                tree4.column("#0", width=90, minwidth=85)
                # Adjust the column width based on the content
                tree4.column(f"column{i + 1}", width=82, minwidth=80, stretch=True)
                tree4.heading(f"column{i + 1}", text=column_name, anchor=CENTER)

            # Insert data from the first table into the Treeview widget
            for row in rows4:
                tree4.insert("", "end", text=row[0], values=row[1:num_columns4 + 1])

            root.geometry("1420x800+250+130")

        elif buttons == 2:
            cursor = cnx.cursor()
            cursor.execute("SELECT Name, Status FROM memberdetails WHERE Status <> 'Single'") # Replace "your_table" with the actual table name
            column_names = [column[0] for column in cursor.description]
            rows = cursor.fetchall()

            # Determine the number of columns
            num_columns = len(column_names)

            # Set the columns in the Treeview widget
            tree1["columns"] = tuple(f"column{i + 1}" for i in range(num_columns))
            tree1.heading("#0", text=column_names[0])
            for i, column_name in enumerate(column_names[1:]):
                tree1.heading(f"column{i + 1}", text=column_name)
                tree1.column("#0", width=90, minwidth=85)
                # Adjust the column width based on the content
                tree1.column(f"column{i + 1}", width=82, minwidth=80, stretch=True)
                tree1.heading(f"column{i + 1}", text=column_name, anchor=CENTER)

            # Insert data into the Treeview widget
            for row in rows:
                tree1.insert("", "end", text=row[0], values=row[1:num_columns + 1])
            root.geometry("500x500+250+130")


        elif buttons == 3:
            cursor = cnx.cursor()
            cursor.execute("SELECT Name, PhoneNumber FROM memberdetails WHERE PhoneNumber LIKE '0949%'")  # Replace "your_table" with the actual table name
            column_names = [column[0] for column in cursor.description]
            rows = cursor.fetchall()

            # Determine the number of columns
            num_columns = len(column_names)

            # Set the columns in the Treeview widget
            tree1["columns"] = tuple(f"column{i + 1}" for i in range(num_columns))
            tree1.heading("#0", text=column_names[0])
            for i, column_name in enumerate(column_names[1:]):
                tree1.heading(f"column{i + 1}", text=column_name)
                tree1.column("#0", width=90, minwidth=85)
                # Adjust the column width based on the content
                tree1.column(f"column{i + 1}", width=82, minwidth=80, stretch=True)
                tree1.heading(f"column{i + 1}", text=column_name, anchor=CENTER)

            # Insert data into the Treeview widget
            for row in rows:
                tree1.insert("", "end", text=row[0], values=row[1:num_columns + 1])

        elif buttons == 4:
            cursor = cnx.cursor()
            cursor.execute("SELECT MIDNumber, Name, PhoneNumber FROM memberdetails WHERE SEX ='Male'")  # Replace "your_table" with the actual table name
            column_names = [column[0] for column in cursor.description]
            rows = cursor.fetchall()

            # Determine the number of columns
            num_columns = len(column_names)

            # Set the columns in the Treeview widget
            tree1["columns"] = tuple(f"column{i + 1}" for i in range(num_columns))
            tree1.heading("#0", text=column_names[0])
            for i, column_name in enumerate(column_names[1:]):
                tree1.heading(f"column{i + 1}", text=column_name)
                tree1.column("#0", width=90, minwidth=85)
                # Adjust the column width based on the content
                tree1.column(f"column{i + 1}", width=82, minwidth=80, stretch=True)
                tree1.heading(f"column{i + 1}", text=column_name, anchor=CENTER)

            # Insert data into the Treeview widget
            for row in rows:
                tree1.insert("", "end", text=row[0], values=row[1:num_columns + 1])

        elif buttons == 5:
            cursor = cnx.cursor()
            cursor.execute("SELECT Occupation FROM workdetails")  # Replace "your_table" with the actual table name
            column_names = [column[0] for column in cursor.description]
            rows = cursor.fetchall()

            # Determine the number of columns
            num_columns = len(column_names)

            # Set the columns in the Treeview widget
            tree1["columns"] = tuple(f"column{i + 1}" for i in range(num_columns))
            tree1.heading("#0", text=column_names[0])
            for i, column_name in enumerate(column_names[1:]):
                tree1.heading(f"column{i + 1}", text=column_name)
                tree1.column("#0", width=90, minwidth=85)
                # Adjust the column width based on the content
                tree1.column(f"column{i + 1}", width=82, minwidth=80, stretch=True)
                tree1.heading(f"column{i + 1}", text=column_name, anchor=CENTER)

            # Insert data into the Treeview widget
            for row in rows:
                tree1.insert("", "end", text=row[0], values=row[1:num_columns + 1])

        # Close the database connections
        cursor1.close()
        cursor2.close()
        cursor3.close()
        cursor4.close()
    My_Window.mainloop()



def Moderate():
    # put background picture
    file_bg_login = tk.PhotoImage(file="moderate.png")
    bg_login = tk.Label(My_Window, image=file_bg_login)
    bg_login.place(x=-2, y=0)

    easybutton = Button(My_Window, text="EASY", font=("Arial", 12, 'bold'), bg="#E4E7E8",
                      activebackground="#E4E7E8",
                      foreground="#242424", activeforeground="blue", height=0, width=5, borderwidth=0, bd=0,
                      relief=FLAT,
                      command=lambda: Easy())
    easybutton.place(x=190, y=120)

    mediumbutton = Button(My_Window, text="MODERATE", font=("Arial", 12, 'bold'), bg="yellow",
                        activebackground="yellow",
                        foreground="#242424", activeforeground="blue", height=0, width=10, borderwidth=0, bd=0,
                        relief=FLAT,
                        command=lambda: Moderate())
    mediumbutton.place(x=556, y=120)

    hardbutton = Button(My_Window, text="HARD", font=("Arial", 12, 'bold'), bg="#E4E7E8",
                          activebackground="#E4E7E8",
                          foreground="#242424", activeforeground="blue", height=0, width=10, borderwidth=0, bd=0,
                          relief=FLAT,
                          command=lambda: Hard())
    hardbutton.place(x=960, y=120)

    # logo
    image = Image.open('logo.png')
    img = image.resize((50, 50))
    my_img = ImageTk.PhotoImage(img)
    label = Button(My_Window, image=my_img, bg="#0F102B", activebackground="#0F102B", relief="flat",
                       command=HomePage)
    label.pack()
    label.place(x=30, y=30)

    number1 = Button(My_Window, text="SHOW", font=("Arial", 12, 'bold'), bg="#00BF63",
                         activebackground="#00BF63",
                         foreground="#242424", activeforeground="blue", height=0, width=5, borderwidth=0, bd=0,
                         relief=FLAT,
                         command=lambda: easybuttons(1))
    number1.place(x=1045, y=227)

    number2 = Button(My_Window, text="SHOW", font=("Arial", 12, 'bold'), bg="#00BF63",
                         activebackground="#00BF63",
                         foreground="#242424", activeforeground="blue", height=0, width=5, borderwidth=0, bd=0,
                         relief=FLAT,
                         command=lambda: easybuttons(2))
    number2.place(x=1045, y=312)

    number3 = Button(My_Window, text="SHOW", font=("Arial", 12, 'bold'), bg="#00BF63",
                         activebackground="#00BF63",
                         foreground="#242424", activeforeground="blue", height=0, width=5, borderwidth=0, bd=0,
                         relief=FLAT,
                         command=lambda: easybuttons(3))
    number3.place(x=1045, y=397)

    number4 = Button(My_Window, text="SHOW", font=("Arial", 12, 'bold'), bg="#00BF63",
                         activebackground="#00BF63",
                         foreground="#242424", activeforeground="blue", height=0, width=5, borderwidth=0, bd=0,
                         relief=FLAT,
                         command=lambda: easybuttons(4))
    number4.place(x=1045, y=482)

    number5 = Button(My_Window, text="SHOW", font=("Arial", 12, 'bold'), bg="#00BF63",
                         activebackground="#00BF63",
                         foreground="#242424", activeforeground="blue", height=0, width=5, borderwidth=0, bd=0,
                         relief=FLAT,
                         command=lambda: easybuttons(5))
    number5.place(x=1045, y=567)

    def easybuttons(buttons):
        # Retrieve data from the first table
        root = Tk()

        # Create a Treeview widget for the first table
        tree1 = ttk.Treeview(root)
        tree1.pack(fill=BOTH, expand=True)

        cursor1 = cnx.cursor()
        cursor1.execute("SELECT * FROM memberdetails")  # Replace with your first table name
        rows1 = cursor1.fetchall()

        # Retrieve data from the second table
        cursor2 = cnx.cursor()
        cursor2.execute("SELECT * FROM workdetails")  # Replace with your second table name
        rows2 = cursor2.fetchall()

        # Retrieve data from the third table
        cursor3 = cnx.cursor()
        cursor3.execute("SELECT * FROM employer")  # Replace with your third table name
        rows3 = cursor3.fetchall()

        # Retrieve data from the fourth table
        cursor4 = cnx.cursor()
        cursor4.execute("SELECT * FROM payment")  # Replace with your fourth table name
        rows4 = cursor4.fetchall()

        if buttons == 1:
            cursor = cnx.cursor()
            cursor.execute(
                "SELECT Name, sex, TIMESTAMPDIFF(YEAR, Birthdate, CURDATE()) AS Age FROM memberdetails "
                "WHERE TIMESTAMPDIFF(YEAR, Birthdate, CURDATE()) >= 15 "
                "GROUP BY Name, sex, Birthdate;")  # Replace "your_table" with the actual table name
            column_names = [column[0] for column in cursor.description]
            rows = cursor.fetchall()

            # Determine the number of columns
            num_columns = len(column_names)

            # Set the columns in the Treeview widget
            tree1["columns"] = tuple(f"column{i + 1}" for i in range(num_columns))
            tree1.heading("#0", text=column_names[0])
            for i, column_name in enumerate(column_names[1:]):
                tree1.heading(f"column{i + 1}", text=column_name)
                tree1.column("#0", width=90, minwidth=85)
                # Adjust the column width based on the content
                tree1.column(f"column{i + 1}", width=82, minwidth=80, stretch=True)
                tree1.heading(f"column{i + 1}", text=column_name, anchor=CENTER)

                # Insert data into the Treeview widget
            for row in rows:
                tree1.insert("", "end", text=row[0], values=row[1:num_columns + 1])
            root.geometry("500x500+250+130")

        elif buttons == 2:
            cursor = cnx.cursor()
            cursor.execute(
                    "SELECT AVG(TIMESTAMPDIFF(YEAR, Birthdate, CURDATE())) AS AverageAge FROM memberdetails;")  # Replace "your_table" with the actual table name
            column_names = [column[0] for column in cursor.description]
            rows = cursor.fetchall()

                # Determine the number of columns
            num_columns = len(column_names)

                # Set the columns in the Treeview widget
            tree1["columns"] = tuple(f"column{i + 1}" for i in range(num_columns))
            tree1.heading("#0", text=column_names[0])
            for i, column_name in enumerate(column_names[1:]):
                tree1.heading(f"column{i + 1}", text=column_name)
                tree1.column("#0", width=90, minwidth=85)
                    # Adjust the column width based on the content
                tree1.column(f"column{i + 1}", width=82, minwidth=80, stretch=True)
                tree1.heading(f"column{i + 1}", text=column_name, anchor=CENTER)

                # Insert data into the Treeview widget
            for row in rows:
                tree1.insert("", "end", text=row[0], values=row[1:num_columns + 1])
            root.geometry("500x500+250+130")


        elif buttons == 3:
            cursor = cnx.cursor()
            cursor.execute(
                    "SELECT Name, Birthdate FROM memberdetails WHERE MONTH(Birthdate) = MONTH(CURDATE());")  # Replace "your_table" with the actual table name
            column_names = [column[0] for column in cursor.description]
            rows = cursor.fetchall()

                # Determine the number of columns
            num_columns = len(column_names)

                # Set the columns in the Treeview widget
            tree1["columns"] = tuple(f"column{i + 1}" for i in range(num_columns))
            tree1.heading("#0", text=column_names[0])
            for i, column_name in enumerate(column_names[1:]):
                tree1.heading(f"column{i + 1}", text=column_name)
                tree1.column("#0", width=90, minwidth=85)
                    # Adjust the column width based on the content
                tree1.column(f"column{i + 1}", width=82, minwidth=80, stretch=True)
                tree1.heading(f"column{i + 1}", text=column_name, anchor=CENTER)

                # Insert data into the Treeview widget
            for row in rows:
                tree1.insert("", "end", text=row[0], values=row[1:num_columns + 1])

        elif buttons == 4:
            cursor = cnx.cursor()
            cursor.execute(
                    "SELECT Name, MonthlyIncome FROM workdetails as w, memberdetails as m, payment as p, employer e "
                    "WHERE w.EmployeeNumber = p.EmployeeNumber AND m.MIDNumber = p.EmployeeNumber AND w.EmployerID = e.EmployerID "
                    "ORDER BY MonthlyIncome DESC;")  # Replace "your_table" with the actual table name
            column_names = [column[0] for column in cursor.description]
            rows = cursor.fetchall()

                # Determine the number of columns
            num_columns = len(column_names)

                # Set the columns in the Treeview widget
            tree1["columns"] = tuple(f"column{i + 1}" for i in range(num_columns))
            tree1.heading("#0", text=column_names[0])
            for i, column_name in enumerate(column_names[1:]):
                tree1.heading(f"column{i + 1}", text=column_name)
                tree1.column("#0", width=90, minwidth=85)
                    # Adjust the column width based on the content
                tree1.column(f"column{i + 1}", width=82, minwidth=80, stretch=True)
                tree1.heading(f"column{i + 1}", text=column_name, anchor=CENTER)

                # Insert data into the Treeview widget
            for row in rows:
                tree1.insert("", "end", text=row[0], values=row[1:num_columns + 1])

        elif buttons == 5:
            cursor = cnx.cursor()
            cursor.execute("SELECT COUNT(*), EmploymentStatus, MembershipCategory FROM workdetails AS w, payment as p "
                           "WHERE w.EmployeeNumber = p.EmployeeNumber "
                           "GROUP BY EmploymentStatus, MembershipCategory;")  # Replace "your_table" with the actual table name
            column_names = [column[0] for column in cursor.description]
            rows = cursor.fetchall()

                # Determine the number of columns
            num_columns = len(column_names)

                # Set the columns in the Treeview widget
            tree1["columns"] = tuple(f"column{i + 1}" for i in range(num_columns))
            tree1.heading("#0", text=column_names[0])
            for i, column_name in enumerate(column_names[1:]):
                tree1.heading(f"column{i + 1}", text=column_name)
                tree1.column("#0", width=90, minwidth=85)
                    # Adjust the column width based on the content
                tree1.column(f"column{i + 1}", width=82, minwidth=80, stretch=True)
                tree1.heading(f"column{i + 1}", text=column_name, anchor=CENTER)

                # Insert data into the Treeview widget
            for row in rows:
                tree1.insert("", "end", text=row[0], values=row[1:num_columns + 1])

            # Close the database connections
        cursor1.close()
        cursor2.close()
        cursor3.close()
        cursor4.close()
    My_Window.mainloop()
def Hard():
    # put background picture
    file_bg_login = tk.PhotoImage(file="hard.png")
    bg_login = tk.Label(My_Window, image=file_bg_login)
    bg_login.place(x=-2, y=0)

    easybutton = Button(My_Window, text="EASY", font=("Arial", 12, 'bold'), bg="#E4E7E8",
                        activebackground="#E4E7E8",
                        foreground="#242424", activeforeground="blue", height=0, width=5, borderwidth=0, bd=0,
                        relief=FLAT,
                        command=lambda: Easy())
    easybutton.place(x=190, y=120)

    mediumbutton = Button(My_Window, text="MODERATE", font=("Arial", 12, 'bold'), bg="#E4E7E8",
                          activebackground="#E4E7E8",
                          foreground="#242424", activeforeground="blue", height=0, width=10, borderwidth=0, bd=0,
                          relief=FLAT,
                          command=lambda: Moderate())
    mediumbutton.place(x=556, y=120)

    hardbutton = Button(My_Window, text="HARD", font=("Arial", 12, 'bold'), bg="yellow",
                        activebackground="yellow",
                        foreground="#242424", activeforeground="blue", height=0, width=10, borderwidth=0, bd=0,
                        relief=FLAT,
                        command=lambda: Hard())
    hardbutton.place(x=960, y=120)

    # logo
    image = Image.open('logo.png')
    img = image.resize((50, 50))
    my_img = ImageTk.PhotoImage(img)
    label = Button(My_Window, image=my_img, bg="#0F102B", activebackground="#0F102B", relief="flat",
                       command=HomePage)
    label.pack()
    label.place(x=30, y=30)

    number1 = Button(My_Window, text="SHOW", font=("Arial", 12, 'bold'), bg="#00BF63",
                         activebackground="#00BF63",
                         foreground="#242424", activeforeground="blue", height=0, width=5, borderwidth=0, bd=0,
                         relief=FLAT,
                         command=lambda: easybuttons(1))
    number1.place(x=1045, y=227)

    number2 = Button(My_Window, text="SHOW", font=("Arial", 12, 'bold'), bg="#00BF63",
                         activebackground="#00BF63",
                         foreground="#242424", activeforeground="blue", height=0, width=5, borderwidth=0, bd=0,
                         relief=FLAT,
                         command=lambda: easybuttons(2))
    number2.place(x=1045, y=312)

    number3 = Button(My_Window, text="SHOW", font=("Arial", 12, 'bold'), bg="#00BF63",
                         activebackground="#00BF63",
                         foreground="#242424", activeforeground="blue", height=0, width=5, borderwidth=0, bd=0,
                         relief=FLAT,
                         command=lambda: easybuttons(3))
    number3.place(x=1045, y=397)

    number4 = Button(My_Window, text="SHOW", font=("Arial", 12, 'bold'), bg="#00BF63",
                         activebackground="#00BF63",
                         foreground="#242424", activeforeground="blue", height=0, width=5, borderwidth=0, bd=0,
                         relief=FLAT,
                         command=lambda: easybuttons(4))
    number4.place(x=1045, y=482)

    number5 = Button(My_Window, text="SHOW", font=("Arial", 12, 'bold'), bg="#00BF63",
                         activebackground="#00BF63",
                         foreground="#242424", activeforeground="blue", height=0, width=5, borderwidth=0, bd=0,
                         relief=FLAT,
                         command=lambda: easybuttons(5))
    number5.place(x=1045, y=567)

    def easybuttons(buttons):
        # Retrieve data from the first table
        root = Tk()

        # Create a Treeview widget for the first table
        tree1 = ttk.Treeview(root)
        tree1.pack(fill=BOTH, expand=True)

        cursor1 = cnx.cursor()
        cursor1.execute("SELECT * FROM memberdetails")  # Replace with your first table name
        rows1 = cursor1.fetchall()

        # Retrieve data from the second table
        cursor2 = cnx.cursor()
        cursor2.execute("SELECT * FROM workdetails")  # Replace with your second table name
        rows2 = cursor2.fetchall()

        # Retrieve data from the third table
        cursor3 = cnx.cursor()
        cursor3.execute("SELECT * FROM employer")  # Replace with your third table name
        rows3 = cursor3.fetchall()

        # Retrieve data from the fourth table
        cursor4 = cnx.cursor()
        cursor4.execute("SELECT * FROM payment")  # Replace with your fourth table name
        rows4 = cursor4.fetchall()

        if buttons == 1:
            cursor = cnx.cursor()
            cursor.execute(
                "SELECT name, birthdate, occupation FROM memberdetails as m, workdetails as w, payment p WHERE w.EmployeeNumber = p.EmployeeNumber "
                "AND p.MIDNumber = m.MIDNumber AND year(m.birthdate) BETWEEN 2000 AND 2010 ORDER BY name;")  # Replace "your_table" with the actual table name
            column_names = [column[0] for column in cursor.description]
            rows = cursor.fetchall()

            # Determine the number of columns
            num_columns = len(column_names)

            # Set the columns in the Treeview widget
            tree1["columns"] = tuple(f"column{i + 1}" for i in range(num_columns))
            tree1.heading("#0", text=column_names[0])
            for i, column_name in enumerate(column_names[1:]):
                tree1.heading(f"column{i + 1}", text=column_name)
                tree1.column("#0", width=90, minwidth=85)
                # Adjust the column width based on the content
                tree1.column(f"column{i + 1}", width=82, minwidth=80, stretch=True)
                tree1.heading(f"column{i + 1}", text=column_name, anchor=CENTER)

                # Insert data into the Treeview widget
            for row in rows:
                tree1.insert("", "end", text=row[0], values=row[1:num_columns + 1])
            root.geometry("500x500+250+130")

        elif buttons == 2:
            cursor = cnx.cursor()
            cursor.execute(
                    "SELECT mspayment, name, month(birthdate) as m_birthmonth, heirsname, month(heirsbirthdate) as h_birthmonth "
                    "FROM memberdetails as m, payment as p "
                    "WHERE p.MIDNumber = m.MIDNumber AND (month(birthdate) = month(heirsbirthdate));")  # Replace "your_table" with the actual table name

            column_names = [column[0] for column in cursor.description]
            rows = cursor.fetchall()

                # Determine the number of columns
            num_columns = len(column_names)

                # Set the columns in the Treeview widget
            tree1["columns"] = tuple(f"column{i + 1}" for i in range(num_columns))
            tree1.heading("#0", text=column_names[0])
            for i, column_name in enumerate(column_names[1:]):
                tree1.heading(f"column{i + 1}", text=column_name)
                tree1.column("#0", width=90, minwidth=85)
                    # Adjust the column width based on the content
                tree1.column(f"column{i + 1}", width=82, minwidth=80, stretch=True)
                tree1.heading(f"column{i + 1}", text=column_name, anchor=CENTER)

                # Insert data into the Treeview widget
            for row in rows:
                tree1.insert("", "end", text=row[0], values=row[1:num_columns + 1])
            root.geometry("500x500+250+130")


        elif buttons == 3:
            cursor = cnx.cursor()
            cursor.execute(
                    "SELECT sex ,name, homeaddress, AVG(monthlyincome) as average_monthlyincome "
                    "FROM memberdetails as m, workdetails as w, payment p "
                    "WHERE w.EmployeeNumber = p.EmployeeNumber AND p.MIDNumber = m.MIDNumber AND (m.HomeAddress LIKE '%Manila%') GROUP BY sex, name, homeaddress;")  # Replace "your_table" with the actual table name
            column_names = [column[0] for column in cursor.description]
            rows = cursor.fetchall()

                # Determine the number of columns
            num_columns = len(column_names)

                # Set the columns in the Treeview widget
            tree1["columns"] = tuple(f"column{i + 1}" for i in range(num_columns))
            tree1.heading("#0", text=column_names[0])
            for i, column_name in enumerate(column_names[1:]):
                tree1.heading(f"column{i + 1}", text=column_name)
                tree1.column("#0", width=90, minwidth=85)
                    # Adjust the column width based on the content
                tree1.column(f"column{i + 1}", width=82, minwidth=80, stretch=True)
                tree1.heading(f"column{i + 1}", text=column_name, anchor=CENTER)

                # Insert data into the Treeview widget
            for row in rows:
                tree1.insert("", "end", text=row[0], values=row[1:num_columns + 1])

        elif buttons == 4:
            cursor = cnx.cursor()
            cursor.execute(
                    "SELECT membershipcategory, COUNT(*) as Count "
                    "FROM workdetails as w, payment p, memberdetails m "
                    "WHERE w.EmployeeNumber = p.EmployeeNumber AND p.MIDNumber = m.MIDNumber AND (w.monthlyincome > 15000)"
                    "GROUP BY membershipcategory;")  # Replace "your_table" with the actual table name
            column_names = [column[0] for column in cursor.description]
            rows = cursor.fetchall()

                # Determine the number of columns
            num_columns = len(column_names)

                # Set the columns in the Treeview widget
            tree1["columns"] = tuple(f"column{i + 1}" for i in range(num_columns))
            tree1.heading("#0", text=column_names[0])
            for i, column_name in enumerate(column_names[1:]):
                tree1.heading(f"column{i + 1}", text=column_name)
                tree1.column("#0", width=90, minwidth=85)
                    # Adjust the column width based on the content
                tree1.column(f"column{i + 1}", width=82, minwidth=80, stretch=True)
                tree1.heading(f"column{i + 1}", text=column_name, anchor=CENTER)

                # Insert data into the Treeview widget
            for row in rows:
                tree1.insert("", "end", text=row[0], values=row[1:num_columns + 1])

        elif buttons == 5:
            cursor = cnx.cursor()
            cursor.execute("SELECT name, occupation, employer "
                           "FROM memberdetails as m, workdetails as w, payment p, employer e "
                           "WHERE w.EmployeeNumber = p.EmployeeNumber AND m.MIDNumber = p.EmployeeNumber AND w.EmployerID = e.EmployerID AND (e.employeraddress NOT LIKE '%MANILA%');")  # Replace "your_table" with the actual table name
            column_names = [column[0] for column in cursor.description]
            rows = cursor.fetchall()

                # Determine the number of columns
            num_columns = len(column_names)

                # Set the columns in the Treeview widget
            tree1["columns"] = tuple(f"column{i + 1}" for i in range(num_columns))
            tree1.heading("#0", text=column_names[0])
            for i, column_name in enumerate(column_names[1:]):
                tree1.heading(f"column{i + 1}", text=column_name)
                tree1.column("#0", width=90, minwidth=85)
                    # Adjust the column width based on the content
                tree1.column(f"column{i + 1}", width=82, minwidth=80, stretch=True)
                tree1.heading(f"column{i + 1}", text=column_name, anchor=CENTER)

                # Insert data into the Treeview widget
            for row in rows:
                tree1.insert("", "end", text=row[0], values=row[1:num_columns + 1])

            # Close the database connections
        cursor1.close()
        cursor2.close()
        cursor3.close()
        cursor4.close()
    My_Window.mainloop()

HomePage()




