import tkinter as tk
from tkinter import Text, Entry, Button, Label
import customtkinter as ctk
from tkinter import ttk
from PIL import Image, ImageTk
import random
import mysql.connector

def generate_random_numbers(length):
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(length))
    return random_numbers


def display_output():
    random_numbers = generate_random_numbers(10)  # Generate random numbers
    MIDCode_textbox.delete('1.0', tk.END)  # Clear previous content
    MIDCode_textbox.insert('1.0', random_numbers)  # Insert new numbers


def Register1():
    global My_Window, MIDCode_textbox, password_textbox

    My_Window = tk.Tk()
    My_Window.title("Pag-IBIG Fund")
    My_Window.geometry("1200x675+365+130")
    My_Window.resizable(width=False, height=False)

    # put background picture
    file_bg_login = tk.PhotoImage(file="login.png")
    bg_login = tk.Label(My_Window, image=file_bg_login)
    bg_login.place(x=-2, y=0)

    # put textbox for MIDCode
    MIDCode_textbox = tk.Text(My_Window, height=1, width=25, highlightbackground="#CDFFD8", highlightthickness=1)
    MIDCode_textbox.configure(font=("Comic Sans MS", 15))
    MIDCode_textbox.configure(borderwidth=0, relief="ridge", bg='LightSteelBlue1')
    MIDCode_textbox.place(x=80, y=280)

    display_button = tk.Button(My_Window, text="Generate", command=display_output)
    display_button.configure(font=("Zing Rust Base", 10), width=8, highlightbackground="#444444",
                             highlightthickness=1, activebackground="LightSteelBlue2")
    display_button.configure(borderwidth=0, relief="ridge", bg='#CDFFD8')
    display_button.place(x=310, y=283)

    # put textbox for password
    password_textbox = Entry(My_Window, show='*')
    password_textbox.configure(font=("Comic Sans MS", 15), width=25, highlightbackground="#CDFFD8",
                               highlightthickness=1)
    password_textbox.configure(borderwidth=0, relief="ridge", bg='LightSteelBlue1')
    password_textbox.place(x=80, y=370)

    def save_login():
        MIDCode = MIDCode_textbox.get('1.0', tk.END).strip()
        password = password_textbox.get().strip()

        query = "INSERT INTO login (MIDCode, Password) VALUES (%s, %s)"
        cursor.execute(query, (MIDCode, password))
        cnx.commit()
        RegisterPage()

    button = Button(My_Window, text="SIGN UP", font=("Zing Rust Base", 13, 'bold'), relief="flat", height=1, width=15,
                    bg="#CDFFD8",
                    activebackground="#CDFFD8", command=save_login)
    button.place(x=150, y=440)

    back_button = Button(My_Window, text="Back To Home", font=("Arial", 13, 'bold'), width=30, relief=tk.FLAT,
                         bg="#BCE0B6",
                         command=HomePage)
    back_button.place(x=80, y=570)

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
    sex = tk.StringVar()
    male_button = tk.Radiobutton(My_Window, text="Male", font=("Arial", 12), variable=sex, value='Male')
    male_button.place(x=910, y=320)
    female_button = tk.Radiobutton(My_Window, text="Female", font=("Arial", 12), variable=sex, value='Female')
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
        birthdate = bdate_textbox.get("1.0", "end-1c")  # Retrieve the date value after the user has entered it
        heirbday = heirbday_textbox.get("1.0", "end-1c")  # Retrieve the date value after the user has entered it

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
    global My_Window, emplno_textbox, occ_textbox, empstat_textbox, dateemp_textbox, income_textbox

    # change bg picture
    file_bg_window = ImageTk.PhotoImage(file="bgreg2.png")
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
    personaldetails.bind("<Button-1>", lambda event: RegisterPage())

    workdetails = Label(My_Window, text="Work Details", font=("Arial", 13), bg="#EFEFEF", fg="black",
                            cursor="hand2")
    workdetails.place(x=50, y=255)
    workdetails.bind("<Button-1>", lambda event: RegisterPage2())

    employer = Label(My_Window, text="Employer Details", font=("Arial", 13), bg="yellow", fg="black",
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
    personaldetails.bind("<Button-1>", lambda event: RegisterPage())

    workdetails = Label(My_Window, text="Work Details", font=("Arial", 13), bg="#EFEFEF", fg="black",
                            cursor="hand2")
    workdetails.place(x=50, y=255)
    workdetails.bind("<Button-1>", lambda event: RegisterPage2())

    employer = Label(My_Window, text="Employer Details", font=("Arial", 13), bg="#EFEFEF", fg="black",
                        cursor="hand2")
    employer.place(x=50, y=315)
    employer.bind("<Button-1>", lambda event: RegisterPage3())

    payment = Label(My_Window, text="Payment Details", font=("Arial", 13), bg="#FEFC02", fg="black",
                     cursor="hand2")
    payment.place(x=50, y=375)
    payment.bind("<Button-1>", lambda event: RegisterPage4())

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

        query = "INSERT INTO payment (MIDNumber, EmployeeNumber, MembershipCategory, MSPayment) VALUES (%s, %s, %s, %s)"
        values = (MIDCode_textbox.get("1.0", "end-1c"),
                  emplno_textbox.get("1.0", "end-1c"), membershipcat.get(), membershippay.get())
        cursor.execute(query, values)
        cnx.commit()
        Register1() # HomePage



    save_button = Button(My_Window, text="Save", command=save_details)
    save_button.place(x=1100, y=600)

    My_Window.mainloop()

def Afterlogin():
    # put background picture
    file_bg_login = tk.PhotoImage(file="afterlogin.png")
    bg_login = tk.Label(My_Window, image=file_bg_login)
    bg_login.place(x=-2, y=0)

    # log in button
    button_about = Button(My_Window, text="Log In", font=("Arial", 12, 'bold'), bg="#E4E7E8",
                          activebackground="#E4E7E8",
                          foreground="#242424", activeforeground="blue", height=1, width=8, borderwidth=0, bd=0,
                          command=lambda: HomePage())
    button_about.place(x=260, y=15)

def HomePage():
    global My_Window
    My_Window.destroy()
    Register1()


if __name__ == '__main__':
    cnx = mysql.connector.connect(
        host='localhost',
        user='andy',
        password='Andydy212003*',
        database='project_database'
    )
    cursor = cnx.cursor()
    Register1()
