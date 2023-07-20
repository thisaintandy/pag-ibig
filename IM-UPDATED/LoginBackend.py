import tkinter as tk
import mysql.connector


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
    MIDCode = MIDCode_textbox.get()
    password = password_textbox.get()
    login = check_credentials(MIDCode, password)

    if login:
        print("Login successful. User ID:", login)
        retrieve_details(login)
    else:
        print("Invalid username or password.")

def LoginPage():
    global MIDCode_textbox, password_textbox

    My_Window = tk.Tk()

    # Set the window size and position
    window_width = 1200
    window_height = 675
    screen_width = My_Window.winfo_screenwidth()
    screen_height = My_Window.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    My_Window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Disable window resizing
    My_Window.resizable(False, False)

    # put background picture
    file_bg_login = tk.PhotoImage(file="login.png")
    bg_login = tk.Label(My_Window, image=file_bg_login, borderwidth=0)
    bg_login.place(x=0, y=0)

    # put textbox for MIDCode
    MIDCode_textbox = tk.Entry(My_Window, font=("Arial", 20))
    MIDCode_textbox.place(x=100, y=275)

    # put textbox for password
    password_textbox = tk.Entry(My_Window, font=("Arial", 20), show="*")
    password_textbox.place(x=100, y=375)

    # put enter button
    file_enterbutton = tk.PhotoImage(file="enterbutton.png")
    button_enter = tk.Button(My_Window, image=file_enterbutton, activebackground="yellow", height=41, width=120,
                          borderwidth=0, bd=0, relief=tk.FLAT, command=login_action)
    button_enter.place(x=165, y=457)

    # put create account button
    file_createaccountbutton = tk.PhotoImage(file="createaccountbutton.png")
    button_createaccount = tk.Button(My_Window, image=file_createaccountbutton, activebackground="black", height=47,
                                  width=278, borderwidth=0, bd=0, relief=tk.FLAT, command=lambda: RegisterPage1())
    button_createaccount.place(x=90, y=580)

    My_Window.mainloop()

LoginPage()
