from tkinter import *
from tkinter import messagebox
import os

class User:
    def __init__(self, name):
        self.name = name

class Post:
    def __init__(self, user, title, content):
        self.user = user
        self.title = title
        self.content = content

    def save_post(self):
        filename = f"{self.user.name}_{self.title}.txt"
        with open(filename, "w") as file:
            file.write(self.content)


def save_post():
    name = entry_name.get()
    title = entry_title.get()
    content = text_content.get("1.0", END)

    if name == "" or title == "" or content.strip() == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        user = User(name)
        post = Post(user, title, content)
        post.save_post()

        messagebox.showinfo("Success", "Post Saved Successfully!")
        load_posts()

        entry_title.delete(0, END)
        text_content.delete("1.0", END)

    except Exception as e:
        messagebox.showerror("Error", str(e))


def load_posts():
    listbox_posts.delete(0, END)
    files = [f for f in os.listdir() if f.endswith(".txt")]
    
    for file in files:
        listbox_posts.insert(END, file)


def view_post():
    try:
        selected = listbox_posts.get(listbox_posts.curselection())
        
        with open(selected, "r") as file:
            content = file.read()

        text_content.delete("1.0", END)
        text_content.insert(END, content)

    except:
        messagebox.showerror("Error", "No file selected!")


root = Tk()
root.title("MiniBlog App")
root.geometry("500x500")

Label(root, text="Name").pack()
entry_name = Entry(root)
entry_name.pack()

Label(root, text="Title").pack()
entry_title = Entry(root)
entry_title.pack()

Label(root, text="Content").pack()
text_content = Text(root, height=10)
text_content.pack()

Button(root, text="Save Post", command=save_post).pack(pady=5)
Button(root, text="View Selected Post", command=view_post).pack(pady=5)

listbox_posts = Listbox(root)
listbox_posts.pack(fill=BOTH, expand=True)

load_posts()

root.mainloop()