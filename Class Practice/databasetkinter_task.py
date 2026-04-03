from tkinter import *
import pymysql

def submit_data():
    name = entry_name.get()
    email = entry_email.get()
    mobile = entry_mobile.get()

    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="tops@2580",
        database="student_db"
    )

    cursor = conn.cursor()

    query = "INSERT INTO users (name, email, mobile) "
    values = (name, email, mobile)

    cursor.execute(query)
    conn.commit()

    conn.close()

    print("Data Inserted Successfully!")

root = Tk()
root.title("User Form")
root.geometry("300x250")

Label(root, text="Name").pack()
entry_name = Entry(root)
entry_name.pack()

Label(root, text="Email").pack()
entry_email = Entry(root)
entry_email.pack()

Label(root, text="Mobile").pack()
entry_mobile = Entry(root)
entry_mobile.pack()

Button(root, text="Submit", command=submit_data).pack(pady=10)

root.mainloop()
