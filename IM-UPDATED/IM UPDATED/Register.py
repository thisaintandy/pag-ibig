import mysql.connector
import random
from tkinter import *
import getpass

# Replace the placeholders with your database details
cnx = mysql.connector.connect(
    host='localhost',
    user='andy',
    password='Andydy212003*',
    database='project_database'
)

cursor = cnx.cursor()

# Function to generate random numbers
def generate_random_numbers(length):
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(length))
    return random_numbers

# Generate MIDCode
MIDCode = generate_random_numbers(11)
print("MIDCode:", MIDCode)

# Insert MIDCode and password into login table
query = "INSERT INTO login (MIDCode, Password) VALUES (%s, %s)"
password = input("Enter your password: ")
cursor.execute(query, (MIDCode, password))
cnx.commit()

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
    male_button = Radiobutton(My_Window, text="Male", font=("Arial", 12), bg="white", activebackground="white",
                              foreground="#060606",
                              activeforeground="#060606", height=1, width=8, bd=0, borderwidth=0, relief=FLAT,
                              variable=sex, value='Male')
    male_button.place(x=910, y=341)
    female_button = Radiobutton(My_Window, text="Female", font=("Arial", 12), bg="white", activebackground="white",
                                foreground="#060606",
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

    query = "INSERT INTO memberdetails (Name, Birthdate,Birthplace, Sex, Spouse, Status,Citizenship, Father, Mother)VALUES( %s, %s, %s, %s, %s, %s, %s,%s, %s)"
    values = (name_textbox, bdate_textbox, bplace_textbox, sex, spouse_textbox, status_textbox, citizenship_textbox, father_textbox, mother_texbox)
    cursor.execute(query, values)
    cnx.commit()

    cursor.close()
    cnx.close()

    # ----- buttons for other pages ----- #"

    # personal information
    button_personal = Button(My_Window, text="Personal Information", font=("Arial", 13), bg="yellow",
                             activebackground="yellow",
                             foreground="#242424", activeforeground="#242424", height=1, width=19, borderwidth=0, bd=0,
                             relief=FLAT,
                             command=lambda: RegisterPage())
    button_personal.place(x=40, y=192)

    # account
    button_account = Button(My_Window, text="Account", font=("Arial", 13), bg="white", activebackground="white",
                            foreground="#242424", activeforeground="#242424", height=1, width=19, borderwidth=0, bd=0,
                            relief=FLAT,
                            command=lambda: AccountPage())
    button_account.place(x=40, y=252)

    # current work
    button_currentwork = Button(My_Window, text="Current Work", font=("Arial", 13), bg="white",
                                activebackground="white",
                                foreground="#242424", activeforeground="#242424", height=1, width=19, borderwidth=0,
                                bd=0, relief=FLAT,
                                command=lambda: CurrentWorkPage())
    button_currentwork.place(x=40, y=312)

    # previous work
    button_previouswork = Button(My_Window, text="Previous Work", font=("Arial", 13), bg="white",
                                 activebackground="white",
                                 foreground="#242424", activeforeground="#242424", height=1, width=19, borderwidth=0,
                                 bd=0, relief=FLAT,
                                 command=lambda: PreviousWorkPage())
    button_previouswork.place(x=40, y=372)

    # other information
    button_otherinfo = Button(My_Window, text="Other Information", font=("Arial", 13), bg="white",
                              activebackground="white",
                              foreground="#242424", activeforeground="#242424", height=1, width=19, borderwidth=0, bd=0,
                              relief=FLAT,
                              command=lambda: OtherInfoPage())
    button_otherinfo.place(x=40, y=432)

    # ----- SAVE BUTTON ----- #
    save_button = Button(My_Window, text="Save", font=("Arial", 11, 'bold'), bg="yellow", activebackground="yellow",
                         foreground="#242424", activeforeground="#242424", height=1, width=9, borderwidth=0, bd=0,
                         relief=FLAT)
    save_button.place(x=1040, y=595)

    My_Window.mainloop()


