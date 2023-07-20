import mysql.connector
from tkinter import *
from tkinter import ttk

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="andy",
    password="Andydy212003*",
    database="project_database"
)

# Create the Tkinter window
root = Tk()

# Create a Treeview widget for the first table
tree1 = ttk.Treeview(root)
tree1.pack(fill=BOTH, expand=True)

# Retrieve data from the first table
cursor1 = db.cursor()

# Condition 1: Show all columns

cursor1.execute("SELECT * FROM memberdetails WHERE YEAR(Birthdate) = 2002")  # Replace with your first table name
column_names1 = [column[0] for column in cursor1.description]


rows1 = cursor1.fetchall()

# Determine the number of columns for the first table
num_columns1 = len(column_names1)

# Set the columns for the first table in the Treeview widget
tree1["columns"] = tuple(f"column{i+1}" for i in range(num_columns1))
tree1.heading("#0", text=column_names1[0])
for i, column_name in enumerate(column_names1[1:]):
    tree1.heading(f"column{i+1}", text=column_name)
    tree1.column("#0", width=90, minwidth=85)
    # Adjust the column width based on the content
    tree1.column(f"column{i+1}", width=82, minwidth=80, stretch=True)
    tree1.heading(f"column{i+1}", text=column_name, anchor=CENTER)

# Insert data from the first table into the Treeview widget
for row in rows1:
    tree1.insert("", "end", text=row[0], values=row[1:num_columns1+1])

# ... Rest of the code ...

# Close the database connections
cursor1.close()


# Resize the space
root.geometry("1400x800")

# Start the Tkinter event loop
root.mainloop()
