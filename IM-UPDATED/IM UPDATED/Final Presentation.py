import tkinter as tk
import mysql.connector
from tkinter import *
from PIL import Image, ImageTk
from tkinter import Entry
import random
from datetime import datetime
import customtkinter as ctk
from tkinter import ttk

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

def generate_random_numbers(length):
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(length))
    return random_numbers


def display_output():
    random_numbers = generate_random_numbers(10)  # Generate random numbers
    MIDCode_textbox.delete('1.0', tk.END)  # Clear previous content
    MIDCode_textbox.insert('1.0', random_numbers)  # Insert new numbers


def Register():
    global MIDCode_textbox, password_textbox
    # put background picture
    file_bg_login = tk.PhotoImage(file="login.png")
    bg_login = tk.Label(My_Window, image=file_bg_login)
    bg_login.place(x=0, y=0)

    # logo
    image = Image.open('logo.png')
    img = image.resize((50, 50))
    my_img = ImageTk.PhotoImage(img)
    label = Button(My_Window, image=my_img, bg="white", relief="flat")
    label.pack()
    label.place(x=800, y=180)

    MIDCode_textbox = Text(My_Window, height=1, width=25, highlightbackground="#444444", highlightthickness=1)
    MIDCode_textbox.configure(font=("Comic Sans MS", 15))
    MIDCode_textbox.configure(borderwidth=0, relief="ridge", bg='LightSteelBlue1')
    MIDCode_textbox.place(x=665, y=305)

    caption = tk.Label(My_Window, text="MIDCode", font=("Arial", 8), bg="white")
    caption.place(x=665, y=285)

    display_button = tk.Button(My_Window, text="Generate", command=display_output)
    display_button.configure(font=("Comic Sans MS", 10), width=8, highlightbackground="#444444",
                             highlightthickness=1, activebackground="LightSteelBlue2")
    display_button.configure(borderwidth=0, relief="ridge", bg='LightSteelBlue1')
    display_button.place(x=895, y=306)

    password_textbox = Entry(My_Window, show='*')
    password_textbox.configure(font=("Comic Sans MS", 15), width=25, highlightbackground="#444444",
                               highlightthickness=1)
    password_textbox.configure(borderwidth=0, relief="ridge", bg='LightSteelBlue1')
    password_textbox.place(x=665, y=370)

    caption = tk.Label(My_Window, text="Password", font=("Arial", 8), bg="white")
    caption.place(x=665, y=350)

    save_button = Button(My_Window,text="SIGN UP", font=("Arial", 13, 'bold'), relief="ridge", height=1, width=30, bg="pale green",
                    activebackground="pale green", command=RegisterPage)
    save_button.place(x=664, y=430)

    back_button = Button(My_Window, text="Back To Home", font=("Arial", 13, 'bold'), width=30, relief= FLAT,
                         bg="white")
    back_button.place(x=664, y=530)

    My_Window.mainloop()

def RegisterPage():
    # change bg picture
    file_bg_window = PhotoImage(file="bgreg1.png", master=My_Window)
    bg_window = Label(My_Window, image=file_bg_window, borderwidth=0)
    bg_window.place(x=0, y=0)

    # ------ pages button ------#
    personaldetails = Label(My_Window, text="Personal Details", font=("Arial", 13), bg="yellow", fg="black",
                            cursor="hand2")
    personaldetails.place(x=50, y=195)
    personaldetails.bind("<Button-1>", lambda event: RegisterPage())

    workdetails = Label(My_Window, text="Work Details", font=("Arial", 13), bg="white", fg="black",
                            cursor="hand2")
    workdetails.place(x=50, y=255)
    workdetails.bind("<Button-1>", lambda event: RegisterPage2())

    employer = Label(My_Window, text="Employer Details", font=("Arial", 13), bg="white", fg="black",
                        cursor="hand2")
    employer.place(x=50, y=315)
    employer.bind("<Button-1>", lambda event: RegisterPage3())

    payment = Label(My_Window, text="Payment Details", font=("Arial", 13), bg="white", fg="black",
                     cursor="hand2")
    payment.place(x=50, y=375)
    payment.bind("<Button-1>", lambda event: RegisterPage4())

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
    sex = StringVar()
    male_button = ctk.CTkRadioButton(My_Window, text="Male", font=("Arial", 12), text_color="white", bg_color="#060606",
                              fg_color="yellow", height=1, width=8,variable=sex, value='Male')
    male_button.place(x=910, y=320)
    female_button = ctk.CTkRadioButton(My_Window, text="Female", font=("Arial", 12), text_color="white", bg_color="#060606",
                              fg_color="yellow", height=1, width=8,variable=sex, value='Female')
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

    save_button = Button(My_Window, text="Save", command=RegisterPage2)
    save_button.place(x=1100, y=600)
    My_Window.mainloop()

def RegisterPage2():
    # change bg picture
    file_bg_window = PhotoImage(file="bgreg2.png", master=My_Window)
    bg_window = Label(My_Window, image=file_bg_window, borderwidth=0)
    bg_window.place(x=0, y=0)

    # ------ pages button ------#
    personaldetails = Label(My_Window, text="Personal Details", font=("Arial", 13), bg="#EFEFEF", fg="black",
                            cursor="hand2")
    personaldetails.place(x=50, y=195)
    personaldetails.bind("<Button-1>", lambda event: RegisterPage())

    workdetails = Label(My_Window, text="Work Details", font=("Arial", 13), bg="yellow", fg="black",
                            cursor="hand2")
    workdetails.place(x=50, y=255)
    workdetails.bind("<Button-1>", lambda event: RegisterPage2())

    employer = Label(My_Window, text="Employer Details", font=("Arial", 13), bg="#EFEFEF", fg="black",
                        cursor="hand2")
    employer.place(x=50, y=315)
    employer.bind("<Button-1>", lambda event: RegisterPage3())

    payment = Label(My_Window, text="Payment Details", font=("Arial", 13), bg="#EFEFEF", fg="black",
                     cursor="hand2")
    payment.place(x=50, y=375)
    payment.bind("<Button-1>", lambda event: RegisterPage4())

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


    My_Window.mainloop()

def save_login():
    MIDCode = MIDCode_textbox.get('1.0', tk.END).strip()
    password = password_textbox.get().strip()

    query = "INSERT INTO login (MIDCode, Password) VALUES (%s, %s)"
    cursor.execute(query, (MIDCode, password))
    cnx.commit()


Register()