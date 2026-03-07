# PostBoard - Simple Terminal Application

users = {}
posts = []

# -----------------------------
# Register User
# -----------------------------
def register():
    username = input("Enter username: ")

    if username in users:
        print("Username already exists")
        return

    password = input("Enter password: ")
    users[username] = password
    print("Registration successful")


# -----------------------------
# Login
# -----------------------------
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print("Login successful")
        return username
    else:
        print("Invalid login")
        return None


# -----------------------------
# Create Post
# -----------------------------
def create_post(username):

    title = input("Enter post title: ")
    description = input("Enter description: ")
    date = input("Enter date: ")

    post = {
        "author": username,
        "title": title,
        "description": description,
        "date": date
    }

    posts.append(post)

    print("Post created successfully")


# -----------------------------
# View All Posts
# -----------------------------
def view_posts():

    if len(posts) == 0:
        print("No posts available")
        return

    for post in posts:
        print("\nAuthor:", post["author"])
        print("Title:", post["title"])
        print("Date:", post["date"])
        print("Description:", post["description"])


# -----------------------------
# Search Post By Username
# -----------------------------
def search_post():

    name = input("Enter username to search posts: ")

    found = False

    for post in posts:
        if post["author"] == name:
            print("\nTitle:", post["title"])
            print("Date:", post["date"])
            print("Description:", post["description"])
            found = True

    if found == False:
        print("No posts found for this user")


# -----------------------------
# Main Menu
# -----------------------------
def main():

    while True:

        print("\n----- POSTBOARD MENU -----")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register()

        elif choice == "2":
            user = login()

            if user != None:

                while True:

                    print("\n1. Create Post")
                    print("2. View All Posts")
                    print("3. Search Post by Username")
                    print("4. Logout")

                    ch = input("Enter choice: ")

                    if ch == "1":
                        create_post(user)

                    elif ch == "2":
                        view_posts()

                    elif ch == "3":
                        search_post()

                    elif ch == "4":
                        break

        elif choice == "3":
            print("Exiting program")
            break


main()